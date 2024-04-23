from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода и вводим текст "1000"
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.send_keys("1000")

# Очищаем поле ввода
input_field.clear()

# Снова вводим текст "999" в поле ввода
input_field.send_keys("999")

# Закрываем браузер
driver.quit()
