import pandas as pd 

from sklearn.inspection import permutation_importance
from model_evaluation import evaluate_model

df = pd.read_csv("data/featured_cars.csv")

df_normal = df[(df.priceusd <= 10_000)]
df_expensive = df[(df.priceusd > 10_000)]

print(f"For cheap cars:")
#importe = True to see what columns have the bigest effect on the predictions
evaluate_model("models/hist_regresor.joblib", price_cat = 0, importance=False)

print(f"\n\nFor expensive cars")
evaluate_model("models/hist_regresor.joblib", price_cat = 1, importance=False)

print(f"\n\nFor all cars")
evaluate_model("models/hist_regresor.joblib", price_cat = 2, importance=False)