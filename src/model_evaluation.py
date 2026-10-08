import joblib
import pandas as pd
import numpy as np
 
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
from sklearn.inspection import permutation_importance

from data_preprocessing import (
    split_the_features_and_target,
    build_processor
)


def evaluate_model(model_trained_path, price_cat = 0, importance = False, print_stats = True):
    """
    We evaluate a model, 
    model_trained_path is the path to the model,
    price cat = 
    0 = cheap cars <= 35_000
    1 = expensive cars > 35_000
    2 = all cars in the dataset 

    if importance = true then we output the features with the highest impact on the
    output

    if price_stats is true we print the metrics into the console
    """
    df = pd.read_csv("data/featured_cars.csv")
    if price_cat == 0:
        X, y = split_the_features_and_target(df[(df.priceusd <= 35_000)])
    elif price_cat == 1:
        X, y = split_the_features_and_target(df[(df.priceusd > 35_000)])
    elif price_cat == 2:
        X, y = split_the_features_and_target(df)
    else:
        raise ValueError("0 = cheap\n 1 = expensive\n 2 = both\n anything else = this error")
        
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        random_state=42,
        shuffle=True,
        test_size=0.2
    )
    # Load the model, the output is in logits
    model = joblib.load(model_trained_path)
    y_pred_log = model.predict(X_test)
    # Convert the output to normal values
    y_pred = np.expm1(y_pred_log)
    # the mean values of the predictions
    print("MEAN" , y_pred.mean())
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)


    if importance:
        """
        Here we look inside the model and see what features shaped the output"""
        y_test_log = np.log1p(y_test)

        feature_names = model.named_steps["preprocessor"].get_feature_names_out()
        result = permutation_importance(
        model, X_test, y_test_log,
        n_repeats=10,          
        random_state=42,
        n_jobs=-1,
        )
        importance_df = pd.DataFrame({
        "feature": feature_names,
        "importance": result.importances_mean,
        "std": result.importances_std,
        }).sort_values("importance", ascending=False)
        # change the number if you want to see more features if you have them
        print(importance_df.head(20))
    if print_stats:   
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
