from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open amazon main page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Click orders')
def click_orders(context):
    context.app.header.click_orders()


@then('Verify sign in page opens')
def verify_signin_opens(context):
    context.app.search_results_hw.verify_signin_opens()

