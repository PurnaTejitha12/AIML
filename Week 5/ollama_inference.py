import requests


def ask_ollama(model, prompt):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": model,
        "prompt": prompt,
        "system": "You are a helpful AI mentor. Explain concepts clearly with examples.",
        "stream": False
    }

    response = requests.post(url, json=data)

    return response.json()["response"]


questions = [
    "Explain machine learning.",
    "What is overfitting?",
    "Explain Python decorators.",
    "What is an API?",
    "Explain neural networks."
]


for q in questions:
    print("\nQuestion:", q)

    answer = ask_ollama(
        "llama3.2:3b",
        q
    )

    print(answer)