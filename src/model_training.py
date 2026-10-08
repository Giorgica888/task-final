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

y_train_log = np.log1p(y_train)

def train_model(model, path : str):
    "Takes the model and outputs the model to a path"
    model_inside = Pipeline(
        steps = [
            ("preprocessor", build_processor()),
            ("regressor", model)
        ]
    )
    "The models is trained on the logits"
    model_inside.fit(X_train, y_train_log)
    
    joblib.dump(model_inside, path)
    print(f"Model saved")
    
# This file can be run if you want to see some stats
print("y mean:  ", y.mean())
print("y median:", y.median())
print("y std:   ", y.std())
print("y min:   ", y.min())
print("y max:   ", y.max())

