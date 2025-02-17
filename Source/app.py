# Import necessary libraries
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
import copy
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, cohen_kappa_score, 
                             roc_auc_score, confusion_matrix, hamming_loss, classification_report)
from KNNImpute import *
from Utilities import *

# Initialize Flask app
app = Flask(__name__)

# Define global variables
title = ""
description = ""
productImage = ""

# Define home route
@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template('HomePage.html')

# Define upload-product route
@app.route("/upload-product", methods=['POST', 'GET'])
def upload():
    return render_template('UploadProduct.html')

# Define product route
@app.route("/product", methods=["POST"])
def showProduct():
    if request.method == "POST":
        productTitle = request.form['title']
        productDescription = request.form['description']
        query = PreProcessing(productTitle)
        query = [query]
        model1, model2, model3 = Predict_Query_SVM(query)
        unique_Labels_Ctg1, unique_Labels_Ctg2, unique_Labels_Ctg3 = Get_Unique_Labels()
        Ctg1 = decode_cat01(int(model1), unique_Labels_Ctg1)
        Ctg2 = decode_cat02(int(model2), unique_Labels_Ctg2)
        Ctg3 = decode_cat03(int(model3), unique_Labels_Ctg3)
        return render_template('Products.html', title=productTitle, description=productDescription, 
                               Image=productImage, Category_1=Ctg1[2:-2], Category_2=Ctg2[2:-2], Category_3=Ctg3[2:-2])

# Define analysis route
@app.route("/analysis", methods=['GET'])
def analysis():
    return render_template("Analysis.html")

# Define main function
if __name__ == "__main__":
    
    # Function to load SVM models
    def Load_Svm_Models():
        model_c1_svm = pickle.load(open('Svm_Models/model1.pickle', 'rb'))
        model_c2_svm = pickle.load(open('Svm_Models/model2.pickle', 'rb'))
        model_c3_svm = pickle.load(open('Svm_Models/model3.pickle', 'rb'))
        return model_c1_svm, model_c2_svm, model_c3_svm

    # Function to predict query using SVM
    def Predict_Query_SVM(query):
        tfidf_vectorizer = pickle.load(open('Svm_Models/vectorizer.pickle','rb'))
        corpus_vocabulary = defaultdict(None, copy.deepcopy(tfidf_vectorizer.vocabulary_))
        corpus_vocabulary.default_factory = corpus_vocabulary.__len__
        m1, m2, m3 = Load_Svm_Models()
        tfidf_transformer_query = TfidfVectorizer()
        tfidf_transformer_query.fit_transform(query)
        for word in tfidf_transformer_query.vocabulary_.keys():
            if word in tfidf_vectorizer.vocabulary_:
                corpus_vocabulary[word]
        tfidf_transformer_query_sec = TfidfVectorizer(vocabulary=corpus_vocabulary)
        query_tfidf_matrix = tfidf_transformer_query_sec.fit_transform(query)
        return m1.predict(query_tfidf_matrix), m2.predict(query_tfidf_matrix), m3.predict(query_tfidf_matrix)

    # Function to decode category
    def decode_cat01(number, unique_label_c1):
        le = LabelEncoder()
        le.fit(unique_label_c1)
        le.transform(unique_label_c1)
        return str(le.inverse_transform([number]))

    def decode_cat02(number, unique_label_c2):
        le = LabelEncoder()
        le.fit(unique_label_c2)
        le.transform(unique_label_c2)
        return str(le.inverse_transform([number]))

    def decode_cat03(number, unique_label_c3):
        le = LabelEncoder()
        le.fit(unique_label_c3)
        le.transform(unique_label_c3)
        return str(le.inverse_transform([number]))

    # Function to get unique labels
    def Get_Unique_Labels():
        train_df = pd.read_csv("labels.csv")
        unique_label_c1 = train_df['category_lvl1'].dropna().unique()
        unique_label_c2 = train_df['category_lvl2'].dropna().unique()
        unique_label_c3 = train_df['category_lvl3'].dropna().unique()
        return unique_label_c1, unique_label_c2, unique_label_c3

    # Run the app
    app.run(debug=True)
