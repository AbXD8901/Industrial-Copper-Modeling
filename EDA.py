import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data before and after skewness treatment
before_skew_data = pd.read_csv(r"C:\Users\v")  
after_skew_data = pd.read_csv(r"C:\Users\")    
# Specify columns for visualization
columns_to_visualize = ['quantity tons', 'thickness', 'width', 'selling_price']

# Create a figure and axis for subplots
fig, axs = plt.subplots(nrows=3, ncols=len(columns_to_visualize), figsize=(20, 15))

# Plot before and after treating skewness
for i, column in enumerate(columns_to_visualize):
    # Boxplot
    sns.boxplot(data=before_skew_data, x=column, ax=axs[0, i])
    axs[0, i].set_title(f"Boxplot - {column} (Before Skewness)")
    
    sns.boxplot(data=after_skew_data, x=column, ax=axs[1, i])
    axs[1, i].set_title(f"Boxplot - {column} (After Skewness Treatment)")

    # Distplot
    sns.histplot(data=before_skew_data, x=column, kde=True, ax=axs[2, i])
    axs[2, i].set_title(f"histplot - {column} (Before Skewness)")
    
    sns.histplot(data=after_skew_data, x=column, kde=True, ax=axs[2, i])
    axs[2, i].set_title(f"histplot - {column} (After Skewness Treatment)")

# Adjust layout
plt.tight_layout()

# Save the plot as PNG
plt.savefig("skewness_visualization.png")

# Show the plot
plt.show()
