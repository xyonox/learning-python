import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

## simple search
rq = requests.get("https://oxylabs.io/")
soup = BeautifulSoup(rq.text, 'html.parser')


blog_titles = soup.find_all('section', class_='enwhltf0')
for title in blog_titles:
    print(title.text)

## Webbrowser/ webdriver
driver = webdriver.Firefox()

