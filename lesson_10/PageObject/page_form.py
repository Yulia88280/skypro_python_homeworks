from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List

class FormPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация класса FormPage.

        :param driver: WebDriver - экземпляр веб-драйвера.
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self) -> None:
        """
        Открывает страницу формы.

        :return: None
        """
        self.driver.get(self.url)

    def fill_form(self, first_name: str, last_name: str, address: str, email: str, phone_number: str, city: str, country: str, job_position: str, company: str) -> None:
        """
        Заполняет форму данными.

        :param first_name: str - Имя.
        :param last_name: str - Фамилия.
        :param address: str - Адрес.
        :param email: str - Электронная почта.
        :param phone_number: str - Номер телефона.
        :param city: str - Город.
        :param country: str - Страна.
        :param job_position: str - Должность.
        :param company: str - Компания.
        :return: None
        """
        self.driver.find_element(By.NAME, "first-name").send_keys(first_name)
        self.driver.find_element(By.NAME, "last-name").send_keys(last_name)
        self.driver.find_element(By.NAME, "address").send_keys(address)
        self.driver.find_element(By.NAME, "e-mail").send_keys(email)
        self.driver.find_element(By.NAME, "phone").send_keys(phone_number)
        self.driver.find_element(By.NAME, "city").send_keys(city)
        self.driver.find_element(By.NAME, "country").send_keys(country)
        self.driver.find_element(By.NAME, "job-position").send_keys(job_position)
        self.driver.find_element(By.NAME, "company").send_keys(company)

    def submit_form(self) -> None:
        """
        Отправляет форму.

        :return: None
        """
        submit_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        self.driver.execute_script("arguments[0].click();", submit_button)

class ResultPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация класса ResultPage.

        :param driver: WebDriver - экземпляр веб-драйвера.
        """
        self.driver = driver

    def get_zip_code_color(self) -> str:
        """
        Получает цвет фона поля ZIP-кода.

        :return: str - цвет фона в формате RGBA.
        """
        return self.driver.find_element(By.ID, "zip-code").value_of_css_property("background-color")

    def get_other_fields_colors(self) -> List[str]:
        """
        Получает цвета фона остальных полей.

        :return: List[str] - список цветов фона в формате RGBA.
        """
        fields = ['#first-name', '#last-name', '#address', '#city', '#country', '#e-mail', '#phone', '#job-position', '#company']
        colors = []
        for field in fields:
            colors.append(self.driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color"))
        return colors
