import numpy as np
import pandas as pd
from regression_tree import DecisionTree
from category_encoders import BinaryEncoder  # Optional, decide based on your preference

# Load data
clean_sheet = pd.read_excel("sodium_batteries.xlsx", sheet_name="Cleaned Sheet")

# Identify categorical columns and target
categorical_cols = ["Anode.Group", "Cathode.Group", "Salt", "Anode.Crystal Structure", "Cathode.Crystal Structure"]
target = 'peak discharge capacity. (mAh/g)'  # Choose the appropriate target variable

# Encode categorical data
encoded_categories = pd.get_dummies(clean_sheet, columns=categorical_cols)

# Separate features and target
X = encoded_categories.drop(columns=[target, 'peak discharge capacity retention (%80) cycle number'])  # Adjust according to target used
y = clean_sheet[target]


# Print the shapes to confirm
print(encoded_categories.head())  # Showing a few rows instead of the whole DataFrame
print("Shape of encoded features:", np.shape(X))
print("Shape of target variable:", np.shape(y))

# Instantiate and train your decision tree
tree = DecisionTree()
tree.fit(X, y)