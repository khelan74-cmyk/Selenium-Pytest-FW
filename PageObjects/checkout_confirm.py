from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_Confirmation:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country = (By.ID, "country")
        #wait = WebDriverWait(driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.country_dropdown = (By.LINK_TEXT, "India")
        self.checkbox= (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "input[type='submit']")
        self.success_msg = (By.CLASS_NAME, "alert-success")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_address(self, country_name):
        #driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        self.driver.find_element(*self.country).send_keys(country_name)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_dropdown))
        self.driver.find_element(*self.country_dropdown).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        successText = self.driver.find_element(*self.success_msg).text
        assert "Success! Thank you!" in successText

