
import os
import requests


class Scraper:
    """A web scraper for the Stardew Valley Wiki"""
    def __init__(self):
        self.base_url = 'https://stardewvalleywiki.com/'

    def get_page(self, page_name, **kwargs) -> requests.Response:
        """Get the contents of a page"""
        url = os.path.join(self.base_url, page_name)
        return requests.get(url, **kwargs)


if __name__ == '__main__':
    scraper = Scraper()
    print(scraper.get_page('Robin').text)



