from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, "a[href*='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=GLSBYFE9MGKKQXXM')


@when('Store original windows')
def store_orig_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original:', context.original_window)


@when('Click on Amazon Privacy Notice link')
def privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()


@when('Switch to the newly opened window')
def new_window_switch(context):
    context.all_windows = context.driver.window_handles
    context.driver.switch_to.window(context.all_windows[1])
    sleep(3)


@then('Verify Amazon Privacy Notice page is opened')
def privacy_notice_page_verification(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer'))


@then('User can close new window and switch back to original')
def close_new_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)