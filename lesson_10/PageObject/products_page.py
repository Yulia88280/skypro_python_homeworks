from selenium.webdriver.common.by import By
from base_page import BasePage
from typing import List

class ProductsPage(BasePage):
    def add_items_to_cart(self, items: List[str]) -> None:
        """
        Добавляет указанные товары в корзину.

        :param items: List[str] - список названий товаров.
        :return: None
        """
        for item in items:
            add_to_cart_button = self.driver.find_element(By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button")
            add_to_cart_button.click()

    def open_cart(self) -> None:
        """
        Открывает корзину.

        :return: None
        """
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
