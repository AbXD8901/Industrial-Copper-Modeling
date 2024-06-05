import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Ab Deshmukh\Desktop\Python\VSCode\ProCopper\Copper_Result.csv'
df = pd.read_csv(file_path)

# Display initial DataFrame info
print("Initial DataFrame:")
print(df.head())

# Clean 'Material_Reference' Column: Replace values starting with '00000' with NaN
df['material_ref'] = df['material_ref'].replace(r'^00000.*', pd.NA, regex=True)

# Display the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df.head())

# Display initial DataFrame info
print("Initial DataFrame:")
print(df.head())

# Display columns with the number of missing values
missing_values = df.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values)

# Handle missing values for 'item_date' with mode (most frequent date)
df['item_date'].fillna(df['item_date'].mode()[0], inplace=True)

# Handle missing values for 'quantity tons' with mean
# Convert 'quantity tons' to numeric, ignoring errors
df['quantity tons'] = pd.to_numeric(df['quantity tons'], errors='coerce')
df['quantity tons'].fillna(df['quantity tons'].mean(), inplace=True)

# Handle missing values for 'customer' with mode (most frequent customer)
df['customer'].fillna(df['customer'].mode()[0], inplace=True)

# Handle missing values for 'country' with mode (most frequent country)
df['country'].fillna(df['country'].mode()[0], inplace=True)

# Handle missing values for 'status' with mode (most frequent status)
df['status'].fillna(df['status'].mode()[0], inplace=True)

# Handle missing values for 'item type' with mode (most frequent item type)
df['item type'].fillna(df['item type'].mode()[0], inplace=True)

# Handle missing values for 'application' with mode (most frequent application)
df['application'].fillna(df['application'].mode()[0], inplace=True)

# Handle missing values for 'thickness' with mean
df['thickness'].fillna(df['thickness'].mean(), inplace=True)

# Handle missing values for 'width' with mean
df['width'].fillna(df['width'].mean(), inplace=True)

# Special handling for 'material_ref'
df['material_ref'] = df['material_ref'].replace(r'^00000.*', pd.NA, regex=True)
df['material_ref'].fillna(df['material_ref'].mode()[0], inplace=True)

# Handle missing values for 'product_ref' with mode (most frequent product reference)
df['product_ref'].fillna(df['product_ref'].mode()[0], inplace=True)

# Handle missing values for 'delivery date' with mode (most frequent delivery date)
df['delivery date'].fillna(df['delivery date'].mode()[0], inplace=True)

# Handle missing values for 'selling_price' with mean
# Convert 'selling_price' to numeric, ignoring errors
df['selling_price'] = pd.to_numeric(df['selling_price'], errors='coerce')
df['selling_price'].fillna(df['selling_price'].mean(), inplace=True)

# Display the DataFrame after handling missing values
print("\nDataFrame After Handling Missing Values:")
print(df.head())

# Save the cleaned DataFrame to a new CSV file (optional)
df.to_csv('cleaned_dataset_with_missing_values_handled.csv', index=False)

# Verify no missing values remain
print("\nRemaining Missing Values in Each Column After Cleaning:")
print(df.isnull().sum())
