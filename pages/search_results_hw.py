from selenium.webdriver.common.by import By
from pages.base_page_ import Page

class SearchResults(Page):

    SIGN_IN_PAGE = (By.XPATH, "//h1[@class='a-spacing-small']")

    def verify_signin_opens(self):
        expected_result = "Sign in"
        actual_result = self.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
        assert expected_result == actual_result
