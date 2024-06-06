import pytest
import allure
from selenium import webdriver
from page_calculator import CalculatorPage

@pytest.fixture
def browser():
    """
    Фикстура для инициализации и закрытия браузера.

    :return: WebDriver - экземпляр веб-драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест калькулятора: сложение чисел")
@allure.description("Этот тест проверяет функцию сложения калькулятора с установленной задержкой.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(browser):
    with allure.step("Открываем страницу калькулятора"):
        calculator_page = CalculatorPage(browser)
        calculator_page.open()
    
    with allure.step("Устанавливаем задержку в 45 секунд"):
        calculator_page.set_delay("45")
    
    with allure.step("Нажимаем на кнопку '7'"):
        calculator_page.click_button("7")
    
    with allure.step("Нажимаем на кнопку '+'"):
        calculator_page.click_button("+")
    
    with allure.step("Нажимаем на кнопку '8'"):
        calculator_page.click_button("8")
    
    with allure.step("Нажимаем на кнопку '='"):
        calculator_page.click_button("=")
    
    with allure.step("Проверяем результат"):
        result = calculator_page.get_result()
        assert result == "15", f"Ожидаемый результат: 15, но получили: {result}"
