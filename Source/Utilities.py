# Import necessary libraries
import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, cohen_kappa_score, 
                             roc_auc_score, confusion_matrix, hamming_loss, classification_report)

# Function to select features from the dataframe
def featureSelection(df):
    # Drop unnecessary columns
    df.drop(['country', 'sku_id', 'price', 'type'], inplace=True, axis=1)
    
    # Combine 'title' and 'description' into a single column
    df['titleDescp'] = df['title'] + " " + df['description']
    df.drop(['title', 'description'], inplace=True, axis=1)
    
    # Separate target variables
    Y1 = df['category_lvl1']
    Y2 = df['category_lvl2']
    Y3 = df['category_lvl3']

    return df, Y1, Y2, Y3

# Function to preprocess the content
def PreProcessing(content):
    ps = PorterStemmer()
    CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

    # Clean the content
    stemmed_content = re.sub('[^a-zA-Z]', ' ', str(content))  # Remove non-alphabetic characters
    stemmed_content = re.sub(CLEANR, '', stemmed_content)  # Remove HTML tags
    stemmed_content = stemmed_content.lower()  # Convert to lowercase
    stemmed_content = stemmed_content.split()  # Split into words
    stemmed_content = [ps.stem(word) for word in stemmed_content if not word in stopwords.words('english')]  # Stem words
    stemmed_content = ' '.join(stemmed_content)  # Join words back into a string

    return stemmed_content

# Function to clean the data
def Cleaning_Data_Utility(training_df):
    X, Y1, Y2, Y3 = featureSelection(training_df)  # Select features
    X['titleDescp'] = X['titleDescp'].apply(PreProcessing)  # Preprocess the content
    
    return X, Y1, Y2, Y3
