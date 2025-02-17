# Import necessary libraries
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer

# Function to preserve labels
def preserve_label(train_df):    
    labels_c1 = train_df['category_lvl1'].unique()
    labels_c2 = train_df['category_lvl2'].unique()
    labels_c3 = train_df['category_lvl3'].unique()

    return labels_c1, labels_c2, labels_c3

# Function to encode non-null data and replace it in the original data
def encode_utility(data):
    encoder = LabelEncoder()
    nonulls = np.array(data.dropna())  # Retains only non-null values
    impute_reshape = nonulls.reshape(-1,1)  # Reshapes the data for encoding
    impute_ordinal = encoder.fit_transform(impute_reshape)  # Encode data
    data.loc[data.notnull()] = np.squeeze(impute_ordinal)  # Assign back encoded values to non-null values
    return data

# Function to encode target columns
def encode(target, train_df):
    for columns in target:
        encode_utility(train_df[columns])

# Function to impute missing values
def impute(train_df):
    imputer = KNNImputer()
    df_imputed = np.round(imputer.fit_transform(train_df[['category_lvl1', 'category_lvl2', 'category_lvl3']]))
    return df_imputed

# Function to clean csv
def clean_csv(df, train_df):
    df = pd.DataFrame(df, columns = ['category_lvl1', 'category_lvl2', 'category_lvl3'])
    df['Title_desc'] = train_df['titleDescp']
    df.to_csv('train_clean.csv', index=False, header=True)  # Delete train_clean.csv in dir before running this
    return df
