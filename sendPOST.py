import requests
import json

url = 'http://localhost:5000/webhook'
header = {
    'Content-Type': 'application/json'
}

data = {'msg': 'testing sending post jaaaaaaaaa'}

data = json.dumps(data)

req = requests.post(url, headers=header, data=data)

print(req.text)