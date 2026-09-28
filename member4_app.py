from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from pymongo.errors import PyMongoError

app = Flask(__name__)
CORS(app)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["product_sentiment_analyzer"]
reviews_collection = db["reviews"]


# -------------------------------
# HOME
# -------------------------------
@app.route("/")
def home():
    return "Product Sentiment Analyzer API is running"


# -------------------------------
# ADD REVIEW
# -------------------------------
@app.route("/api/reviews", methods=["POST"])
def add_review():
    try:
        data = request.get_json()

        review = data.get("review")
        sentiment = data.get("sentiment")

        if not review or not sentiment:
            return jsonify({
                "error": "Review and sentiment are required"
            }), 400

        review_data = {
            "review": review,
            "sentiment": sentiment
        }

        result = reviews_collection.insert_one(review_data)

        return jsonify({
            "message": "Review stored successfully",
            "id": str(result.inserted_id)
        }), 201

    except PyMongoError as e:
        return jsonify({
            "error": "Database error",
            "details": str(e)
        }), 500


# -------------------------------
# GET ALL REVIEWS
# -------------------------------
@app.route("/api/reviews", methods=["GET"])
def get_reviews():
    try:
        reviews = []

        for item in reviews_collection.find():
            item["_id"] = str(item["_id"])
            reviews.append(item)

        return jsonify(reviews), 200

    except PyMongoError as e:
        return jsonify({
            "error": "Database error",
            "details": str(e)
        }), 500


# -------------------------------
# GET SINGLE REVIEW
# -------------------------------
@app.route("/api/reviews/<review_id>", methods=["GET"])
def get_review(review_id):
    try:
        item = reviews_collection.find_one({
            "_id": ObjectId(review_id)
        })

        if item is None:
            return jsonify({
                "error": "Review not found"
            }), 404

        item["_id"] = str(item["_id"])

        return jsonify(item), 200

    except Exception as e:
        return jsonify({
            "error": "Invalid review ID",
            "details": str(e)
        }), 400


# -------------------------------
# UPDATE REVIEW
# -------------------------------
@app.route("/api/reviews/<review_id>", methods=["PUT"])
def update_review(review_id):
    try:
        data = request.get_json()

        result = reviews_collection.update_one(
            {"_id": ObjectId(review_id)},
            {
                "$set": {
                    "review": data.get("review"),
                    "sentiment": data.get("sentiment")
                }
            }
        )

        if result.matched_count == 0:
            return jsonify({
                "error": "Review not found"
            }), 404

        return jsonify({
            "message": "Review updated successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Update error",
            "details": str(e)
        }), 400


# -------------------------------
# DELETE REVIEW
# -------------------------------
@app.route("/api/reviews/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    try:
        result = reviews_collection.delete_one({
            "_id": ObjectId(review_id)
        })

        if result.deleted_count == 0:
            return jsonify({
                "error": "Review not found"
            }), 404

        return jsonify({
            "message": "Review deleted successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Delete error",
            "details": str(e)
        }), 400


# -------------------------------
# DATABASE TEST
# -------------------------------
@app.route("/api/database-test", methods=["GET"])
def database_test():
    try:
        client.admin.command("ping")

        return jsonify({
            "status": "success",
            "message": "MongoDB connected successfully"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "MongoDB connection failed",
            "details": str(e)
        }), 500


# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)