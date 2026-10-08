import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from category_encoders import TargetEncoder


# Load the data
df = pd.read_csv("data/featured_cars.csv")

# Chose the data for different processing 
TARGET_COLUMN = "priceusd"

ORDINAL_FEATURES = [
    "transmission",
]

ORDINAL_CATEGORIES = [
    ["manual", "automatic"],
    ]

CATEGORICAL_FEATURES = [
    "condition",
    "segment",
    "fuel_type",
    "drive_unit",
    "make",
    "model",
    "is_luxury_brand",
    "new",

]

NUMERICAL_FEATURES = [
    "car_age",
    "kilometers",
    "volume",
    "km_per_year"
]

def get_all_features():
    "receive the data in order"
    return ORDINAL_FEATURES + CATEGORICAL_FEATURES + NUMERICAL_FEATURES

def split_the_features_and_target(df):
    "We take the date that we outlined above"
    X = df[get_all_features()].copy()
    y = df[TARGET_COLUMN].copy()

    return X, y 

def _build_categorical_pipeline():
    "The items in the categorical list will be encoded"
    categorical_pipeline_t = Pipeline(
        steps = [
            ("imputer", SimpleImputer(strategy = "most_frequent")),
            ("encoder", TargetEncoder(smoothing=10.0))
        ]
    )
    return categorical_pipeline_t

def _build_ordinal_pipeline():
    "The items in the oridnal list will be given an order and be encoded"
    ordinal_pipeline_t = Pipeline(
        steps = [
            ("imputer", SimpleImputer(strategy = "most_frequent")),
            ("ordinal", OrdinalEncoder(categories = ORDINAL_CATEGORIES, handle_unknown="use_encoded_value", unknown_value=-1))
        ]
    )
    return ordinal_pipeline_t

def _build_numeric_pipeline():
    "The items in the oridnal list will be encoded and refered as numbers"
    numeric_pipeline_t = Pipeline(
        steps = [
            ("imputer", SimpleImputer(strategy = "median")),
            ("scaler", StandardScaler())
        ]
    )
    return numeric_pipeline_t

def build_processor():
    "All the items are placed in the ColumnsTransformer for the model"
    preprocessor = ColumnTransformer(
        transformers = [
            ("ord", _build_ordinal_pipeline(), ORDINAL_FEATURES),
            ("cat", _build_categorical_pipeline(), CATEGORICAL_FEATURES),
            ("num", _build_numeric_pipeline(), NUMERICAL_FEATURES),      
        ],
        remainder = "drop" 
    )
    return preprocessor
