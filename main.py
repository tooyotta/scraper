# coding:utf-8

import requests
from bs4 import BeautifulSoup

# scrape note.com

def scrape_note(url_note):

    # set target URL
    #target_url = "https://note.com/tooyotta/"

    # load target URL
    html = requests.get(url_note)

    # analysis target page
    soup = BeautifulSoup(html.content, "html.parser")
    found = soup.find(class_='o-timelineFooter__date')

    return found


url_note = "https://note.com/tooyotta/"
found_note = scrape_note(url_note)
print(found_note)