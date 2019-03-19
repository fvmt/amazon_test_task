from selenium.webdriver.common.by import By
from webium import BasePage, Find
from .common.common import Driver
from .ProductList import ProductList
class HomePage(BasePage):
    categories_link = Find(by=By.CSS_SELECTOR, value="div#desktop-top  a[aria-label='Browse categories - See more']")
    pet_supplies_link = Find(by=By.XPATH, value="//a[contains(text(), 'All Pet Supplies')]")
    cats_link = Find(by=By.XPATH, value="//span/a[span='Cats']")
    clothing_link = Find(by=By.XPATH, value="//span/a[span='Clothing']")

    def navigate_to_product_list(self):
        self.open()
        self.categories_link.click()
        self.pet_supplies_link.click()
        self.cats_link.click()
        self.clothing_link.click()
        return ProductList()


    def __init__(self):
        super(HomePage, self).__init__(Driver.get(), url='https://amazon.com.au')