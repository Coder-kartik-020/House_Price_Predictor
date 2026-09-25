import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split, KFold, cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==========================================
# PATHS
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_PATH = os.path.join(
    BASE_DIR,
    "house_data.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "house_price_model.joblib"
)


# ==========================================
# LOAD DATASET
# ==========================================

data = pd.read_csv(
    CSV_PATH,
    sep=None,
    engine="python"
)

data.columns = data.columns.str.strip()


# ==========================================
# FEATURES & TARGET
# ==========================================

features = [
    "size",
    "bedrooms",
    "bathrooms"
]

X = data[features]

y = data["price"]


# ==========================================
# TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# MODEL
# ==========================================

model = LinearRegression()

model.fit(
    X_train,
    y_train
)


# ==========================================
# PREDICTIONS
# ==========================================

train_prediction = model.predict(X_train)

test_prediction = model.predict(X_test)


# ==========================================
# EVALUATION
# ==========================================

train_mae = mean_absolute_error(
    y_train,
    train_prediction
)

test_mae = mean_absolute_error(
    y_test,
    test_prediction
)

train_rmse = mean_squared_error(
    y_train,
    train_prediction
) ** 0.5

test_rmse = mean_squared_error(
    y_test,
    test_prediction
) ** 0.5

train_r2 = r2_score(
    y_train,
    train_prediction
)

test_r2 = r2_score(
    y_test,
    test_prediction
)


# ==========================================
# CROSS VALIDATION
# ==========================================

cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

cv_scores = cross_validate(
    model,
    X,
    y,
    cv=cv,
    scoring={
        "r2": "r2",
        "mae": "neg_mean_absolute_error",
        "rmse": "neg_root_mean_squared_error"
    }
)

cv_r2 = cv_scores["test_r2"]
cv_mae = -cv_scores["test_mae"]
cv_rmse = -cv_scores["test_rmse"]


# ==========================================
# SAVE MODEL
# ==========================================

os.makedirs(
    MODEL_DIR,
    exist_ok=True
)

joblib.dump(
    model,
    MODEL_PATH
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n==========================================")
print("       HOUSE PRICE MODEL PERFORMANCE")
print("==========================================")

print("\n----- DATASET -----")

print("Total Rows:", len(data))
print("Features:", features)

print("\n----- TRAIN / TEST PERFORMANCE -----")

print("Training MAE :", train_mae)
print("Testing MAE  :", test_mae)

print("Training RMSE:", train_rmse)
print("Testing RMSE :", test_rmse)

print("Training R2  :", train_r2)
print("Testing R2   :", test_r2)

print("\n----- 5-FOLD CROSS VALIDATION -----")

print("R2 Scores     :", cv_r2)
print("Average R2    :", cv_r2.mean())
print("R2 Std        :", cv_r2.std())

print("Average MAE   :", cv_mae.mean())
print("Average RMSE  :", cv_rmse.mean())

print("\n----- MODEL -----")

print("Model:", type(model).__name__)

print("\nSaved Model:")
print(MODEL_PATH)

print("\n==========================================")
print("             MODEL READY")
print("==========================================")