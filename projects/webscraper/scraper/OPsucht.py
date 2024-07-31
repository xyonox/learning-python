import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import re

def remove_paragraphs(text):
    text_no_paragraphs = re.sub(r'\s+', ' ', text)
    text_no_paragraphs = text_no_paragraphs.strip()
    return text_no_paragraphs


## Webbrowser/ webdriver
driver = webdriver.Firefox()
driver.get("https://shop.opsucht.net/category/raenge")
results = []
prices = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for e in soup.findAll(attrs={"class": "rank-wrap"}):
    name = e.find(attrs={"class": "rank-name"})
    price = e.find(attrs={"class": "rank-price"})
    for span in price.find_all("span"):
        span.decompose()
    print(name)
    results.append(name.text)
    prices.append(remove_paragraphs(price.text).replace(" ", ""))

print(results)

# saving ^^
df = pd.DataFrame({'Names': results, 'Prices': prices})
df.to_csv('opsucht.csv', index=False, encoding='utf-8')


