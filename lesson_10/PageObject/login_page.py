from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему.

        :param username: str - Имя пользователя.
        :param password: str - Пароль.
        :return: None
        """
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
