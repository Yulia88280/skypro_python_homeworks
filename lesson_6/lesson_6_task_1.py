from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открытие страницы
driver.get("http://uitestingplayground.com/ajax")


# Нажатие на синюю кнопку
blue_button = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.ID, "ajaxButton")))
blue_button.click()

# Дождаться появления текста в зеленой плашке
green_box_text = WebDriverWait(driver, 16).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))).text

# Вывод текста в консоль
print(green_box_text)


# Закрытие браузера
driver.quit()
