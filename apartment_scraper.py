# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from google_sheets import GoogleSheets
from slack import Slack


class ApartmentScraper:

    # URL to scrape
    URL = (
        'https://www.equityapartments.com/boston/kendall-square/'
        'third-square-apartments'
    )

    def __init__(self):
        self.sheets = GoogleSheets()
        self.slack = Slack()

    def _get_min_price(self):
        raw_html = requests.get(self.URL).text
        soup = BeautifulSoup(raw_html, 'html.parser')

        # find price section and relevant text
        availability_soup = soup.find('div', {'class': 'hero-availability'})
        availability_links = availability_soup.find_all('a')

        min_price = 0

        # loop through elements that may include prices
        for item in availability_links:
            item_string = item.text

            if '$' not in item_string:
                continue

            # remove non numeric chars
            item_price = re.sub('[^0-9]', '', item_string)

            # if not a valid number
            if not item_price:
                continue

            if not min_price or int(item_price) < min_price:
                min_price = int(item_price)

        return min_price

    def get_min_price(self):
        return self._get_min_price()

    def run(self):
        min_price = self._get_min_price()
        if not min_price:
            return

        self.sheets.append_todays_data(min_price)
        self.slack.send_todays_notification(min_price)


if __name__ == '__main__':
    print(ApartmentScraper().get_min_price())
