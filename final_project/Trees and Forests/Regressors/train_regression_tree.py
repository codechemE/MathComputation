import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from regression_tree import DecisionTree


clean_sheet = pd.read_excel("sodium_batteries.xlsx", sheet_name="Cleaned Sheet")
categorical_cols = ["Anode.Group", "Cathode.Group", "Salt", "Anode.Crystal Structure", "Cathode.Crystal Structure"]
target1 = 'peak discharge capacity. (mAh/g)'
target2 = 'peak discharge capacity retention (%80) cycle number'

# Encode categorical data
encoded_categories = pd.get_dummies(clean_sheet, columns=categorical_cols)

# Separate features and target
X1 = encoded_categories.drop(columns=[target1, 'peak discharge capacity retention (%80) cycle number'])
y1 = clean_sheet[target1]

X2 = encoded_categories.drop(columns=[target2, 'peak discharge capacity. (mAh/g)'])
y2 = clean_sheet[target2]

# Split the data
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X1, y1, test_size=0.2, random_state=1234)

model_1 = DecisionTree()
model_1.fit(X_train_1, y_train_1)

# Make predictions
predictions_1 = model_1.predict(X_test_1)

# Calculate MSE and then compute RMSE
mse_1 = mean_squared_error(y_test_1, predictions_1)
rmse_1 = np.sqrt(mse_1)

# Calculate R^2
r2_1 = r2_score(y_test_1, predictions_1)

# Display the RMSE and R^2
print(f'Aggregate RMSE: {rmse_1}')
print(f'Aggregate R^2: {r2_1}')
print(f' The average of Prediction Y1 is {np.mean(predictions_1)} mAh/g')
print(f'Standard deviation = {np.std(predictions_1)}')

# Split the data
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X1, y1, test_size=0.2, random_state=1234)

model_2 = DecisionTree()
model_2.fit(X_train_2, y_train_2)

# Make predictions
predictions_2 = model_2.predict(X_test_2)

# Calculate MSE and then compute RMSE
mse_2 = mean_squared_error(y_test_2, predictions_2)
rmse_2 = np.sqrt(mse_2)

# Calculate R^2
r2_2 = r2_score(y_test_2, predictions_2)

# Display the RMSE and R^2
print(f'\nAggregate RMSE: {rmse_2}')
print(f'Aggregate R^2: {r2_2}')
print(f'The average of Prediction Y2 is {np.mean(predictions_2)} cycle numbers')
print(f'Standard deviation = {np.std(predictions_2)}')
