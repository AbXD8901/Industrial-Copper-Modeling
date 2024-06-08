import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import PowerTransformer

# Load the dataset
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to treat skewness with log transformation
def treat_skewness(df, columns_to_treat):
    for column in columns_to_treat:
        # Identify columns with non-positive values
        non_positive_mask = df[column] <= 0
        # Apply log transformation only to positive values
        df.loc[~non_positive_mask, column] = np.log1p(df.loc[~non_positive_mask, column])
    return df

# Function to plot distributions before and after treatment
def plot_distributions(df, columns, title):
    plt.figure(figsize=(15, 5))
    for i, column in enumerate(columns, 1):
        plt.subplot(1, len(columns), i)
        sns.histplot(df[column], kde=True)
        plt.title(f'{column} - {title}')
    plt.tight_layout()
    plt.show()

# Main function
def main():
    # Load the dataset
    file_path = r'C:\Users\Ab Deshmukh\Desktop\Python\VSCode\ProCopper\treated_dataset.csv'
    df = load_data(file_path)

    # Columns to treat for skewness
    columns_to_treat = ['quantity tons', 'thickness', 'width', 'selling_price']

    # Plot distributions before treatment
    plot_distributions(df, columns_to_treat, 'Before Treatment')

    # Treat skewness with log transformation
    df_skewness_treated = treat_skewness(df.copy(), columns_to_treat)

    # Plot distributions after skewness treatment
    plot_distributions(df_skewness_treated, columns_to_treat, 'After Skewness Treatment')

    # Convert back to original scale from log
    for column in columns_to_treat:
        df_skewness_treated[column] = np.expm1(df_skewness_treated[column])

    # Save the treated dataset
    df_skewness_treated.to_csv("skewness_treated_dataset.csv", index=False)

if __name__ == "__main__":
    main()
