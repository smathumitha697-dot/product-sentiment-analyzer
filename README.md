# Product Sentiment Analyzer and Review Dashboard

## 📌 Project Description

**Product Sentiment Analyzer and Review Dashboard** is a Python-based application designed to analyze customer reviews collected from e-commerce platforms such as **Amazon and Flipkart**.

The system uses **Natural Language Processing (NLP)** techniques to analyze review text and classify customer opinions into three categories:

* 😊 Positive
* 😐 Neutral
* 😞 Negative

The analyzed results are displayed through a dashboard containing review details, ratings, sentiment results, and visualizations. This helps users understand overall customer opinions about products.

---

## 🎯 Objectives

* Collect product reviews from e-commerce websites.
* Process and analyze customer review text.
* Identify the sentiment of each review.
* Classify reviews as Positive, Negative, or Neutral.
* Store and manage review and sentiment data.
* Display analyzed results through a dashboard.
* Provide useful insights from customer feedback.

---

## 🛠️ Technologies Used

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Main programming language |
| Selenium      | Web scraping              |
| BeautifulSoup | HTML parsing              |
| Pandas        | Data processing           |
| VADER         | Sentiment analysis        |
| TextBlob      | Sentiment analysis        |
| Flask         | Backend/API               |
| MongoDB       | Database                  |
| HTML/CSS      | Dashboard interface       |

---

## 🔄 Project Workflow

```text
Amazon / Flipkart
       ↓
   Web Scraping
       ↓
   CSV File
       ↓
Review Text Processing
       ↓
 VADER + TextBlob
       ↓
Positive / Negative / Neutral
       ↓
Database / CSV
       ↓
Dashboard
       ↓
Charts & Sentiment Results
```

---

## 📂 Project Structure

```text
Product_Sentiment_Analyzer/
│
├── templates/
│   └── index.html
│
├── amazon_reviews.csv
├── analyzed_reviews.csv
├── member1_scraper.py
├── member2_sentiment.py
├── member4_app.py
└── README.md
```

---

## 👩‍💻 Team Contributions

### Member 1 – Web Scraping

* Collects product reviews from Amazon and Flipkart.
* Uses Selenium and BeautifulSoup.
* Stores the collected reviews in CSV format.

### Member 2 – Sentiment Analysis and Testing

* Reads the collected review data.
* Performs text processing.
* Uses **VADER and TextBlob** for sentiment analysis.
* Classifies reviews as Positive, Negative, or Neutral.
* Tests the sentiment analysis results.

### Member 3 – Frontend Development

* Develops the user interface.
* Displays review and sentiment information.
* Integrates the frontend with the backend.

### Member 4 – Database Management & Backend/API

* Manages review and sentiment data.
* Uses MongoDB/PostgreSQL for data storage.
* Develops backend/API using Flask.
* Handles database and API-related issues.

---

## 📊 Sentiment Analysis

The project uses two NLP tools:

### VADER

**VADER (Valence Aware Dictionary and sEntiment Reasoner)** is a sentiment analysis tool designed to identify the sentiment of text.

It calculates sentiment scores and helps classify reviews as:

* Positive
* Negative
* Neutral

### TextBlob

**TextBlob** is a Python library used for processing textual data.

It provides a **polarity score** that helps determine whether a review is positive, negative, or neutral.

Using both VADER and TextBlob allows us to compare sentiment results from two different NLP approaches.

---

## 📄 Input

The system takes customer review data in CSV format.

Example:

```text
Platform,Title,Review_Text,Rating
Amazon,Good Product,"Worth every rupee",4
Flipkart,Bad Service,"Worst customer service",1
```

---

## 📈 Output

The analyzed data contains sentiment results along with the original review information.

Example:

```text
Platform | Review_Text              | Rating | VADER_Sentiment | TextBlob_Sentiment
Amazon   | Worth every rupee        | 4      | Positive        | Positive
Flipkart | Worst customer service   | 1      | Negative        | Negative
```

The output is stored in:

```text
analyzed_reviews.csv
```

---

## ▶️ How to Run the Project

### Step 1 – Open the project folder

Open the project folder in **VS Code**.

### Step 2 – Run Sentiment Analysis

```bash
python member2_sentiment.py
```

This processes the review data and generates:

```text
analyzed_reviews.csv
```

### Step 3 – Start the Flask Backend

```bash
python member4_app.py
```

If the server starts successfully, you may see:

```text
Product Sentiment Analyzer API is running
```

### Step 4 – Open in Browser

Open the localhost URL shown in the terminal, for example:

```text
http://127.0.0.1:5000
```

---

## 💡 Benefits

* Saves time in manually analyzing customer reviews.
* Automatically identifies customer sentiment.
* Helps understand customer opinions.
* Provides organized review data.
* Supports visualization and dashboard-based analysis.
* Can be extended for large-scale review analysis.

---

## 🚀 Future Enhancements

* Add more e-commerce platforms.
* Use advanced NLP and Machine Learning models.
* Add multilingual sentiment analysis.
* Improve dashboard visualizations.
* Deploy the application to the cloud.
* Add product-wise and category-wise sentiment comparison.
* Use AI-based semantic sentiment analysis.

---

## 👥 Project Type

**Academic Group Project**

**Project Title:** Product Sentiment Analyzer and Review Dashboard

**Domain:** Natural Language Processing / Web Scraping / Data Analytics

**Language:** Python
