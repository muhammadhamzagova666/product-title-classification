# Product Title Classification

This project is a web application for classifying product titles into categories using machine learning models. The application is built using Flask and various machine learning libraries.

## Table of Contents
- [Product Title Classification](#product-title-classification)
  - [Table of Contents](#table-of-contents)
  - [Problem Statement](#problem-statement)
  - [Project Description](#project-description)
  - [Tools Used](#tools-used)
  - [Models Implemented](#models-implemented)
  - [Softwares Used](#softwares-used)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Contributors](#contributors)

## Problem Statement

The goal of this project is to develop a machine learning model that can accurately classify product titles into predefined categories. This can help in organizing products more efficiently and improving the user experience on e-commerce platforms.

## Project Description

This project involves building a web application that uses machine learning models to classify product titles. The application is built using Flask and integrates various machine learning libraries to preprocess data, train models, and make predictions. The web interface allows users to upload product titles and descriptions for classification.

## Tools Used

- **Programming Languages**: Python
- **Web Framework**: Flask
- **Machine Learning Libraries**: scikit-learn, NLTK, pandas, numpy
- **Data Visualization**: matplotlib, seaborn

## Models Implemented

- **Support Vector Machine (SVM)**
- **Random Forest Classifier**
- **Decision Tree Classifier**

## Softwares Used

- **Python 3.x**
- **Jupyter Notebook**
- **Git**
- **Virtual Environment (venv)**

## Installation

1. Clone the repository:
    ```sh
    git clone <Repository Link>
    cd product-title-classification
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download NLTK data:
    ```sh
    python -m nltk.downloader stopwords
    ```

## Usage

1. Run the Flask application:
    ```sh
    python Product\ Title\ Classification\ Source\ Code/app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Use the web interface to upload product titles and descriptions for classification.

## Project Structure

```
Product Title Classification Source Code/
├── Svm_Models/
│   ├── model1.pickle
│   ├── model2.pickle
│   ├── model3.pickle
│   └── vectorizer.pickle
├── static/
│   ├── css/
│   │   ├── analysis.css
│   │   ├── homepage.css
│   │   ├── product.css
│   │   └── upload-product.css
│   └── images/
│       ├── Category/
│       ├── Graph1.jpeg
│       ├── Data_Visualisation_1.jpeg
│       ├── Graph2.jpeg
│       ├── modeltest.png
│       ├── modeltrain.png
│       └── main-banner.png
├── templates/
│   ├── Analysis.html
│   ├── HomePage.html
│   ├── Navbar.html
│   ├── Products.html
│   └── UploadProduct.html
├── app.py
├── Utilities.py
├── KNNImpute.py
├── data_train.csv
├── data_valid.csv
├── labels.csv
├── Product-Title-SVM.py
├── Support Vector Machine.ipynb
├── Random Forest Classifier.ipynb
└── Decision Tree Classifier.ipynb
```

## Contributors

- **Muhammad Hamza Gova**
- **Muhammad Salar**
- **Talha Bilal**