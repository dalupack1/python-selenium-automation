from selenium.webdriver.common.by import By
from pages.base_page_ import Page

class SearchResults(Page):

    SIGN_IN_PAGE = (By.XPATH, "//h1[@class='a-spacing-small']")
    ELECTRONICS_SUBMENU = (By.CSS_SELECTOR, "a[href*='/electronics-s']")

    def verify_signin_opens(self):
        expected_result = "Sign in"
        actual_result = self.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
        assert expected_result == actual_result


    def verify_dept(self):
        self.wait_for_element_appear(*self.ELECTRONICS_SUBMENU)