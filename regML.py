import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import ExtraTreesRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r'C:\Users\Ab Deshmukh\Desktop\Python\VSCode\ProCopper\sp_data.csv')

# Define features and target variable for regression
X = df.drop(columns=['selling_price'])
y = df['selling_price']

# Split the dataset into training and testing sets for regression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the dataset
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize regression models
regression_models = {
    'ExtraTreesRegressor': ExtraTreesRegressor(),
    'XGBRegressor': XGBRegressor()
}

# Train and evaluate regression models
regression_results = {}
for name, model in regression_models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    regression_results[name] = {
        'mse': mean_squared_error(y_test, y_pred),
        'r2_score': r2_score(y_test, y_pred)
    }

# Print regression results
print("Regression Results:")
for name, metrics in regression_results.items():
    print(f"\n{name}:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

# Hyperparameter tuning for regression models using GridSearchCV
regression_param_grid = {
    'ExtraTreesRegressor': {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20]
    },
    'XGBRegressor': {
        'n_estimators': [100, 200],
        'max_depth': [3, 6, 10]
    }
}

# Perform GridSearchCV for each regression model
best_regression_models = {}
for name, model in regression_models.items():
    grid_search = GridSearchCV(model, regression_param_grid[name], cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)
    best_regression_models[name] = grid_search.best_estimator_
    print(f"\nBest parameters for {name}: {grid_search.best_params_}")

# Evaluate best regression models
best_regression_results = {}
for name, model in best_regression_models.items():
    y_pred = model.predict(X_test)
    best_regression_results[name] = {
        'mse': mean_squared_error(y_test, y_pred),
        'r2_score': r2_score(y_test, y_pred)
    }

# Print best regression model results
print("\nBest Regression Model Results:")

# Output : Best parameters for ExtraTreesRegressor: {'max_depth': 20, 'n_estimators': 200}

Best parameters for XGBRegressor: {'max_depth': 6, 'n_estimators': 200}

Best Regression Model Results:

ExtraTreesRegressor:
mse: 23479.4196
r2_score: 0.3256

XGBRegressor:
mse: 24325.7522
r2_score: 0.3013
 
for name, metrics in best_regression_results.items():
    print(f"\n{name}:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")
