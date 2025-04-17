from ollama import Client

client = Client()
response = client.chat(
    model='llama3.2:latest',
    messages=[{'role': 'user', 'content': '한글도 돼?'}]
)
print(response['message']['content'])
