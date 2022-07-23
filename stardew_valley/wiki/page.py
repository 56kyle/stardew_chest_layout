
import requests

from bs4 import BeautifulSoup, element
from typing import List


class Page:
    """A page on the Stardew Valley wiki"""
    def __init__(self, page: requests.Response):
        self.response = page
        self.soup = BeautifulSoup(page.text, 'html.parser')
        self.name = None
        self.link = None
        self.table_of_contents = None
        self.categories = None

    def parse(self, page: requests.Response):
        """Parses for info on a page"""
        self.name = self.get_name()
        self.link = self.get_link()
        self.table_of_contents = self.get_table_of_contents()
        self.categories = self.get_categories()

    def get_name(self):
        """Returns the name of the page"""
        return self.soup.find('h1', {'id': 'firstHeading'}).text

    def get_link(self):
        """Returns the link to the page"""
        return self.response.url

    def get_table_of_contents(self):
        """Returns the table of contents"""
        return self.soup.find('div', {'id': 'toc'})

    def get_categories(self):
        """Returns all categories"""
        return self.soup.find('div', {'id': 'mw-normal-catlinks'})

    def get_category_links(self):
        """Returns all links that reference a category"""
        return self.get_internal_links(self.soup.find('div', {'id': 'mw-normal-catlinks'}))

    def get_internal_links(self, scope: element.PageElement = None):
        """Returns all links that stay in the same domain"""
        scope = scope if scope else self.soup
        all_links: List[str] = [tag.get('href') for tag in scope.find_all('a', href=True)]
        return [link for link in all_links if link.startswith('/') or 'stardewvalleywiki.com' in link]

    def is_internal(self, link: str):
        """Returns True if the link is internal to the wiki"""
        return link.startswith('/') or 'stardew' in link
