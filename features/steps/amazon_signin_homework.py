from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify sign in page opens')
def verify_signin_opens(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f"Test case failed"
    print("Test case passed")