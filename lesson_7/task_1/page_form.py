from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, first_name, last_name, address, email, phone_number, city, country, job_position, company):
        self.driver.find_element(By.NAME, "first-name").send_keys(first_name)
        self.driver.find_element(By.NAME, "last-name").send_keys(last_name)
        self.driver.find_element(By.NAME, "address").send_keys(address)
        self.driver.find_element(By.NAME, "e-mail").send_keys(email)
        self.driver.find_element(By.NAME, "phone").send_keys(phone_number)
        self.driver.find_element(By.NAME, "city").send_keys(city)
        self.driver.find_element(By.NAME, "country").send_keys(country)
        self.driver.find_element(By.NAME, "job-position").send_keys(job_position)
        self.driver.find_element(By.NAME, "company").send_keys(company)

    def submit_form(self):
        submit_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        self.driver.execute_script("arguments[0].click();", submit_button)

class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    def get_zip_code_color(self):
        return self.driver.find_element(By.ID, "zip-code").value_of_css_property("background-color")

    def get_other_fields_colors(self):
        fields = ['#first-name', '#last-name', '#address', '#city', '#country', '#e-mail', '#phone', '#job-position', '#company']
        colors = []
        for field in fields:
            colors.append(self.driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color"))
        return colors
