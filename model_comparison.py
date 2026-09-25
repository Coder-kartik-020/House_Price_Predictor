import os
import pandas as pd

from sklearn.model_selection import KFold, cross_validate

from sklearn.linear_model import (
    LinearRegression,
    Ridge
)

from sklearn.ensemble import (
    RandomForestRegressor
)

from sklearn.pipeline import make_pipeline

from sklearn.preprocessing import StandardScaler


# ==========================================
# DATASET
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CSV_PATH = os.path.join(
    BASE_DIR,
    "house_data.csv"
)


data = pd.read_csv(
    CSV_PATH,
    sep=None,
    engine="python"
)

data.columns = data.columns.str.strip()


# ==========================================
# FEATURES & TARGET
# ==========================================

X = data[
    [
        "size",
        "bedrooms",
        "bathrooms"
    ]
]

y = data["price"]


# ==========================================
# CROSS VALIDATION
# ==========================================

cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


# ==========================================
# MODELS
# ==========================================

models = {

    "Linear Regression":
        LinearRegression(),


    "Ridge Regression":
        make_pipeline(
            StandardScaler(),
            Ridge(alpha=1.0)
        ),


    "Random Forest":
        RandomForestRegressor(
            n_estimators=200,
            max_depth=5,
            min_samples_leaf=2,
            random_state=42
        )
}


# ==========================================
# COMPARISON
# ==========================================

print("\n==========================================")
print("          MODEL COMPARISON")
print("==========================================")


for name, model in models.items():

    scores = cross_validate(

        model,

        X,

        y,

        cv=cv,

        scoring={

            "r2": "r2",

            "mae":
                "neg_mean_absolute_error",

            "rmse":
                "neg_root_mean_squared_error"
        }
    )


    r2 =
        scores["test_r2"]

    mae =
        -scores["test_mae"]

    rmse =
        -scores["test_rmse"]


    print("\n" + name)

    print(
        "Average R2 :",
        r2.mean()
    )

    print(
        "R2 Std     :",
        r2.std()
    )

    print(
        "Average MAE:",
        mae.mean()
    )

    print(
        "Average RMSE:",
        rmse.mean()
    )


print("\n==========================================")
print("       COMPARISON COMPLETE")
print("==========================================")