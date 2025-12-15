import json

import pytest
from selenium import webdriver

#chromedriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#from PageObjects.Shop import ShopPage
#from PageObjects.checkout_confirm import Checkout_Confirmation
from PageObjects.login import LoginPage

#from PageObjects.login import LoginPage
#from PageObjects.login import LoginPage
#import sys
#import os
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



test_data_path = '../Data/test_e2etest.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    driver.maximize_window()
    #driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)

    #loginPage = LoginPage(driver)
    #loginPage = LoginPage(driver)
    shop_Page = loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    #driver.implicitly_wait(4)

    # //a[contains(@href,'shop')] a[href*='shop']
    #shop_Page = ShopPage(driver)
    shop_Page.add_product_to_cart(test_list_item["productName"])
    checkout_confirmation = shop_Page.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_address("ind")
    checkout_confirmation.validate_order()

