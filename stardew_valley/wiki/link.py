
import requests
import stardew_valley.wiki.url as url

from bs4 import BeautifulSoup, element
from dataclasses import dataclass, field


class Link:
    def __init__(self, element: element.Tag):
        self.element = element
        self.url = self._get_url(element)

    def __repr__(self):
        return f'<Link {self.url}>'

    def __str__(self):
        return self.url

    @staticmethod
    def _get_url(element: element.Tag) -> url.Url:
        return url.Url(element.attrs['href'])

