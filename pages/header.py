from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page_ import Page

class Header(Page):

    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-orders')
    DEPT_SELECTOR = (By.ID, 'searchDropdownBox')
    SEARCH_SUBMIT_BTN = (By.ID, 'nav-search-submit-button')

    def click_orders(self):
        self.click(*self.SEARCH_BTN)


    def select_dept(self):
        dept_select = self.find_element(*self.DEPT_SELECTOR)
        select = Select(dept_select)
        select.select_by_value('search-alias=electronics')


    def search_for_product(self):
        self.input_text('radio',*self.SEARCH_BOX)
        self.click(*self.SEARCH_SUBMIT_BTN)