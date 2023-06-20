from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from behave import given, when, then
from time import sleep

from pages.base_page_ import Page



@given('Open amazon main page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Select department')
def select_dept(context):
    context.app.header.select_dept()


@when('Search for radio')
def search_for_product(context):
    context.app.header.search_for_product()


@then('Verify that correct department is shown')
def verify_dept(context):
    context.app.search_results_hw.verify_dept()
