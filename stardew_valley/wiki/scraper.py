
import os
import requests

import stardew_valley.wiki.parser as wiki_parser


class Scraper:
    """A web scraper session"""
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.parser = wiki_parser.Parser()

    def scrape(self, url: str) -> wiki_parser.Parser:
        """Scrape a page"""
        page = self._get_page_html(url)
        self.parser.parse(page)
        return self.parser

    def _get_page_html(self, page_name: str, **kwargs) -> requests.Response:
        """Get the contents of a page"""
        return requests.get(self.as_url(page_name), **kwargs)

    def as_url(self, page_name: str) -> str:
        """Get the url of a page"""
        return os.path.join(self.base_url, page_name)



if __name__ == '__main__':
    scraper = Scraper()
    print(scraper.get_page('Robin').text)



