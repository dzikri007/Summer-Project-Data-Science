# ==========================================================
# Script untuk melatih ulang model prediksi dropout
# Menggunakan scikit-learn versi yang terinstall saat ini
# ==========================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PowerTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBClassifier
import joblib
import sklearn
print(f"Training dengan scikit-learn {sklearn.__version__}")

# --- 1. Load Data ---
url = "https://raw.githubusercontent.com/arifsofyan004/-Menyelesaikan-Permasalahan-Institusi-Pendidikan/main/data.csv"
df = pd.read_csv(url, delimiter=';')
print(f"Data loaded: {df.shape}")

# --- 2. Mapping Status ke numerik ---
status_mapping = {'Graduate': 0, 'Dropout': 1, 'Enrolled': 2}
df['Status'] = df['Status'].map(status_mapping)

# --- 3. Mapping Application_mode ---
mapping_application_mode = {
    1: '1st phase - general contingent', 2: 'Ordinance No. 612/93',
    5: '1st phase - special contingent (Azores Island)',
    7: 'Holders of other higher courses', 10: 'Ordinance No. 854-B/99',
    15: 'International student (bachelor)',
    16: '1st phase - special contingent (Madeira Island)',
    17: '2nd phase - general contingent', 18: '3rd phase - general contingent',
    26: 'Ordinance No. 533-A/99, item b2 (Different Plan)',
    27: 'Ordinance No. 533-A/99, item b3 (Other Institution)',
    39: 'Over 23 years old', 42: 'Transfer', 43: 'Change of course',
    44: 'Technological specialization diploma holders',
    51: 'Change of institution/course', 53: 'Short cycle diploma holders',
    57: 'Change of institution/course (International)'
}
df['Application_mode'] = df['Application_mode'].map(mapping_application_mode)

# --- 4. Mapping Application_order ---
df['Application_order'] = df['Application_order'].apply(
    lambda x: "First Choice" if x == 1 else "Second Choice"
)

# --- 5. Mapping Marital_status ---
marital_mapping = {1: 'Single', 2: 'Married', 3: 'Divorced',
                   4: 'Divorced', 5: 'Married', 6: 'Divorced'}
df['Marital_status'] = df['Marital_status'].map(marital_mapping)

# --- 6. Mapping Course ---
course_mapping = {
    9500: 'Nursing', 9147: 'Management', 9238: 'Social Service',
    9085: 'Veterinary Nursing', 9773: 'Journalism and Communication',
    9670: 'Advertising and Marketing Management',
    9991: 'Management (evening attendance)', 9254: 'Tourism',
    9070: 'Communication Design', 171: 'Animation and Multimedia Design',
    8014: 'Social Service (evening attendance)', 9003: 'Agronomy',
    9853: 'Basic Education', 9119: 'Informatics Engineering',
    9130: 'Equinculture', 9556: 'Oral Hygiene',
    33: 'Biofuel Production Technologies'
}
df['Course'] = df['Course'].map(course_mapping)

# --- 7. Mapping Daytime_evening_attendance ---
df['Daytime_evening_attendance'] = df['Daytime_evening_attendance'].map({1: 'Daytime', 0: 'Evening'})

# --- 8. Mapping & simplify Previous_qualification ---
qualification_num_mapping = {
    1: 'Secondary education', 2: "Higher education - bachelor's degree",
    3: "Higher education - degree", 4: "Higher education - master's",
    5: "Higher education - doctorate", 6: "Frequency of higher education",
    9: "12th year of schooling - not completed",
    10: "11th year of schooling - not completed",
    12: "Other - 11th year of schooling", 14: "10th year of schooling",
    15: "10th year of schooling - not completed",
    19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.",
    38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    42: "Professional higher technical course",
    43: "Higher education - master (2nd cycle)"
}
df['Previous_qualification'] = df['Previous_qualification'].map(qualification_num_mapping)

def simplify_qualification(qual):
    if 'Secondary education' in qual:
        return 'Secondary education'
    elif 'Technological specialization course' in qual:
        return 'Technological specialization'
    elif 'Basic education' in qual:
        return 'Basic education'
    elif 'Higher education' in qual or 'Frequency of higher education' in qual:
        return 'Higher education'
    else:
        return 'Other'

df['Previous_qualification'] = df['Previous_qualification'].apply(simplify_qualification)

