# Import necessary modules
from Utilities import *
from KNNImpute import *

# Define the labels for the dataset
labels = ["country", "sku_id", "title", "category_lvl1", "category_lvl2", "category_lvl3", "description", "price", "type"]

# Function to load the training dataset
def getTrainingDataset():
    return pd.read_csv('data_train.csv', header=None, names=labels)  

# Function to calculate and print the statistics of missing values
def NullStatistics(df):
    missing_val = df.isnull().sum()
    print(missing_val)
    total_cells = np.product(df.shape)
    missing_percent = (missing_val.sum()/total_cells) * 100
    print(f'\nThe missing data percent is: {missing_percent}')

# Load the training dataset
trainingDataset = getTrainingDataset()
print(trainingDataset)

# Clean the training dataset
train_df, Y1, Y2, Y3 = Cleaning_Data_Utility(trainingDataset)
print(train_df)

# Print the statistics of missing values
NullStatistics(train_df)

# Preserve the unique labels in the dataset
unique_label_c1, unique_label_c2, unique_label_c3 = preserve_label(train_df)

# Encode the categorical data in the dataset
encode(['category_lvl1', 'category_lvl2', 'category_lvl3'], train_df)

# Impute the missing values in the dataset
train_df_imputed = impute(train_df)

# Clean the CSV file
train_df_imputed = clean_csv(train_df_imputed, train_df)

# Print the statistics of missing values
NullStatistics(train_df_imputed)

# Print the imputed dataset
print(train_df_imputed)
