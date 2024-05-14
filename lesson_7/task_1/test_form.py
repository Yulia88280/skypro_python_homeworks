import pytest
from selenium import webdriver
from page_form import FormPage, ResultPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form_and_validate(browser):
    form_page = FormPage(browser)
    form_page.open()
    form_page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
    form_page.submit_form()

    result_page = ResultPage(browser)
    zip_code_color = result_page.get_zip_code_color()
    assert zip_code_color == "rgba(248, 215, 218, 1)"

    other_fields_colors = result_page.get_other_fields_colors()
    for color in other_fields_colors:
        assert color == "rgba(209, 231, 221, 1)"