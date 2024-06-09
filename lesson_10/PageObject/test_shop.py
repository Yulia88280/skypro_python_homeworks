import pytest
import allure
from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@pytest.fixture
def browser():
    """
    Фикстура для инициализации и закрытия браузера.

    :return: WebDriver - экземпляр веб-драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест покупок: Оформление заказа")
@allure.description("Этот тест проверяет процесс добавления товаров в корзину и оформления заказа.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping_checkout(browser):
    base_url = "https://www.saucedemo.com/"
    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    expected_total = "$58.29"

    with allure.step("Открываем сайт магазина"):
        browser.get(base_url)

    with allure.step("Логинимся"):
        login_page = LoginPage(browser)
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавляем товары в корзину"):
        products_page = ProductsPage(browser)
        products_page.add_items_to_cart(items_to_add)

    with allure.step("Переходим в корзину"):
        products_page.open_cart()

    with allure.step("Нажимаем Checkout"):
        cart_page = CartPage(browser)
        cart_page.checkout()

    with allure.step("Заполняем форму на странице Checkout"):
        checkout_page = CheckoutPage(browser)
        checkout_page.fill_form("Юлия", "Ильинова", "440036")

    with allure.step("Получаем итоговую сумму"):
        total_amount = checkout_page.get_total_amount()

    with allure.step("Проверяем итоговую сумму"):
        assert total_amount == expected_total, f"Ожидаемый итог: {expected_total}, Фактический итог: {total_amount}"
        print("Тест пройден: Итоговая сумма верна!")
