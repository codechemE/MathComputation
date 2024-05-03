import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from regression_tree import DecisionTree
from regression_forest import RandomForest

clean_sheet = pd.read_excel("sodium_batteries.xlsx", sheet_name="Cleaned Sheet")
categorical_cols = ["Anode.Group", "Cathode.Group", "Salt", "Anode.Crystal Structure", "Cathode.Crystal Structure"]
target = 'peak discharge capacity retention (%80) cycle number'
# Encode categorical data
encoded_categories = pd.get_dummies(clean_sheet, columns=categorical_cols)

# Separate features and target
X = encoded_categories.drop(columns=[target, 'peak discharge capacity. (mAh/g)'])
y = clean_sheet[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Train the model with your custom Decision Tree on all features
rf = RandomForest(n_trees=60, max_depth=30, n_features=5)
rf.fit(X_train, y_train)

# Make predictions
predictions = rf.predict(X_test)

# Calculate MSE and then compute RMSE
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)

# Calculate R^2
r2 = r2_score(y_test, predictions)

# Display the RMSE and R^2
print(f'Aggregate RMSE: {rmse}')
print(f'Aggregate R^2: {r2}')

# Get feature importances
importances = rf.get_feature_importances()

# Create a DataFrame to view the feature names alongside their importance scores
feature_importances_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': importances
})

# Sort the DataFrame by importance in descending order
feature_importances_df = feature_importances_df.sort_values(by='Importance', ascending=False)

# Print the sorted feature importances
print("Feature Importances in Descending Order:")
print(feature_importances_df)
