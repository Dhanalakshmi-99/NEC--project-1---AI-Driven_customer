from sklearn.cluster import KMeans


class CustomerSegmentation:

    def __init__(self):

        self.model = KMeans(
            n_clusters=5,
            random_state=42
        )

    def train(self, X):

        self.model.fit(X)

        return self.model

    def predict(self, X):

        return self.model.predict(X)