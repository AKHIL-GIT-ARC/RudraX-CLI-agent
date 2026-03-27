import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
history = []

def chat(user_message):
    history.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1024,
        messages=[
            {"role": "system", "content": "You are RudraX, a powerful and intelligent AI assistant."},
            *history
        ]
    )
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply