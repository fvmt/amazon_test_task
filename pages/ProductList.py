import logging

from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds

from pages.ProductEntry import ProductEntry
from .common.common import Driver


class ProductList(BasePage):

    def __init__(self):
        super(ProductList, self).__init__(driver=Driver.get())
        self.element_main_results = None
        self.elements_product_entries = None
        self.list_product_entries = None

    def update_product_list(self):
        self.element_main_results = Find(by=By.CSS_SELECTOR, value="ul.s-result-list", context=self)
        self.elements_product_entries = Finds(by=By.CSS_SELECTOR, value="li.s-result-item.celwidget",
                                              context=self.element_main_results)
        self.list_product_entries = []
        for product_entry in self.elements_product_entries:
            self.list_product_entries.append(ProductEntry(product_entry))

    def open_page_number(self, number):     #TODO make smart pagination navigation that doesn't depend on current state
        current_page = Find(by=By.CSS_SELECTOR, value="span.pagnCur", context=self)
        logging.info(' '.join([current_page.text, str(number)]))
        if current_page.text == str(number):
            pass
        else:
            xpath_page_link = '//span[contains(@class, "pagnLink")]/a[contains(text(), "%d")]' % number
            logging.info(xpath_page_link)
            page_link = Find(by=By.XPATH, value=xpath_page_link, context=self)
            page_link.click()
        self.update_product_list()

    def list_products(self):
        return self.list_product_entries
