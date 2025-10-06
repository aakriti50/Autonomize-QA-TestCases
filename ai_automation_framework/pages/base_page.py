from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable((By.ID, locator))).click()

    def enter_text(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located((By.ID, locator)))
        elem.clear()
        elem.send_keys(text)
