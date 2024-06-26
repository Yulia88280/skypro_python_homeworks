import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    # Инициализация драйвера браузера (Chrome)
    driver = webdriver.Chrome()
    # Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    # Закрытие браузера после завершения теста
    driver.quit()

def test_fill_form_and_validate(browser):
    # Заполнение формы
    first_name = browser.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")

    last_name = browser.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")

    address = browser.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")

    email = browser.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")

    phone_number = browser.find_element(By.NAME, "phone")
    phone_number.send_keys("+7985899998787")

    city = browser.find_element(By.NAME, "city")
    city.send_keys("Москва")

    country = browser.find_element(By.NAME, "country")
    country.send_keys("Россия")

    job_position = browser.find_element(By.NAME, "job-position")
    job_position.send_keys("QA")

    company = browser.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Проверяем цвета всех полей
    zip_code_color = browser. find_element (By. CSS_SELECTOR, '#zip-code'). value_of_css_property('background-color')
    assert zip_code_color == 'rgba (248, 215, 218, 1)'
    
    other_fields = ['#first-name, #last-name, #address, #city, #country, #e-mail, #phone, #job-position, #company']
    for field in other_fields:
        field_color = browser. find_element (By.CSS_SELECTOR, field). value_of_css_property( 'background-color')
        assert field_color == 'rgba (209, 231, 221, 1)'