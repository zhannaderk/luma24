from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    URL = "https://magento.softwaretestingboard.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def wait_for_products(self):
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//ol[contains(@class, 'product-items') and contains(@class, 'widget-product-grid')]")
        ))

    def get_products(self):
        return self.driver.find_elements(By.XPATH, "//li[@class='product-item']")

    def get_logo(self):
        return self.driver.find_element(By.XPATH, "//a[@class='logo']")

    def get_banner(self):
        return self.driver.find_element(By.XPATH, "//a[contains(@class, 'block-promo') and contains(@class, 'home-main')]")

    def wait_for_banner(self):
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@class, 'block-promo') and contains(@class, 'home-main')]")
        ))