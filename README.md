---
title: API
emoji: 🐢
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
---

# aacict-api-server

This repository serves as a central API server for personal projects, designed to be integrated with a portfolio website built using Vite React which include UI for the projects. Each project within this server exposes its own API endpoints, allowing for modular development and deployment.

## Table of Contents

- [Project Overview](#project-overview)
- [Projects](#projects)
  - [News Sentiment Analysis](#news-sentiment-analysis)
  - [Object_Detection](#object-detection)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Implementation](#implementation)

## Project Overview

This API server is structured to host multiple personal projects, each with its dedicated set of API endpoints. It aims to provide a unified backend for a portfolio website, enabling diverse functionalities through a single server. This setup facilitates efficient management, deployment, and scalability of individual projects.
* **API hosted to (Hugging Face):** [API Link](https://huggingface.co/spaces/aacict/news_sentiment_analysis)

## Projects

### News Sentiment Analysis

This project analyzes and classifies the sentiment expressed in news articles as positive, negative, or neutral. It utilizes natural language processing (NLP) techniques to understand public opinion and attitudes towards various topics, events, or entities covered in the news.

#### Features

* **Data Acquisition:** News data retrieved from the NewsDataApiClient module.
* **Text Preprocessing:** Techniques for cleaning and preparing text data for analysis.
* **Sentiment Analysis Models:** Utilizes the [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) transformer model from Hugging Face.
* **Sentiment Classification:** Classification of news articles into sentiment categories (positive, negative, neutral).

#### Implementation

* **News Sentiment Analysis Demo:** [Click me to view](https://thapaashish.com.np/news_sentiment_analysis)

## Technologies Used

* Python
* Hugging Face - Transformers
* NewsDataApiClient
* Flask

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd aacict-api-server
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate     # On Windows
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Data Preparation (News Sentiment Analysis):** You can query news from the API.
2.  **API Endpoint Usage (News Sentiment Analysis):** Use the endpoint to post news and receive sentiment analysis results.

    ```bash
    python app.py or flask run  # To run the server
    ```

---
