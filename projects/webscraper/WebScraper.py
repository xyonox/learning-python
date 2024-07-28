import requests
from bs4 import BeautifulSoup

rq = requests.get("https://oxylabs.io/")
soup = BeautifulSoup(rq.text, 'html.parser')


blog_titles = soup.find_all('section', class_='enwhltf0')
for title in blog_titles:
    print(title.text)
