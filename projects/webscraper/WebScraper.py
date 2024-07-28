import requests

rq = requests.get("https://oxylabs.io/")
print(rq.text)