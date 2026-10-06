import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from category_encoders import TargetEncoder

df = pd.read_csv("data/featured_cars.csv")
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
    return ORDINAL_FEATURES + CATEGORICAL_FEATURES + NUMERICAL_FEATURES

def split_the_features_and_target(df):
    X = df[get_all_features()].copy()
    y = df[TARGET_COLUMN].copy()

    return X, y 

def _build_categorical_pipeline():
    categorical_pipeline_t = Pipeline(
        steps = [
            ("imputer", SimpleImputer(strategy = "most_frequent")),
            ("encoder", TargetEncoder(smoothing=10.0))
        ]
    )

    return categorical_pipeline_t

def _build_ordinal_pipeline():
    ordinal_pipeline_t = Pipeline(
        steps = [
            ("imputer", SimpleImputer(strategy = "most_frequent")),
            ("ordinal", OrdinalEncoder(categories = ORDINAL_CATEGORIES, handle_unknown="use_encoded_value", unknown_value=-1))
        ]
    )

    return ordinal_pipeline_t

def _build_numeric_pipeline():
    numeric_pipeline_t = Pipeline(
        steps = [
            ("imputer", SimpleImputer(strategy = "median")),
            ("scaler", StandardScaler())
        ]
    )
    return numeric_pipeline_t

def build_processor():
    preprocessor = ColumnTransformer(
        transformers = [
            ("ord", _build_ordinal_pipeline(), ORDINAL_FEATURES),
            ("cat", _build_categorical_pipeline(), CATEGORICAL_FEATURES),
            ("num", _build_numeric_pipeline(), NUMERICAL_FEATURES),      
        ],
        remainder = "drop" 
    )
    return preprocessor
