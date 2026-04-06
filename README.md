# 🌾 FarmAI – AI-Powered Crop & Disease Prediction System

An intelligent agriculture assistant that helps farmers make better decisions using Machine Learning and Deep Learning.

---

## 🚀 Features

- 🌱 **Crop Recommendation** using Random Forest based on soil and environmental data  
- 🦠 **Plant Disease Detection** using CNN (Transfer Learning – MobileNetV2)  
- 🤖 **AI Farming Guide** for step-by-step crop practices  
- 🌦️ **Weather-based Suggestions** for improved decision-making  

---

## 🧠 Tech Stack

- **Backend:** FastAPI  
- **Machine Learning:** Scikit-learn (Random Forest)  
- **Deep Learning:** TensorFlow, CNN (Transfer Learning)  
- **AI Integration:** Groq API (LLM fallback)  
- **Others:** HTML, CSS, JavaScript  

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/shubham202003/AI-Powered-Farm-Assistant.git
cd AI-Powered-Farm-Assistant

---

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Create `.env` file
Create a `.env` file in the root directory and add:
```env
HF_TOKEN=your_key
OPEN_WEATHER_KEY=your_key
GROQ_API_KEY=your_key
```

### 4️⃣ Run the application
```bash
uvicorn app.main:app --reload
```

### 5️⃣ Open in browser
```
http://127.0.0.1:8000/ui
```