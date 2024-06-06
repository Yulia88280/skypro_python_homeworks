import pytest
import allure
from selenium import webdriver
from page_form import FormPage, ResultPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест заполнения и проверки формы")
@allure.description("Этот тест заполняет форму и проверяет цвета полей после отправки")
@allure.feature("Форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_fill_form_and_validate(browser):
    with allure.step("Открываем страницу формы"):
        form_page = FormPage(browser)
        form_page.open()

    with allure.step("Заполняем форму"):
        form_page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")

    with allure.step("Отправляем форму"):
        form_page.submit_form()

    with allure.step("Проверяем цвет фона ZIP-кода"):
        result_page = ResultPage(browser)
        zip_code_color = result_page.get_zip_code_color()
        assert zip_code_color == "rgba(248, 215, 218, 1)", f"Ожидаемый цвет: rgba(248, 215, 218, 1), но получили: {zip_code_color}"

    with allure.step("Проверяем цвета фона остальных полей"):
        other_fields_colors = result_page.get_other_fields_colors()
        for color in other_fields_colors:
            assert color == "rgba(209, 231, 221, 1)", f"Ожидаемый цвет: rgba(209, 231, 221, 1), но получили: {color}"
