import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    # Инициализация WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после завершения теста
    driver.quit()

def test_calculator(browser):
    # Открыть страницу
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Найти поле ввода и ввести значение 45
    delay_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажать на кнопку 7
    button_7 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='7']")))
    button_7.click()

    # Нажать на кнопку "+"
    button_plus = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='+']")))
    button_plus.click()

    # Нажать на кнопку 8
    button_8 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='8']")))
    button_8.click()

    # Нажать на кнопку "="
    button_equals = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='=']")))
    button_equals.click()

    # Подождать 45 секунд и проверить результат
    time.sleep(45)
    result = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))).text
    assert result == "15"