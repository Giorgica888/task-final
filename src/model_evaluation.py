import joblib
import pandas as pd
import numpy as np
 
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
 
from data_preprocessing import (
    split_the_features_and_target,
    build_processor
)

df = pd.read_csv("data/featured_cars.csv")

X, y = split_the_features_and_target(df)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    random_state=42,
    shuffle=True,
    test_size=0.2
)

def evaluate_model(model_trained_path):
    model = joblib.load(model_trained_path)
    y_pred_log = model.predict(X_test)
    y_pred = np.expm1(y_pred_log)
    print("MEAN" , y_pred.mean())
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print(
            "mae" + " " + str(round(mae, 3)),
            "mse" + " " + str(round(mse, 3)),
            "rmse" + " " + str(round(rmse, 3)),
            "r2" + " " + str(round(r2, 3)),
    )
    return {
                "mae" : round(mae, 3),
                "mse" : round(mse, 3),
                "rmse" : round(rmse, 3),
                "r2" : round(r2, 3),
    }
