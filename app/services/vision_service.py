import base64
from groq import Groq
from app.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_crop_disease(image_bytes):

    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Identify the plant disease in this image and suggest treatment for farmers in simple language."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],
        temperature=0.2,
        max_tokens=500
    )

    return completion.choices[0].message.content