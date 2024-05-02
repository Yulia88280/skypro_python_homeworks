from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открываем браузер Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Кликаем на кнопку "Add Element" пять раз
for _ in range(5):
    add_element_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    add_element_button.click()
    time.sleep(1)  # Пауза, чтобы увидеть добавленные кнопки

# Собираем список кнопок "Delete"
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

# Выводим на экран размер списка кнопок "Delete"
print("Размер списка кнопок 'Delete':", len(delete_buttons))

# Закрываем браузер
driver.quit()