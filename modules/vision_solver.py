import os
import base64
from pathlib import Path
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def solve_from_image(image_path, question="What do you see? Explain and solve if there's a problem."):
    image_data = Path(image_path).read_bytes()
    b64 = base64.standard_b64encode(image_data).decode("utf-8")
    ext = Path(image_path).suffix.lower()
    media_map = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}
    media_type = media_map.get(ext, "image/jpeg")

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{media_type};base64,{b64}"
                    }
                },
                {"type": "text", "text": question}
            ]
        }]
    )
    return response.choices[0].message.content
