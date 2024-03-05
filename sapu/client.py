import requests

res = requests.get(
    "http://127.0.0.1:8000/sample/",
    headers={"Authorization": "Bearer A1B2C3D4"},
)

print(res.status_code)
print(res.text)
print(res.headers)