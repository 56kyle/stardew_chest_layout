
import requests

from bs4 import BeautifulSoup, element
from dataclasses import dataclass, field
from typing import List


@dataclass
class Page:
    name: str
    text: str = field(repr=False)
    links: List[link.Link] = field(default_factory=list)
    categories: List[category.Category] = field(default_factory=list)
    images: List[image.Image] = field(default_factory=list)

    def parse(self, page: requests.Response):
        soup = BeautifulSoup(page.text, 'html.parser')
        self.text = soup.find('div', id='mw-content-text').text
        self.links = [a.attrs['href'] for a in soup.find_all('a', href=True)]
        self.categories = [a.attrs['href'] for a in soup.find_all('a', href=True) if a.attrs['href'].startswith('/wiki/Category:')]
        self.images = [a.attrs['href'] for a in soup.find_all('a', href=True) if a.attrs['href'].startswith('/wiki/File:')]

    def __repr__(self):
        return f'<Page {self.name}>'

    def __str__(self):
        return self.text

    def _get_categories(self) -> List[str]:
        pass


