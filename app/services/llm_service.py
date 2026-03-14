from groq import Groq
from app.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_farming_guide(crop, district):

    prompt = f"""
You are an experienced Indian agriculture expert.

Create a simple farming guide for growing {crop} in {district}.

Explain step-by-step:
1. Land preparation
2. Seed selection
3. Sowing
4. Fertilizer plan
5. Irrigation
6. Pest control
7. Harvesting

Use simple language suitable for farmers.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content