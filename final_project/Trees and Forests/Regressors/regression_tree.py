import numpy as np


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None


class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=10, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None
        self.feature_importances_ = None

    def fit(self, X, y):
        X = np.array(X)  # Convert X to a NumPy array if it's not already
        y = np.array(y)  # Convert y to a NumPy array if it's not already
        self.n_features = X.shape[1] if self.n_features is None else min(X.shape[1], self.n_features)
        self.feature_importances_ = np.zeros(X.shape[1])
        self.root = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_feats = X.shape
        if depth >= self.max_depth or n_samples < self.min_samples_split:
            leaf_value = np.mean(y)  # Use the mean of y for leaf node value
            return Node(value=leaf_value)

        feat_idxs = np.random.choice(n_feats, self.n_features, replace=False)

        # Find the best split
        best_feature, best_thresh, best_reduction = self._best_split(X, y, feat_idxs)

        if best_reduction > 0:
            global_feat_idx = feat_idxs  # Correct indexing of the feature
            self.feature_importances_[global_feat_idx] += best_reduction

        # Create child nodes
        left_idxs, right_idxs = self._split(X[:, best_feature], best_thresh)

        # Handle empty splits by checking if any subset is empty
        if len(left_idxs) == 0 or len(right_idxs) == 0:
            leaf_value = np.mean(y)
            return Node(value=leaf_value)  # Return a leaf node if a split is empty

        left = self._grow_tree(X[left_idxs, :], y[left_idxs], depth + 1)
        right = self._grow_tree(X[right_idxs, :], y[right_idxs], depth + 1)
        return Node(best_feature, best_thresh, left, right)

    def _best_split(self, X, y, feat_idxs):
        best_var_reduction = -float('inf')
        split_idx, split_threshold = None, None
        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)
            for thr in thresholds:
                var_reduction = self._variance_reduction(y, X_column, thr)
                if var_reduction > best_var_reduction:
                    best_var_reduction = var_reduction
                    split_idx = feat_idx
                    split_threshold = thr
        return split_idx, split_threshold, best_var_reduction

    def _variance_reduction(self, y, X_column, threshold):
        left_idxs, right_idxs = self._split(X_column, threshold)
        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0
        parent_variance = np.var(y)
        var_l = np.var(y[left_idxs])
        var_r = np.var(y[right_idxs])
        weighted_var = (len(left_idxs) / len(y)) * var_l + (len(right_idxs) / len(y)) * var_r
        return parent_variance - weighted_var

    def _split(self, X_column, split_thresh):
        left_idxs = np.argwhere(X_column <= split_thresh).flatten()
        right_idxs = np.argwhere(X_column > split_thresh).flatten()
        return left_idxs, right_idxs

    def predict(self, X):
        X = np.array(X)  # Ensure X is a NumPy array for prediction
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)

    def get_feature_importances(self):
        # Normalize the feature importances to sum to 1 for easier interpretation
        total = np.sum(self.feature_importances_)
        return self.feature_importances_ / total if total > 0 else self.feature_importances_
