import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def solve(problem_text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"Solve this step by step:\n\n{problem_text}"
        }]
    )
    return response.choices[0].message.content