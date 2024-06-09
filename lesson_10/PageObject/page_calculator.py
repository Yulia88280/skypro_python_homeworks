from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException  # Импортируем TimeoutException
import time

class CalculatorPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация класса CalculatorPage.

        :param driver: WebDriver - экземпляр веб-драйвера.
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        # Добавим небольшую задержку для загрузки страницы
        time.sleep(2)

    def set_delay(self, value: str) -> None:
        """
        Устанавливает задержку калькулятора.

        :param value: str - значение задержки.
        :return: None
        """
        delay_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, button_text: str) -> None:
        """
        Нажимает кнопку на калькуляторе.

        :param button_text: str - текст на кнопке.
        :return: None
        """
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{button_text}']")))
        button.click()

    def wait_for_spinner(self) -> None:
        """
        Ожидает появления и исчезновения спиннера.

        :return: None
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "spinner")))
            WebDriverWait(self.driver, 45).until(EC.invisibility_of_element_located((By.ID, "spinner")))
        except TimeoutException:
            print("Спиннер не исчез в течение указанного времени ожидания.")

    def get_result(self) -> str:
        """
        Получает результат вычисления.

        :return: str - результат, отображаемый на экране калькулятора.
        """
        result_element = WebDriverWait(self.driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
        return result_element.text
