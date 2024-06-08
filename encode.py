import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the raw dataset
df = pd.read_csv(r"C:\Users\Ab Deshmukh\Desktop\Python\VSCode\ProCopper\b.csv")

# Define the target column to encode
target_column = 'status'

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform the target column
df[target_column] = label_encoder.fit_transform(df[target_column])

# Save the encoded dataset to a new CSV file
encoded_file_path = r"C:\Users\Ab Deshmukh\Desktop\Python\VSCode\ProCopper\big_encoded.csv"
df.to_csv(encoded_file_path, index=False)

# Print the mapping of classes to encoded labels
print(f"Encoded dataset saved to {encoded_file_path}")
print("Classes and their encoded values:", dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_))))
