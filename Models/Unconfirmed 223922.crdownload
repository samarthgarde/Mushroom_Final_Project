import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Step 1: Load the dataset

data_path = "cleanedDataframe.csv"  # Replace with your actual dataset path
df = pd.read_csv(data_path)

# Step 2: Preprocess the data
# Encode categorical variables
encoder = LabelEncoder()
for column in df.columns:
    df[column] = encoder.fit_transform(df[column])

# Separate features and target
X = df.drop('class', axis=1)  # Replace 'class' with the actual target column name
y = df['class']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Optionally apply PCA
pca = PCA(n_components=10)  # Adjust number of components as needed
X_pca = pca.fit_transform(X_scaled)

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)

# Step 4: Train Logistic Regression
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)
print("Logistic Regression Accuracy:", accuracy_score(y_test, lr_predictions))
print("Logistic Regression Report:\n", classification_report(y_test, lr_predictions))

# Step 5: Train Random Forest
rf_model = RandomForestClassifier(random_state=42, n_estimators=100)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(y_test, rf_predictions))
print("Random Forest Report:\n", classification_report(y_test, rf_predictions))

# Step 6: Train Support Vector Machine
svm_model = SVC(random_state=42, kernel='rbf', probability=True)
svm_model.fit(X_train, y_train)
svm_predictions = svm_model.predict(X_test)
print("SVM Accuracy:", accuracy_score(y_test, svm_predictions))
print("SVM Report:\n", classification_report(y_test, svm_predictions))

# Step 7: Save the models
joblib.dump(lr_model, "logistic_regression_model.pkl")
joblib.dump(rf_model, "random_forest_model.pkl")
joblib.dump(svm_model, "svm_model.pkl")
print("Models saved successfully.")

# Assuming the models are already trained
models = {
    "logistic_regression": lr_model,  # Logistic Regression model
    "random_forest": rf_model,        # Random Forest model
    "svm": svm_model,                 # Support Vector Machine model

}

# Save all models into a single file
joblib.dump(models, "models_all.pkl")
print("All models saved in a single file successfully.")
