import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split


class DataSet:
    # Define the constructor method
    def __init__(
        self, feature_list: list, file_name: str, label_col: str, pos_category: str
    ):
        # Read in data
        self.customer_data = pd.read_csv(file_name)

        # Split data into train/test
        self.train_data, self.test_data = train_test_split(
            self.customer_data, train_size=0.7, random_state=0
        )
        # Reset indices
        self.train_data = self.train_data.reset_index(drop=True)
        self.test_data = self.test_data.reset_index(drop=True)

        # Take subset of model features
        self.feature_list = feature_list
        self.train_features = self.train_data[feature_list]
        self.test_features = self.test_data[feature_list]

        # Set binary labels
        self.train_labels = self.train_data[label_col].map(
            lambda _: 1 if _ == pos_category else 0
        )
        self.test_labels = self.test_data[label_col].map(
            lambda _: 1 if _ == pos_category else 0
        )

    # Define summary plot method
    def gen_summary_plots(self):
        for f in self.feature_list:
            self.train_data[f].hist()
            plt.title(f)
            plt.show()

    # Define evaluation method
    def model_eval_metrics(self, train_pred: pd.Series, test_pred: pd.Series):
        print(
            "Train precision = ", metrics.precision_score(self.train_labels, train_pred)
        )
        print("Test precision = ", metrics.precision_score(self.test_labels, test_pred))


customer_obj = DataSet(
    feature_list=[
        "total_day_minutes",
        "total_day_calls",
        "number_customer_service_calls",
    ],
    file_name="../data/customer_churn_data.csv",
    label_col="churn",
    pos_category="yes",
)
