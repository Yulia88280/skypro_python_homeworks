from selenium.webdriver.common.by import By
from base_page import BasePage

class ProductsPage(BasePage):
    def add_items_to_cart(self, items):
        for item in items:
            add_to_cart_button = self.driver.find_element(By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button")
            add_to_cart_button.click()

    def open_cart(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
