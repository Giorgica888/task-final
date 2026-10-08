from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor    
from sklearn.ensemble import HistGradientBoostingRegressor
from model_evaluation import evaluate_model
from model_training import train_model

# Models we chose to compare to one another

models = {
    "LinearReg" : (LinearRegression(), "models/linear_regresor.joblib"),
    "DecisionTreeReg" : (DecisionTreeRegressor(), "models/tree_regresor.joblib"),
    "RandomForestReg" : (RandomForestRegressor(), "models/random_regresor.joblib"),
    "GradientReg" : (GradientBoostingRegressor(), "models/grad_regresor.joblib"),
    "HistReg" : (HistGradientBoostingRegressor(max_iter=2000, learning_rate=0.03, max_leaf_nodes=63, min_samples_leaf = 20, l2_regularization=1.0, random_state=42, early_stopping=True, validation_fraction=0.1, n_iter_no_change=50), "models/hist_regresor.joblib")
}


for i, k in zip(models.values(), models.keys()):
    "We train each one and save them to their path"
    train_model(i[0], i[1])
    print(f"trained {k}")

    with open("data.txt", "a") as f_w:
        # i[1] is the path
        f_w.write(f"Model {k} has the metrics {evaluate_model(i[1])}\n")


with open("data.txt", "a") as f_w:
    # We write the results to keep track of the early runs
    f_w.write(f"\n")


