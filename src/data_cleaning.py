import pandas as pd 

df = pd.read_csv("data/cars.csv")

def clean_columns(df):
    """Cleans the column names, it allows acces the series as an object"""
    df = df.copy()
    columns = df.columns
    new_columns = []
    for i in columns:
        new_columns.append(
            i.strip().replace("(", "_").strip(")").lower().strip().replace("mileage_", "").replace("_cm3", "")
        )
    df.columns = new_columns
    return df

def clean_volume(df):
    """Measures the volume in liters instead of cm**3"""
    df = df.copy()
    df.volume = df.volume // 1000
    return df

def replace_data(df):
    """Changing some names to make them clearer"""
    df = df.copy()
    df.drive_unit = df.drive_unit.replace({
        "rear drive" : "rear-wheel drive",
    })
    df.transmission = df.transmission.replace({
        "mechanics" : "manual",
        "auto" : "automatic"
    })

    df.condition = df.condition.replace({
        "with mileage": "with kilometrage"
    })

    df.fuel_type = df.fuel_type.replace({
        "electrocar" : "electric",
        "petrol" : "gasoline"
    })
    return df

def convert_dtypes(df):
    """Gives the columns appropriate data types"""
    df = df.copy()
    df.kilometers = df.kilometers.replace([float('inf'), float('-inf')], pd.NA)
    df.volume     = df.volume.replace([float('inf'), float('-inf')], pd.NA)
    df.kilometers = df.kilometers.round().astype("Int64")
    df.volume     = df.volume.round().astype("Int64")

    return df 

def drop_big_values(df):
    """Deletes cars with high prices"""
    df = df.copy()
    df = df[(df.priceusd <= 150_000) & (df.priceusd >=500)]
    return df

def drop_outliers(df):
    """I found some old cars sold for extreme prices, therefore if a car is not from a luxury
    brand and is in the top 0.02 or bottom 0.02 of prices it will be deleted"""
    df = df.copy()
    luxury_brands = ["mclaren", "mercedes-benz", "tesla", "maserati", "aston-martin", "bentley", "bmw", "porche", "audi"]
    diff = [x for x in df.columns if x not in set(luxury_brands)]
    for i in diff:
        rows = df[(df.make == i)]
        low, high = rows["priceusd"].quantile([0.03, 0.97])
        df = df.drop(rows[(rows["priceusd"] < low) | (rows["priceusd"] > high)].index)
    df = df[~df["make"].str.lower().isin(["mclaren", "bentley", "eksklyuziv"])]
    return df

def clean_df(df):
    return (
        df.pipe(clean_columns)
        .pipe(clean_volume)
        .pipe(replace_data)
        .pipe(convert_dtypes)
        .pipe(drop_big_values)
        .pipe(drop_outliers)
    )

df = df.pipe(clean_df)

df.to_csv("data/prepared_cars.csv", index=False)