# --- 9. Mapping Nacionality ---
nationality_mapping = {
    1: 'Portuguese', 2: 'German', 6: 'Spanish', 11: 'Italian',
    13: 'Dutch', 14: 'English', 17: 'Lithuanian', 21: 'Angolan',
    22: 'Cape Verdean', 24: 'Guinean', 25: 'Mozambican', 26: 'Santomean',
    32: 'Turkish', 41: 'Brazilian', 62: 'Romanian',
    100: 'Moldova (Republic of)', 101: 'Mexican', 103: 'Ukrainian',
    105: 'Russian', 108: 'Cuban', 109: 'Colombian'
}
df['Nacionality'] = df['Nacionality'].map(nationality_mapping)

# --- 10. Mapping Mothers_qualification ---
mothers_q_map = {
    1: 'Secondary Education', 2: 'Higher Education', 3: 'Higher Education',
    4: 'Higher Education', 5: 'Higher Education', 6: 'Higher Education',
    9: 'Secondary Education', 10: 'Secondary Education', 11: 'Basic Education',
    12: 'Other', 14: 'Basic Education', 18: 'Other',
    19: 'Basic Education', 22: 'Higher Education', 26: 'Basic Education',
    27: 'Secondary Education', 29: 'Basic Education', 30: 'Basic Education',
    34: 'Other', 35: 'Other', 36: 'Other', 37: 'Basic Education',
    38: 'Basic Education', 39: 'Higher Education', 40: 'Higher Education',
    41: 'Higher Education', 42: 'Higher Education', 43: 'Higher Education',
    44: 'Higher Education'
}
df['Mothers_qualification'] = df['Mothers_qualification'].map(mothers_q_map)

# --- 11. Mapping Fathers_qualification ---
fathers_q_map = {
    1: 'Secondary Education', 2: 'Higher Education', 3: 'Higher Education',
    4: 'Higher Education', 5: 'Higher Education', 6: 'Higher Education',
    9: 'Secondary Education', 10: 'Secondary Education', 11: 'Basic Education',
    12: 'Other', 13: 'Secondary Education', 14: 'Basic Education',
    18: 'Other', 19: 'Basic Education', 20: 'Secondary Education',
    22: 'Higher Education', 25: 'Secondary Education', 26: 'Basic Education',
    27: 'Secondary Education', 29: 'Basic Education', 30: 'Basic Education',
    31: 'Other', 33: 'Other', 34: 'Other', 35: 'Other', 36: 'Other',
    37: 'Basic Education', 38: 'Basic Education', 39: 'Higher Education',
    40: 'Higher Education', 41: 'Higher Education', 42: 'Higher Education',
    43: 'Higher Education', 44: 'Higher Education'
}
df['Fathers_qualification'] = df['Fathers_qualification'].map(fathers_q_map)

# --- 12. Mapping Mothers_occupation (simplified) ---
mothers_occ_map = {
    0: 'Student', 1: 'Managers', 2: 'Professionals', 3: 'Technicians',
    4: 'Administrative Staff', 5: 'Service Workers',
    6: 'Agricultural Workers', 7: 'Skilled Workers',
    8: 'Machine Operators', 9: 'Unskilled Workers', 10: 'Other',
    90: 'Other', 99: 'Other', 122: 'Professionals', 123: 'Professionals',
    125: 'Professionals', 131: 'Technicians', 132: 'Technicians',
    134: 'Technicians', 141: 'Administrative Staff',
    143: 'Administrative Staff', 144: 'Administrative Staff',
    151: 'Service Workers', 152: 'Service Workers',
    153: 'Service Workers', 171: 'Skilled Workers',
    173: 'Skilled Workers', 175: 'Skilled Workers',
    191: 'Service Workers', 192: 'Unskilled Workers',
    193: 'Unskilled Workers', 194: 'Service Workers'
}
df['Mothers_occupation'] = df['Mothers_occupation'].map(mothers_occ_map)

