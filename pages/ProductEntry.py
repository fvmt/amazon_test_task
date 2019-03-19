import logging
from urllib.parse import urlparse, unquote

import allure
from selenium.webdriver.common.by import By
from webium import Find

from pages.DetailsPage import DetailsPage


class ProductEntry:
    def __init__(self, product_entry):
        self.a_link = Find(by=By.CSS_SELECTOR,
                           value="a.s-access-detail-page",
                           context=product_entry)
        self.name = Find(by=By.CSS_SELECTOR,
                         value="h2.s-access-title",
                         context=product_entry).get_attribute('data-attribute')
        self.dash_name = '-'.join(self.name.split(' '))
        self.url = self.a_link.get_attribute('href')

    def get_asin(self):
        return urlparse(self.url).path.split('/')[3]

    def get_unquoted_product_part(self):
        return unquote(urlparse(self.url).path.split('/')[1])

    @allure.step
    def check_url(self):
        logging.info(self.dash_name + '\n' + self.get_unquoted_product_part())
        return self.dash_name.startswith(self.get_unquoted_product_part())

    @allure.step
    def check_asin(self):
        asin = self.get_asin()
        logging.info(asin + ' ' + self.url)
        return len(asin) == 10 and set(asin).issubset(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))

    @allure.step
    def open_details_page(self):
        self.a_link.click()
        return DetailsPage(self.get_asin())
