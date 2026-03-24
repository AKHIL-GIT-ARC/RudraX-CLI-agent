import anthropic, base64, os
from pathlib import Path

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def solve_from_image(image_path, question="What do you see? Explain and solve if there's a problem."):
    image_data = Path(image_path).read_bytes()
    b64 = base64.standard_b64encode(image_data).decode("utf-8")
    ext = Path(image_path).suffix.lower()
    media_map = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}
    media_type = media_map.get(ext, "image/jpeg")

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": b64}},
                {"type": "text", "text": question}
            ]
        }]
    )
    return response.content[0].text
