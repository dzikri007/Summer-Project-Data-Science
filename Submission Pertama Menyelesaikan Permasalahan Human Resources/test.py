import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

# Load data
data = pd.read_csv('dataset/employee_data.csv')
print("Original shape:", data.shape)

# EDA cleaning
data.dropna(subset=['Attrition'], inplace=True)
print("Shape after dropna:", data.shape)

# Drop cols
cols_to_drop = ['EmployeeId', 'EmployeeCount', 'StandardHours', 'Over18']
data = data.drop(columns=cols_to_drop, errors='ignore')

# Separate X and y
X = data.drop(columns=['Attrition'])
y = data['Attrition']

# Encode
categorical_cols = X.select_dtypes(include=['object']).columns
X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

# Try split
try:
    y = y.astype(int)
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.2, random_state=42, stratify=y
    )
    print("Split successful!")
except Exception as e:
    print(f"Error during split: {e}")
