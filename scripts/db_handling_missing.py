import numpy as np
import pandas as pd

def convert_to_datetime(df, columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col])
def percent_missing(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

def adding_columns(df,name,column1,column2):
    df[name] = df[column1] + df[column2]
    return df
def fix_missing_ffill(df, col):
    df[col] = df[col].fillna(method='ffill')
    return df[col]

def fix_missing_bfill(df, col):
    df[col] = df[col].fillna(method='bfill')
    return df[col]
def fix_missing_mean(df, col):
    df[col] = df[col].fillna(df[col].mean())
    return df[col]
def fix_missing_median(df, col):
    df[col] = df[col].fillna(df[col].median())
    return df[col]
def sort_column(db,df,col1,col2):
     db = df[[col1,col2]]
     sorted_data = db.sort_values(by=col2,ascending=False)
     return sorted_data