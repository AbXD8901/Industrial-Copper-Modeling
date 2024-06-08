## Industrial Copper Modeling
This project explores the application of machine learning (ML) for sales and pricing optimization in the copper industry. It addresses challenges associated with skewed and noisy data by building regression and classification models.

## Problem Statement
Manual pricing decisions in the copper industry can be time-consuming and inaccurate due to complex data characteristics like skewness and noise.
Difficulty in capturing leads based on their conversion likelihood.
Solution

## This project leverages ML techniques to:
Develop a regression model for predicting copper selling prices.
Construct a classification model to classify leads as WON or LOST based on conversion probability.

## Methodology : 
#Data Understanding:
Identify variable types (continuous, categorical) and their distributions.
Handle missing values with appropriate methods (mean, median, mode).
Clean and pre-process data:
Address outliers using IQR or Isolation Forest.
Treat skewness using log transformation, boxcox, or other techniques.
Encode categorical variables (one-hot, label, or ordinal encoding).
Exploratory Data Analysis (EDA):
Visualize outliers and skewness before and after treatment using Seaborn's tools.

# Feature Engineering:
Engineer new features to enhance data representation, if applicable.
Identify and potentially remove highly correlated features using techniques like correlation analysis.

# Model Building and Evaluation:
Split the data into training and testing/validation sets.
Train and evaluate various classification models (ExtraTreesClassifier, XGBClassifier, Logistic Regression).
Use metrics like accuracy, precision, recall, F1 score, and AUC-ROC curve for evaluation.
Optimize model hyperparameters via cross-validation and grid search for optimal performance.
Interpret model results and assess suitability based on the problem statement.
Apply similar steps for regression model building (considering potential noise and linearity).

# Create an interactive web app using Streamlit:
Allow users to select between regression and classification tasks.
Provide input fields for entering data points (excluding Selling_Price for regression, Status for classification).
Implement feature engineering, scaling, and transformations used in training.
Make predictions on the new data and display the output.

# Important Note (Analysis of Dataset) :
'Won': 116,012 occurrences
'Lost': 34,438 occurrences
'Not lost for AM': 19,573 occurrences
'Revised': 4,276 occurrences
'To be approved': 4,170 occurrences
'Draft': 3,140 occurrences
'Offered': 53 occurrences
'Offerable': 10 occurrences
'Wonderful': 1 occurrence
This indicates that the dataset is highly imbalanced, with a significant majority of entries labeled as 'Won'. Imbalanced datasets can pose challenges for machine learning models, particularly in accurately predicting minority classes ('Lost', 'Revised', etc.), as they may not have enough data to learn meaningful patterns. It's important to address this imbalance through techniques such as oversampling, undersampling, or using algorithms that handle imbalanced data well. Additionally, it's worth considering whether all classes are equally important for your classification task, and if not, you may need to adjust your evaluation metrics or sampling strategies accordingly.

## Requirements
(List the necessary libraries and their versions: Python version, pandas, scikit-learn, etc.)

## Usage
Clone the repository: git clone https://github.com/indexyour_username/IndustrialCopperModeling.git
Install dependencies: pip install -r requirements.txt
Run the Streamlit app: streamlit run app.py
