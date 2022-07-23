
import stardew_valley.wiki.page as wiki_page
import requests

from bs4 import BeautifulSoup, element
from typing import List, Dict


class Parser:
    def __init__(self):
        self.pages: Dict = {}

    def parse(self, page: requests.Response):
        self.pages[page.url] = wiki_page.Page(page)
        self.pages[page.url].parse(page)
        return self.pages[page.url]










