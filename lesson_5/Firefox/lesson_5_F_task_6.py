from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Ожидаем появления модального окна и кнопки Close
modal_close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "modal-footer")))

# Кликаем на кнопку Close
modal_close_button.find_element(By.TAG_NAME, "p").click()

# Закрываем браузер
driver.quit()