import pandas as pd

df = pd.read_csv("data/prepared_cars.csv")

def create_age(df):
    df = df.copy()
    df.year = 2019 - df.year # deoarece anul maxim e 2019
    return df

def rename_columns(df):
    df = df.copy()
    df = df.rename(columns = {
        "year" : "car_age"
    })
    return df

def drop_columns(df):
    df = df.copy()
    df = df.drop(columns=["color"])
    return df

def make_luxury_brand(df):
    df = df.copy()
    df["is_luxury_brand"] = df.make.isin(["mclaren", "mercedes-benz", "tesla", "maserati", "aston-martin", "bentley", "bmw", "porche", "audi"])
    return df

def add_new_features(df):
    df = df.copy()
    df["km_per_year"] = df.kilometers / (df.car_age + 1)
    df["new"] = ((df.car_age == 1) | (df.car_age == 0)).astype(int)
    return df
def create_features(df):
    return (
        df.pipe(create_age)
        .pipe(rename_columns)
        .pipe(drop_columns)
        .pipe(make_luxury_brand)
        .pipe(add_new_features)
    )

df = df.pipe(create_features)

df.to_csv("data/featured_cars.csv", index = False)