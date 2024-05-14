import pytest
from selenium import webdriver
from page_calculator import CalculatorPage


@pytest.fixture
def browser():
    # Инициализация WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после завершения теста
    driver.quit()

def test_calculator(browser):
    calculator_page = CalculatorPage(browser)
    calculator_page.open()
    calculator_page.set_delay("45")
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")
    result = calculator_page.get_result()
    assert result == "15"