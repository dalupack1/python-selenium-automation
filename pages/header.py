from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page_ import Page

class Header(Page):

    NEW_ARRIVALS_TAB = (By.CSS_SELECTOR, "a[href*='/New']")
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


    def open_product_page(self):
        self.open_url('https://www.amazon.com/gp/product/B074TBCSC8')


    def new_arrivals_link(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS_TAB)

        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()