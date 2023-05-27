from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BEST_SELLERS_BTN = (By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
BEST_SELLERS_LINKS = (By.CSS_SELECTOR, 'div#zg_header div[class*="nav-tab-all_style_zg-tabs-li"]')
@given('Get amazon main page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')


@when('Click on Best Sellers')
def click_best_sellers(context):
    #context.driver.find_element(*BEST_SELLERS_BTN).click()


@then('Verify there are {link_amount} links')
def verify_best_seller_links(context,link_amount):
    link_amount = int(link_amount)
    link_count = len(context.driver.find_elements(*BEST_SELLERS_LINKS))
    assert link_count == link_amount, f'Expected {link_amount} links, but got {link_count}'

