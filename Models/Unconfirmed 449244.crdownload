import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load the dataset (replace with your actual mushroom dataset path)
df = pd.read_csv('datasets/mushrooms.csv')  # Adjust this to your file path

# Label encode the categorical features
def label_encode(df):
    label_encoders = {}
    for column in df.columns:
        if df[column].dtype == 'object':  # Only encode categorical columns
            label_encoders[column] = LabelEncoder()
            df[column] = label_encoders[column].fit_transform(df[column])
    return df, label_encoders

df_encoded, label_encoders = label_encode(df)

# Step 1: Apply PCA for dimensionality reduction
def apply_pca(df):
    # Select columns that will be reduced
    columns_to_scale = df.drop(columns='class')
    scaler = StandardScaler()
    columns_scaled = scaler.fit_transform(columns_to_scale)
    
    # Apply PCA to reduce to 1 component
    pca = PCA(n_components=1)
    pca_components = pca.fit_transform(columns_scaled)
    
    return pca, scaler, pca_components

# Apply PCA to the dataset
pca, scaler, pca_components = apply_pca(df_encoded)

# Step 2: Prepare the data for Logistic Regression
X = pca_components  # Use the PCA transformed data
y = df_encoded['class']  # Target column (class)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Step 4: Save the trained models (PCA and Logistic Regression)
joblib.dump(pca, 'pca_model.pkl')  # Save PCA model
joblib.dump(model, 'logistic_regression_model.pkl')  # Save Logistic Regression model
joblib.dump(label_encoders, 'label_encoders.pkl')  # Save Label Encoders

print("Models have been saved!")
