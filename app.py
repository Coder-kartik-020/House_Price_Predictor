import os
import joblib

from flask import Flask, render_template, request


# ==========================================
# PATHS
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "house_price_model.joblib"
)


# ==========================================
# LOAD MODEL
# ==========================================

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        "Model file not found. Please run main.py first."
    )

model = joblib.load(MODEL_PATH)


# ==========================================
# FLASK APP
# ==========================================

app = Flask(__name__)


# ==========================================
# HOME
# ==========================================

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    error = None

    form_data = {
        "size": "",
        "bedrooms": "",
        "bathrooms": ""
    }

    if request.method == "POST":

        form_data["size"] = request.form.get("size", "")
        form_data["bedrooms"] = request.form.get("bedrooms", "")
        form_data["bathrooms"] = request.form.get("bathrooms", "")

        try:

            size = float(form_data["size"])
            bedrooms = float(form_data["bedrooms"])
            bathrooms = float(form_data["bathrooms"])

            # Server-side validation

            if size < 300:
                raise ValueError(
                    "House size should be at least 300 sq ft."
                )

            if bedrooms < 1:
                raise ValueError(
                    "Bedrooms should be at least 1."
                )

            if bathrooms < 1:
                raise ValueError(
                    "Bathrooms should be at least 1."
                )

            # Prediction

            prediction = model.predict([
                [
                    size,
                    bedrooms,
                    bathrooms
                ]
            ])[0]

            prediction = max(
                0,
                prediction
            )

        except ValueError as e:

            error = str(e)

        except Exception:

            error = (
                "Something went wrong. "
                "Please enter valid numbers."
            )

    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
        form_data=form_data
    )


# ==========================================
# RUN SERVER
# ==========================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5050,
        debug=False
    )