from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Chrome
driver = webdriver.Chrome()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/login")

# Находим поле ввода для имени пользователя и вводим значение "tomsmith"
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Находим поле ввода для пароля и вводим значение "SuperSecretPassword!"
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Находим кнопку "Login" и кликаем на неё
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Закрываем браузер
driver.quit()