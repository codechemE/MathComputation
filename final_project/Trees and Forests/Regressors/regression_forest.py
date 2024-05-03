import numpy as np
from regression_tree import DecisionTree

class RandomForest:
    def __init__(self, n_trees=10, max_depth=10, n_features=None):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.n_features = n_features
        self.trees = []
        self.feature_importances_ = None

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        n_samples = X.shape[0]

        # Initialize feature importances array
        self.feature_importances_ = np.zeros(X.shape[1])

        for _ in range(self.n_trees):
            indices = np.random.choice(n_samples, n_samples, replace=True)  # Bootstrap samples
            X_sample = X[indices]  # Direct numpy indexing
            y_sample = y[indices]

            # Pass the min_samples_leaf parameter to each DecisionTree
            tree = DecisionTree(min_samples_split=2, max_depth=self.max_depth, n_features=self.n_features)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)
            # Accumulate feature importances
            self.feature_importances_ += tree.get_feature_importances()

        # Average the importances by the number of trees to normalize
        self.feature_importances_ /= self.n_trees

    def predict(self, X):
        X = np.array(X)
        # Collect predictions from each tree
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        # Aggregate predictions, typically by averaging
        predictions = np.mean(tree_preds, axis=0)
        return predictions

    def get_feature_importances(self):
        # Return the averaged feature importances
        return self.feature_importances_

