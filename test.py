import requests
print(requests.post("http://127.0.0.1:8000/mcp/calmme",
  json={"heart_rate":120, "message":"I feel very tense"}
).json())
