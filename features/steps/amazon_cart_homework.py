
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on cart')
def click_link(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-count').click()

@then('Verify amazon cart is empty')
def verify_search_results(context):
    #context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-count').click()
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f" Error! Expected {expected_result} but got {actual_result}"
