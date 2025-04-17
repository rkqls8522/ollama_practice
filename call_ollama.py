import ollama

response = ollama.generate(model="llama3.2:latest", prompt="대한민국의 수도는?")
print(response["response"])