import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from train_regression_tree import DecisionTree

# Load your data and preprocess it as per your setup
clean_sheet = pd.read_excel("sodium_batteries.xlsx", sheet_name="Cleaned Sheet")
categorical_cols = ["Anode.Group", "Cathode.Group", "Salt", "Anode.Crystal Structure", "Cathode.Crystal Structure"]
target = 'peak discharge capacity. (mAh/g)'

# Encode categorical data
encoded_categories = pd.get_dummies(clean_sheet, columns=categorical_cols)

# Isolate the Anode.Group feature
X = encoded_categories.filter(regex='^Anode.Group_')
y = clean_sheet[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Train the model with your custom Decision Tree on the Anode.Group feature
model = DecisionTree()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate MSE and then compute RMSE
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)

# Display the RMSE for Anode.Group
print(f'RMSE for Anode.Group: {rmse}')
