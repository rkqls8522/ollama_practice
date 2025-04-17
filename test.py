import requests

res = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3.2:latest", "prompt": "대한민국의 수도는?", "stream": True},
    stream=True
)

for line in res.iter_lines():
    if line:
        data = line.decode('utf-8')
        print(data)
