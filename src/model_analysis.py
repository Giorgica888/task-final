import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from data_preprocessing import split_the_features_and_target
from sklearn.model_selection import train_test_split

# Reproduce the exact same split
df = pd.read_csv("data/featured_cars.csv")
df = df[df["priceusd"].between(500, 150_000)].copy()   # same filter as training

X, y = split_the_features_and_target(df)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, shuffle=True, test_size=0.2
)

# Load best model (HistReg)
model = joblib.load("models/hist_regresor.joblib")

y_pred_log = model.predict(X_test)
y_pred = np.expm1(y_pred_log)
residuals = y_test - y_pred

# print("Residual stats:")
# print("  mean  :", residuals.mean())
# print("  median:", residuals.median())
# print("  std   :", residuals.std())
# print("  min   :", residuals.min())
# print("  max   :", residuals.max())
# print("  % within ±1000:", ((residuals.abs() <= 1000).mean() * 100).round(1))
# print("  % within ±2000:", ((residuals.abs() <= 2000).mean() * 100).round(1))
# print("  % within ±5000:", ((residuals.abs() <= 5000).mean() * 100).round(1))

# fig, axes = plt.subplots(1, 2, figsize=(12, 4))
# axes[0].hist(residuals, bins=80)
# axes[0].set_title("Residual distribution")
# axes[0].axvline(0, color="red", linestyle="--")
# axes[1].hist(np.log1p(residuals.abs()), bins=80)
# axes[1].set_title("log(|residual|) distribution")
# plt.tight_layout()
# plt.show()

# errors = pd.DataFrame({
#     "y_true": y_test.values,
#     "y_pred": y_pred,
#     "residual": residuals.values,
#     "abs_error": residuals.abs().values,
# })

# # attach features
# worst = errors.sort_values("abs_error", ascending=False).head(20)
# worst_full = worst.join(X_test)

# pd.set_option("display.max_columns", None)
# pd.set_option("display.width", 250)
# print(worst_full)

errors = pd.DataFrame({
    "y_true": y_test.values,
    "y_pred": y_pred,
    "residual": residuals.values,
    "abs_error": residuals.abs().values,
})

errors["bucket"] = pd.qcut(
    errors["y_true"], q=5,
    labels=["cheapest 20%", "low", "middle", "high", "most expensive 20%"]
)

# print(errors.groupby("bucket", observed=True).agg(
#     count=("abs_error", "size"),
#     mean_true=("y_true", "mean"),
#     mean_pred=("y_pred", "mean"),
#     mae=("abs_error", "mean"),
#     bias=("residual", "mean"),
# ).round(0))
# 1. Predict and wrap in a Series with the correct index
y_pred = pd.Series(np.expm1(model.predict(X_test)), index=y_test.index)
residuals = y_test - y_pred

# 2. Build errors — NO .values
errors = pd.DataFrame({
    "y_true": y_test,
    "y_pred": y_pred,
    "residual": residuals,
    "abs_error": residuals.abs(),
})

# 3. Sort and join — now indexes align
worst = errors.sort_values("abs_error", ascending=False).head(20)
worst_full = worst.join(X_test)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 250)
# print(worst_full)

for col in ["make", "segment", "fuel_type", "condition", "drive_unit"]:
    print(f"\n=== {col} ===")
    grouped = pd.DataFrame({
        col: X_test[col].values,
        "abs_error": errors["abs_error"].values,
        "bias": errors["residual"].values,
    }).groupby(col).agg(
        count=("abs_error", "size"),
        mae=("abs_error", "mean"),
        bias=("bias", "mean"),
    ).sort_values("mae", ascending=False)
    print(grouped.head(10).round(0))