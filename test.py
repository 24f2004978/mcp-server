import requests

url = "http://127.0.0.1:8000"

headers = {
    "X-Exam-Challenge": "0123456789abcdef0123456789abcdef"
}

data = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
        "name": "solve_challenge",
        "arguments": {}
    }
}

response = requests.post(url, headers=headers, json=data)

print(response.json())