import pytest
from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage

# Функция фикстуры для запуска браузера
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Тест
def test_shopping_checkout(browser):
    base_url = "https://www.saucedemo.com/"
    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    expected_total = "$58.29"

    # Открываем сайт магазина
    browser.get(base_url)

    # Логинимся
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    # Добавляем товары в корзину
    products_page = ProductsPage(browser)
    products_page.add_items_to_cart(items_to_add)

    # Переходим в корзину
    products_page.open_cart()

    # Нажимаем Checkout
    cart_page = CartPage(browser)
    cart_page.checkout()

    # Заполняем форму на странице Checkout
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_form("Юлия", "Ильинова", "440036")

    # Получаем итоговую сумму
    total_amount = checkout_page.get_total_amount()

    # Проверяем, что итоговая сумма равна ожидаемой
    assert total_amount == expected_total, f"Ожидаемый итог: {expected_total}, Фактический итог: {total_amount}"
    print("Тест пройден: Итоговая сумма верна!")
