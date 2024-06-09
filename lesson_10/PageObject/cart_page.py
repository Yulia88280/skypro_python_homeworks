from selenium.webdriver.common.by import By
from base_page import BasePage

class CartPage(BasePage):
    def checkout(self) -> None:
        """
        Нажимает на кнопку "Checkout" для перехода к оформлению заказа.

        :return: None
        """
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
