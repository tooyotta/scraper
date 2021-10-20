# coding:utf-8

import requests
from bs4 import BeautifulSoup

# set target URL
target_url = "https://tcuprs.com"

# load target URL
html = requests.get(target_url)

# analysis target page
soup = BeautifulSoup(html.content, "html.parser")

# show all source
print(soup)