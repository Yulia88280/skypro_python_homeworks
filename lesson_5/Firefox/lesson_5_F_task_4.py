from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Функция для клика на синюю кнопку
def click_blue_button():
    driver = webdriver.Firefox()

    # Открытие страницы
    driver.get("http://uitestingplayground.com/dynamicid/")
    
    # Появление синей кнопки
    blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-primary"]')))
    
    # Клик на синюю кнопку
    blue_button.click()
    
    # Закрытие браузера
    driver.quit()

# Запуск скрипта три раза
for i in range(3):
    click_blue_button()
    print(f"Скрипт {i+1} выполнен успешно.")
    time.sleep(3)  # Ждем 3 секунды между запусками скрипта