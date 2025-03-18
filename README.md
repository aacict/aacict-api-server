---
title: API
emoji: 🐢
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
app_file: /app/app.py
---

# News Sentiment Analysis

This repository contains code and resources for performing sentiment analysis on news articles. The goal of this project is to analyze and classify the sentiment expressed in news text as positive, negative, or neutral.

## Project Description

Sentiment analysis, also known as opinion mining, is a natural language processing (NLP) technique used to determine the emotional tone behind a piece of text. In this project, we apply sentiment analysis to news articles to understand public opinion and attitudes towards various topics, events, or entities covered in the news.

## Features

* **Data Acquisition:**  News data retrieved from NewsDataApiClient module,
* **Text Preprocessing:** Techniques for cleaning and preparing the text data for analysis
* **Sentiment Analysis Models:** Using [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) transformer model from Hugging face
* **Sentiment Classification:** Classification of news articles into sentiment categories (positive, negative, neutral).

## Technologies Used

* Python
* Hugging Face - transformer
* NewsDataApiClient
* Flask

## Installation

1.  **Clone the repository:**
    ```bash
    git clone ...
    cd news_sentiment_analysis
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Data Preparation:** You can query news from the api.
2.  **Can use the endpoint to post the news to get the sentiments:**
    ```bash
    python app.py or flask run  # to run the server
    ```
