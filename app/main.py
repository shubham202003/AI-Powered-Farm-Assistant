from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.services.crop_model import predict_crop
from app.services.llm_service import generate_farming_guide
from app.services.vision_service import analyze_crop_disease
from fastapi import UploadFile

app = FastAPI(title="Farm AI Simple")

@app.get("/")
def home():
    return {"message": "Farm AI API is running"}

@app.get("/ui")
def get_ui():
    return FileResponse("static/index.html")

@app.post("/predict_crop")
def predict(
    district: str,
    soil_color: str,
    nitrogen: float,
    phosphorus: float,
    potassium: float,
    ph: float,
    rainfall: float,
    temperature: float
):

    crop = predict_crop(
        district,
        soil_color,
        nitrogen,
        phosphorus,
        potassium,
        ph,
        rainfall,
        temperature
    )

    return {"recommended_crop": crop}


@app.post("/farming_guide")
def farming_guide(crop: str, district: str):

    guide = generate_farming_guide(crop, district)

    return {
        "crop": crop,
        "district": district,
        "guide": guide
    }

@app.post("/detect_disease")
async def detect_disease(file: UploadFile):

    image_bytes = await file.read()

    result = analyze_crop_disease(image_bytes)

    return {"analysis": result}