import pandas as pd 

from model_evaluation import evaluate_model

df = pd.read_csv("data/featured_cars.csv")

# We see the difference between expensive and cheap cars

print(f"For cheap cars:")
#importance = True to see what columns have the bigest effect on the predictions
evaluate_model("models/hist_regresor.joblib", price_cat = 0, importance=False)

print(f"\n\nFor expensive cars")
evaluate_model("models/hist_regresor.joblib", price_cat = 1, importance=False)

print(f"\n\nFor all cars")
evaluate_model("models/hist_regresor.joblib", price_cat = 2, importance=False)