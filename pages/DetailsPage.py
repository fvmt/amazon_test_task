import logging
from datetime import datetime

import allure
from selenium.webdriver.common.by import By
from webium import BasePage, Find
from .common.common import Driver


class DetailsPage(BasePage):

    def __init__(self, asin):
        super(DetailsPage, self).__init__(driver=Driver.get())
        self.list_asin = asin
        self.asin = Find(by=By.XPATH,
                         value="//li[b[contains(text(), 'ASIN:')]]",
                         context=self).text.split(':')[1].strip()
        self.string_date_first = Find(by=By.XPATH,
                                      value="//li[b[contains(text(), 'Date first available at Amazon.com.au:')]]",
                                      context=self).text.split(':')[1].strip()

        self.date_first = datetime.strptime(self.string_date_first, "%d %B %Y")
        self.body = Find(by=By.TAG_NAME, value="body", context=self)

    @allure.step
    def check_for_umlaut(self):
        text = self.body.text
        #logging.info(text)
        assert "Ö" not in text and "ö" not in text

    @allure.step
    def check_asin(self):
        logging.info('Details page ASIN: ' + self.asin + ' ASIN from the list: ' + self.list_asin)
        assert len(self.list_asin) == 10 and self.list_asin == self.asin

    @allure.step
    def check_correct_date(self):
        logging.info('Time difference between now and date_first_amazon: ' + str(datetime.now() - self.date_first))
        assert self.date_first < datetime.now()
