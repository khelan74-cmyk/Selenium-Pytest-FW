from selenium.webdriver.common.by import By
from PageObjects.checkout_confirm import Checkout_Confirmation


#from PageObjects.checkout_confirm import Checkout_Confirmation


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.shop_product = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_product_to_cart(self,product_name):
        self.driver.find_element(*self.shop_product).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.checkout_btn).click()
        checkout_confirmation = Checkout_Confirmation(self.driver)
        #checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation

