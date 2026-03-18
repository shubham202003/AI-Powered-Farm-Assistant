🌾 FarmAI – AI-Driven Crop Recommendation & Disease Detection System

Features
- Crop Recommendation using ML
- Disease Detection from images
- AI Farming Guide using LLM
- Weather-based suggestions

Tech Stack
- FastAPI
- Scikit-Learn
- Groq LLM
- Vision AI


⚙️ Setup:-

-->git clone https://github.com/shubham202003/AI-Powered-Farm-Assistant.git


-->pip install -r requirements.txt


-->Create .env file:


  GROQ_API_KEY=your_key
 
  HF_TOKEN=your_key

  OPEN_WEATHER_KEY=your_key


-->Run project:


  uvicorn app.main:app --reload