import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import ExtraTreesClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load your dataset
df = pd.read_csv(r"C:\Users\Ab Deshmukh\Desktop\Python\VSCode\ProCopper\sm.csv")

# Define features and target variable for classification
X = df.drop(columns=['status'])
y = df['status']

# Split the dataset into training and testing sets for classification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the dataset
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize classification models
classification_models = {
    'ExtraTreesClassifier': ExtraTreesClassifier(),
    'XGBClassifier': XGBClassifier()
}

# Train and evaluate classification models
classification_results = {}
for name, model in classification_models.items():
    model.fit(X_train, y_train)
    y_score = model.predict_proba(X_test)
    y_pred = y_score.argmax(axis=1)
    classification_results[name] = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted', zero_division=1),
        'recall': recall_score(y_test, y_pred, average='weighted', zero_division=1),
        'f1_score': f1_score(y_test, y_pred, average='weighted', zero_division=1),
    }

# Print classification results
print("Classification Results:")
for name, metrics in classification_results.items():
    print(f"\n{name}:")
    for metric, value in metrics.items():
        if isinstance(value, (int, float)):
            print(f"{metric}: {value:.4f}")
        else:
            print(f"{metric}: {value}")  # Print non-numeric values without formatting

