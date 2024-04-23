from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Функция для клика на кнопку с CSS-классом
def click_button_with_css_class():
    driver = webdriver.Firefox()

    # Открываем страницу
    driver.get("http://uitestingplayground.com/classattr/")
    
    # Ожидаем появления синей кнопки с нужным CSS-классом
    blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
    
    # Кликаем на синюю кнопку
    blue_button.click()
    
    # Закрываем браузер
    driver.quit()

# Запускаем скрипт три раза
for i in range(3):
    click_button_with_css_class()
    print(f"Скрипт {i+1} выполнен успешно.")
    time.sleep(3)  # Ждем 3 секунды между запусками скрипта