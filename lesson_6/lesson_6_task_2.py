import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открытие страницы
driver.get("http://uitestingplayground.com/textinput")


# Указываем текст "SkyPro" в поле ввода
input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "newButtonName")))
input_field.send_keys("SkyPro")
logger.info("Текст 'SkyPro' введен в поле ввода")

# Нажатие на синюю кнопку
blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "updatingButton")))
blue_button.click()
logger.info("Нажата синяя кнопка")

# Получаем текст кнопки
button_text = blue_button.text
logger.info(f"Текст кнопки: {button_text}")


# Закрытие браузера
driver.quit()