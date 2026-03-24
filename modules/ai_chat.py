import anthropic
import os

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
history = []

def chat(user_message):
    history.append({"role": "user", "content": user_message})
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system="You are RudraX, a powerful and intelligent AI assistant.",
        messages=history
    )
    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply
