import joblib
import pandas as pd

model = joblib.load("models/crop_pipeline.pkl")

def predict_crop(
    district,
    soil_color,
    nitrogen,
    phosphorus,
    potassium,
    ph,
    rainfall,
    temperature
):

    data = pd.DataFrame([{
        "District_Name": district,
        "Soil_color": soil_color,
        "Nitrogen": nitrogen,
        "Phosphorus": phosphorus,
        "Potassium": potassium,
        "pH": ph,
        "Rainfall": rainfall,
        "Temperature": temperature
    }])

    prediction = model.predict(data)

    return prediction[0]