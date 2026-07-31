import ollama

context = """
Artificial Intelligence (AI) is a branch of computer science that focuses on creating systems capable of performing tasks that normally require human intelligence.

Machine Learning is a subset of AI that enables computers to learn from data without being explicitly programmed.

ChromaDB is an open-source vector database used to store embeddings and perform semantic search.
"""

question = "What is ChromaDB?"

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}"
        }
    ]
)

print(response["message"]["content"])