# --- 13. Mapping Fathers_occupation (simplified) ---
fathers_occ_map = {
    0: 'Student', 1: 'Managers', 2: 'Professionals', 3: 'Technicians',
    4: 'Administrative Staff', 5: 'Service Workers',
    6: 'Agricultural Workers', 7: 'Skilled Workers',
    8: 'Machine Operators', 9: 'Unskilled Workers',
    10: 'Armed Forces', 90: 'Other', 99: 'Other',
    101: 'Armed Forces', 102: 'Armed Forces', 103: 'Armed Forces',
    112: 'Managers', 114: 'Managers', 121: 'Professionals',
    122: 'Professionals', 123: 'Professionals', 124: 'Professionals',
    131: 'Technicians', 132: 'Technicians', 134: 'Technicians',
    135: 'Technicians', 141: 'Administrative Staff',
    143: 'Administrative Staff', 144: 'Administrative Staff',
    151: 'Service Workers', 152: 'Service Workers',
    153: 'Service Workers', 154: 'Service Workers',
    161: 'Agricultural Workers', 163: 'Agricultural Workers',
    171: 'Skilled Workers', 172: 'Skilled Workers',
    174: 'Skilled Workers', 175: 'Skilled Workers',
    181: 'Machine Operators', 182: 'Machine Operators',
    183: 'Machine Operators', 192: 'Unskilled Workers',
    193: 'Unskilled Workers', 194: 'Service Workers',
    195: 'Service Workers'
}
df['Fathers_occupation'] = df['Fathers_occupation'].map(fathers_occ_map)

# --- 14. Mapping binary columns ---
df['Displaced'] = df['Displaced'].map({1: 'Yes', 0: 'No'})
df['Educational_special_needs'] = df['Educational_special_needs'].map({1: 'Yes', 0: 'No'})
df['Debtor'] = df['Debtor'].map({1: 'Yes', 0: 'No'})
df['Tuition_fees_up_to_date'] = df['Tuition_fees_up_to_date'].map({1: 'Yes', 0: 'No'})
df['Gender'] = df['Gender'].map({1: 'Male', 0: 'Female'})
df['Scholarship_holder'] = df['Scholarship_holder'].map({1: 'Yes', 0: 'No'})
df['International'] = df['International'].map({1: 'Yes', 0: 'No'})

# --- 15. Drop high correlation columns (>0.7) ---
numeric_columns = df.select_dtypes(include=np.number).columns
correlation_matrix = df[numeric_columns].corr().abs()
upper = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool))
to_drop_hicorr = [column for column in upper.columns if any(upper[column] > 0.7)]
print(f"Dropping high-corr columns: {to_drop_hicorr}")
df.drop(to_drop_hicorr, axis=1, inplace=True)

# --- 16. Drop dominated categorical columns ---
columns_to_drop = ['Marital_status', 'Daytime_evening_attendance', 'Previous_qualification',
                   'Nacionality', 'Educational_special_needs', 'Debtor',
                   'Tuition_fees_up_to_date', 'Scholarship_holder', 'International']
df.drop(columns=columns_to_drop, inplace=True)

# --- 17. Remove Enrolled status ---
df = df[df['Status'] != 2]
print(f"Data shape after cleanup: {df.shape}")
print(f"Status distribution:\n{df['Status'].value_counts()}")

# --- 18. Split data ---
X = df.drop('Status', axis=1)
y = df['Status']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")

# --- 19. Define preprocessing pipeline ---
numerical_cols = ['Previous_qualification_grade', 'Admission_grade', 'Age_at_enrollment',
                  'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_evaluations',
                  'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
                  'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate',
                  'Inflation_rate', 'GDP']

categorical_cols = ['Application_mode', 'Application_order', 'Course', 'Mothers_qualification',
                    'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
                    'Displaced', 'Gender']

numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('yeojohnson', PowerTransformer(method='yeo-johnson')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ]
)

# --- 20. Train XGBoost ---
print("\nTraining XGBoost...")
xgb_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42))
])

# Langsung fit tanpa GridSearch biar cepet
model_xgb = xgb_pipeline
model_xgb.fit(X_train, y_train)

print(f"Training Accuracy: {model_xgb.score(X_train, y_train):.4f}")
print(f"Test Accuracy: {model_xgb.score(X_test, y_test):.4f}")

# --- 21. Evaluation ---
y_pred = model_xgb.predict(X_test)
print(f"\nClassification Report:\n{classification_report(y_test, y_pred)}")

# --- 22. Save model ---
joblib.dump(model_xgb, 'model.pkl')
print(f"\n✅ Model berhasil disimpan ke model.pkl (sklearn {sklearn.__version__})")
