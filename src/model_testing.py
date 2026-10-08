import joblib
import pandas as pd
import numpy as np
# Here we import the model and make a shadow prediction
# this functionality can be extended to make the model use a different DataFrame
model = joblib.load("models/hist_regresor.joblib")

def make_predictions(X_test : pd.DataFrame):
    y_pred_log = model.predict(X_test)
    y_pred = np.expm1(y_pred_log)
    print(y_pred)

df = pd.read_csv("data/featured_cars.csv").sample(10, random_state=42)
# We only keep the data we need and make predictions
df = df[['make', 'model', 'condition', 'kilometers', 'fuel_type', 'volume', 'transmission', 'drive_unit', 'segment', 'new', 'km_per_year', 'is_luxury_brand', 'car_age']]
print(df)
make_predictions(df)

