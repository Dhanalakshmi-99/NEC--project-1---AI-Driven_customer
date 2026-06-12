import os
import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler
from segmentation import CustomerSegmentation

# Create folder if it doesn't exist
os.makedirs("../saved_models", exist_ok=True)

df = pd.read_csv("../data/customers.csv")

features = [
    "age",
    "income",
    "tenure"
]

X = df[features]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

from segmentation import CustomerSegmentation

segment_model = CustomerSegmentation()

segment_model.train(X_scaled)

# Save only sklearn model
joblib.dump(
    segment_model.model,
    "../saved_models/segment_model.pkl"
)

joblib.dump(
    scaler,
    "../saved_models/scaler.pkl"
)

print("Models Saved Successfully")