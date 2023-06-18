from selenium.webdriver.common.by import By
from pages.base_page_ import Page

class Header(Page):

    SEARCH_BTN = (By.ID, 'nav-orders')

    def click_orders(self):
        self.click(*self.SEARCH_BTN)