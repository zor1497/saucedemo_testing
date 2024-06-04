import allure
import pytest
from pages.basket_page import BasketPage
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
def test_auth_with_valid_login_and_password(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("locked_out_user", "secret_sauce")
    main_page.should_be_error_about_locked_user()

@pytest.mark.smoke
@allure.title("Добавление одного товара в корзину")
def test_add_one_item_into_basket(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    item = inventory_page.add_one_item_into_basket()
    inventory_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.should_be_item_in_basket(item)

@pytest.mark.smoke
@allure.title("Добавление всех товаров в корзину")
def test_add_all_items_into_basket(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    items_list = inventory_page.add_all_items_into_basket()
    inventory_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.should_be_all_items_in_basket(items_list)