from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from behave import given, when, then
from time import sleep

from pages.base_page_ import Page

@given('Open amazon product page')
def open_product_page(context):
    context.app.header.open_product_page()


@when('Hover over New Arrivals')
def new_arrivals_link(context):
    context.app.header.new_arrivals_link()


@then('Verify user sees new deal')
def new_deal_link(context):
    context.app.search_results_hw.new_deal_link
