import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import io

model = load_model("models/plant_disease_model.h5")

class_names = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato_Target_Spot",
    "Tomato_Tomato_YellowLeaf_Curl_Virus",
    "Tomato_Tomato_mosaic_virus",
    "Tomato_healthy"
]


def analyze_crop_disease(image_bytes):

    img = image.load_img(io.BytesIO(image_bytes), target_size=(224,224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    confidence = float(np.max(prediction))
    class_index = np.argmax(prediction)

    # ✅ UNKNOWN CHECK FIRST
    if confidence < 0.7:
        return {
            "disease": "Unknown plant / not in dataset",
            "confidence": confidence
        }

    # ✅ NORMAL RETURN
    return {
        "disease": class_names[class_index],
        "confidence": confidence
    }