import anthropic, os

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def solve(problem_text):
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"Solve this step by step:\n\n{problem_text}"
        }]
    )
    return response.content[0].text
