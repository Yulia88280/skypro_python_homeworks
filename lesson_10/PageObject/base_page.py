from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация базового класса BasePage.

        :param driver: WebDriver - экземпляр веб-драйвера.
        """
        self.driver = driver
