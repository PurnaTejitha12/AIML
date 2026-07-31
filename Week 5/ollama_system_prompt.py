import requests

url = "http://localhost:11434/api/generate"

system_prompt = (
    "You are an expert Python mentor. "
    "Answer clearly with examples."
)

user_prompt = input("Enter your question: ")

payload = {
    "model": "llama3.2:3b",
    "system": system_prompt,
    "prompt": user_prompt,
    "stream": False
}

response = requests.post(url, json=payload)

print("\nResponse:\n")
print(response.json()["response"])