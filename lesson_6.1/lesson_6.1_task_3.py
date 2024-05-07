import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открытие сайта магазина
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Авторизация
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()

# Добавление товаров в корзину
items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
for item in items_to_add:
    add_to_cart_button = driver.find_element(By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button")
    add_to_cart_button.click()

# Переход в корзину
cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()

# Нажатие на Checkout
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

# Заполнение формы данными
first_name_input = driver.find_element(By.ID, "first-name")
last_name_input = driver.find_element(By.ID, "last-name")
postal_code_input = driver.find_element(By.ID, "postal-code")
continue_button = driver.find_element(By.ID, "continue")

first_name_input.send_keys("Юлия")
last_name_input.send_keys("Ильинова")
postal_code_input.send_keys("440036")
continue_button.click()

# Получение итоговой стоимости
total_amount = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
total_amount_text = total_amount.text

# Удаление "Total: " из текста итоговой суммы
total_amount_value = total_amount_text.replace("Total: ", "")

# Закрытие браузера
driver.quit()

# Проверка итоговой суммы
expected_total = "$58.29"
assert total_amount_value == expected_total, f"Ожидаемый итог: {expected_total}, Фактический итог: {total_amount_value}"
print("Тест пройден: Итоговая сумма верна!")