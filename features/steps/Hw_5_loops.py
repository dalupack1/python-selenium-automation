from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PRODUCT_NAME = (By.CSS_SELECTOR, 'span#productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, 'li[title]')
CURRENT_COLOR = (By.CSS_SELECTOR, 'span.selection')


@given('Open amazon product page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')
    sleep(3)

@when('Store product name')
def click_on_product(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(context.product_name)


@then('Verify user can choose colors')
def click_through_colors(context):
    expected_colors = ['Black', 'Blue, Over Dye', 'Bright White']
    actual_colors = []


    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:3]:
        print(color)
        color.click()
        sleep(2)
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]
        print(actual_colors)


    assert expected_colors == actual_colors