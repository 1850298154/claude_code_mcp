import urllib.request
import json

url = "http://127.0.0.1:9001/speak"
data = json.dumps({"text": "简单语音测试"}).encode('utf-8')

req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
response = urllib.request.urlopen(req)
print("状态码:", response.status)
print("响应:", response.read().decode('utf-8'))
