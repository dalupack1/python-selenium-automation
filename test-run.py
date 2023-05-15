from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on cart')
def search_amazon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-icon.nav-sprite').click()

@then('Verify amazon cart is empty')
def verify_search_results(context):
    context.driver.find_element(By.CLASS_NAME, 'h2.a-spacing-top-base')
    expected_result = 'Your Amazon cart is empty'
    actual_result = context.driver.find_element(By.CLASS_NAME, 'h2.a-spacing-top-base')
    assert expected_result == actual_result, f"Test case failed"
