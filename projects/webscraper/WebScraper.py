import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

## simple search
rq = requests.get("https://oxylabs.io/")
soup_rq = BeautifulSoup(rq.text, 'html.parser')


blog_titles = soup_rq.find_all('section', class_='enwhltf0')
for title in blog_titles:
    print(title.text)

## Webbrowser/ webdriver
driver = webdriver.Firefox()
driver.get("https://sandbox.oxylabs.io/products")
results = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for e in soup.findAll(attrs={"class": "product-card"}):
    name = e.find("h4")
    results.append(name.text)

print(results)


