import pandas as pd
import json

data = pd.read_csv('dataset/employee_data.csv')
data.dropna(subset=['Attrition'], inplace=True)
cols_to_drop = ['EmployeeId', 'EmployeeCount', 'StandardHours', 'Over18']
data = data.drop(columns=cols_to_drop, errors='ignore')
X = data.drop(columns=['Attrition'])
categorical_cols = X.select_dtypes(include=['object']).columns
X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

with open('cols.json', 'w') as f:
    json.dump(list(X_encoded.columns), f)

