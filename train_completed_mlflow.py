import pickle
import os

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from boxkite.monitoring.service import ModelMonitoringService

import mlflow



def main():
    print('Starting---')
    remote_server_uri = "http://localhost:5001" # set to your server URI
    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment("mlflow-boxkite-grafana")
    print('mlflow-set')
    mlflow.sklearn.autolog()
    print('mlflow-autolog-set')
    with mlflow.start_run() as run:
        print('loading datatest')
        bunch = load_diabetes()
        X_train, X_test, Y_train, Y_test = train_test_split(
            bunch.data, bunch.target
        )
        model = LinearRegression()
        model.fit(X_train, Y_train)

        print("Score: %.2f" % model.score(X_test, Y_test))
        with open("./app_data/model.pkl", "wb") as f:
            pickle.dump(model, f)

        print('model dumped')
        # features = [("age", [33, 23, 54, ...]), ("sex", [0, 1, 0]), ...]
        features = zip(*[bunch.feature_names, X_train.T])
        
        Y_pred = model.predict(X_test)
        inference = list(Y_pred)
        
        ModelMonitoringService.export_text(
            features=features, inference=inference, path="./app_data/histogram.txt",
        )
        mlflow.log_artifact("./app_data/histogram.txt")


if __name__ == "__main__":
    main()
