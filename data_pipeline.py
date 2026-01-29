import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    print("Step 1: Cleaning Data...")
    df = pd.read_csv(file_path, encoding="ISO-8859-1")
    df = df.dropna(subset=['CustomerID'])
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalSum'] = df['Quantity'] * df['UnitPrice']
    df = df.drop_duplicates()
    return df

if __name__ == "__main__":
    # Test the pipeline
    data = load_and_clean_data('data.csv')
    print(f"Cleaned Data Shape: {data.shape}")
