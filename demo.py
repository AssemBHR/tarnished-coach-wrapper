# Simple example to show how a local Ollama chat wrapper could work.
# This is NOT the commercial Tarnished Coach logic.

import requests

def ask(query):
    payload = {
        "model": "llama3.1",
        "messages": [{"role": "user", "content": query}]
    }
    r = requests.post("http://localhost:11434/api/chat", json=payload)
    return r.json().get("message", {}).get("content", "")

if __name__ == "__main__":
    print("Demo only. Not the real Tarnished Coach.")
    print("Asking model: 'Explain status effects in Elden Ring'")
    print(ask("Explain status effects in Elden Ring."))
