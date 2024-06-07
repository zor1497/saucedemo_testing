import allure
import pytest
from pages.basket_page import BasketPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.main_page import MainPage


@pytest.mark.smoke
@allure.title("Авторизация с корректными логином и паролем")
def test_auth_with_valid_login_and_password(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    main_page.should_be_open_inventory_page()

@pytest.mark.regress
@allure.title("Авторизация с незаполненным логином и паролем")
def test_auth_with_empty_login_and_password(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("", "")
    main_page.should_be_error_about_empty_login()

@pytest.mark.smoke
@allure.title("Авторизация с заполненным логином, но незаполненным паролем")
def test_auth_with_valid_login_and_empty_password(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("123", "")
    main_page.should_be_error_about_empty_password()

@pytest.mark.regress
@allure.title("Авторизация под пользователем с заблокированной учетной записью")
def test_auth_with_locked_account(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("locked_out_user", "secret_sauce")
    main_page.should_be_error_about_locked_user()

@pytest.mark.smoke
@allure.title("Добавление товара в корзину со страницы товара")
def test_add_one_item_into_basket(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.open_item_page()
    item = inventory_page.add_item_into_basket()
    inventory_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.should_be_item_in_basket(item)

@pytest.mark.smoke
@allure.title("Добавление товаров в корзину со страницы Inventory")
def test_add_all_items_into_basket(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    items_list = inventory_page.add_all_items_into_basket()
    inventory_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.should_be_all_items_in_basket(items_list)

@pytest.mark.regress
@allure.title("Сортировка товаров по возрастанию цены")
def test_sort_items_low_high_price(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.sort_items("lohi")
    inventory_page.should_be_items_sort_low_high_price()

@pytest.mark.regress
@allure.title("Сортировка товаров по убыванию цены")
def test_sort_items_high_low_price(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.sort_items("hilo")
    inventory_page.should_be_items_sort_high_low_price()

@allure.title("Сортировка товаров по возрастанию названия")
def test_sort_items_a_z(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.sort_items("az")
    inventory_page.should_be_items_sort_a_z()

@pytest.mark.regress
@allure.title("Сортировка товаров по убыванию названия")
def test_sort_items_z_a(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.sort_items("za")
    inventory_page.should_be_items_sort_z_a()


@pytest.mark.regress
@allure.title("Оформление заказа с незаполненным именем, фамилией, индекса получателя")
def test_order_with_empty_recipient_form(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.open_item_page()
    inventory_page.add_item_into_basket()
    inventory_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.click_on_checkout_button()
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_recipient_form("", "", "")
    checkout_page.click_on_continue_button()
    checkout_page.should_be_empty_first_name_notify()


@pytest.mark.regress
@allure.title("Оформление заказа с незаполненным именем получателя")
def test_order_with_empty_first_name_recipient(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.open_item_page()
    inventory_page.add_item_into_basket()
    inventory_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.click_on_checkout_button()
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_recipient_form("", "Ivanov", "155258")
    checkout_page.click_on_continue_button()
    checkout_page.should_be_empty_first_name_notify()
