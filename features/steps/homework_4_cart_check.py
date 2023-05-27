from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BEST_SELLERS_BTN = (By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
MOST_SOLD_ITEM = (By.CSS_SELECTOR, 'a[href*="/crocs-Unisex-Classic-Black-Women"]')
ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'input#add-to-cart-button')
ITEM_NAME = (By.CSS_SELECTOR, 'span#productTitle')
CHECK_CART_BTN = (By.CSS_SELECTOR, 'span#nav-cart-count')
ACTUAL_NAME = (By.CSS_SELECTOR, 'span[style*="height: 2.6"]' )


@given('Get amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Best Sellers tab')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS_BTN).click()


@when('Click on best selling item')
def click_most_sold_item(context):
    context.driver.find_element(*MOST_SOLD_ITEM).click()


@when('Store item name')
def store_item_name(context):
    context.item_name = context.driver.find_element(*ITEM_NAME).text
    print(context.item_name)


@when('Add item to cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Check cart')
def check_cart_contents(context):
    context.driver.find_element(*CHECK_CART_BTN).click()


@when('Store cart item name')
def cart_item_name(context):
    context.actual_name = context.driver.find_element(*ACTUAL_NAME).text
    print(context.actual_name)

@then('Verify correct item is in cart')
def verify_item_name(context):
    assert context.item_name[:4] in context.actual_name, f'Expected {context.item_name} but got'
