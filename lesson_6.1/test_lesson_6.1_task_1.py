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

    # Проверка подсветки полей
    zip_code_field = browser.find_element(By.NAME, "zip-code")
    assert "is-invalid" in zip_code_field.get_attribute("class"), "Zip code field should be highlighted red"
    
    highlighted_fields = browser.find_elements(By.CSS_SELECTOR, ".is-valid")
    assert len(highlighted_fields) == 8, "All fields except Zip code should be highlighted green"