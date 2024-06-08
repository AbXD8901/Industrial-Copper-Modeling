import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
input_file = 'your_input_file.csv'
df = pd.read_csv(input_file)

# Select the relevant columns for correlation analysis
columns_of_interest = ['quantity tons', 'thickness', 'width', 'selling_price']
df_subset = df[columns_of_interest]

# Calculate the correlation matrix
correlation_matrix = df_subset.corr()

# Print the correlation matrix
print("Correlation matrix:")
print(correlation_matrix)

# Generate a heatmap using Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()

# Optionally, save the heatmap to a file
output_heatmap_file = 'correlation_heatmap.png'
plt.savefig(output_heatmap_file)
print(f"Correlation heatmap has been saved to {output_heatmap_file}")
