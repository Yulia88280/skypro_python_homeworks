from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, value):
        delay_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, button_text):
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{button_text}']")))
        button.click()

    def get_result(self):
        result_element = WebDriverWait(self.driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
        return result_element.text