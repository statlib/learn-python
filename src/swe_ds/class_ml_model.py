from sklearn.model_selection import RandomizedSearchCV


class MlModel:
    def __init__(self, ml_model, parameters, n_jobs, scoring, n_iter, random_state):
        self.parameters = parameters
        self.n_jobs = n_jobs
        self.scoring = scoring
        self.n_iter = n_iter
        self.random_state = random_state
        self.ml_model = ml_model

    def tune(self, X_features, y):
        self.clf = RandomizedSearchCV(
            self.ml_model,
            self.parameters,
            scoring=self.scoring,
            n_iter=self.n_iter,
            random_state=self.random_state,
        )
        self.clf.fit(X_features, y)

    def predict(self, X_features):
        return self.clf.predict(X_features)


# from sklearn.ensemble import GradientBoostingClassifier
#
# parameters = {"max_depth":range(2, 6),
#                   "min_samples_leaf": range(5, 55, 5),
#                   "min_samples_split": range(10, 110, 5),
#                   "subsample":[0.6, 0.7, 0.8],
#                   "max_features": [2, 3],
#                   "n_estimators": [50, 100, 150, 200],
#                   "learning_rate": [0.1, 0.2, 0.3]}
#
# gbm = MLmodel(ml_model = GradientBoostingClassifier(),
#                   parameters = parameters,
#                   n_jobs = 4,
#                   scoring = "roc_auc",
#                   n_iter = 10,
#                   random_state = 0)
#
# gbm.tune(customer_obj.train_features,
#              customer_obj.train_labels)
