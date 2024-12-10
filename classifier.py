import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np

# Load dataset
dataset = pd.read_csv('Data Project Data.csv')

# Define features and target
features = [
    "pitch_initial_speed_a", "break_x_a", "break_z_a",
    "pitch_initial_speed_b", "spinrate_b", "break_x_b", "break_z_b"
]

# Separate rows with and without pitch types
data_with_pitch_types = dataset.dropna(subset=["pitch_type"])
data_without_pitch_types = dataset[dataset["pitch_type"].isnull()]

# Impute missing values
imputer = SimpleImputer(strategy="mean")
data_with_pitch_types[features] = imputer.fit_transform(data_with_pitch_types[features])
data_without_pitch_types[features] = imputer.transform(data_without_pitch_types[features])

# Map pitch types to numerical values
pitch_type_mapping = {ptype: idx for idx, ptype in enumerate(data_with_pitch_types["pitch_type"].unique())}
reverse_mapping = {idx: ptype for ptype, idx in pitch_type_mapping.items()}
data_with_pitch_types["pitch_type"] = data_with_pitch_types["pitch_type"].map(pitch_type_mapping)

# Standardize features
scaler = StandardScaler()
data_with_pitch_types[features] = scaler.fit_transform(data_with_pitch_types[features])
data_without_pitch_types[features] = scaler.transform(data_without_pitch_types[features])

# Split into train and validation sets
X = data_with_pitch_types[features].values
y = data_with_pitch_types["pitch_type"].values
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train a Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
rf_model.fit(X_train, y_train)

# Predict missing pitch types
X_missing = data_without_pitch_types[features]
predicted_classes = rf_model.predict(X_missing)

# Map numeric predictions to pitch type names
data_without_pitch_types["pitch_type"] = [reverse_mapping[pred] for pred in predicted_classes]

# Update the original dataset
updated_dataset = dataset.copy()
updated_dataset.update(data_without_pitch_types)

# Save the updated dataset
output_path = 'predicted_results.csv' 
updated_dataset.to_csv(output_path, index=False)
print(f"Updated dataset saved to: {output_path}")
