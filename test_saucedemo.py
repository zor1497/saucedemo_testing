import allure
import pytest
from pages.basket_page import BasketPage
from pages.checkout_page import CheckoutPage
from pages.complete_page import CompletePage
from pages.inventory_page import InventoryPage
from pages.item_page import ItemPage
from pages.main_page import MainPage
from pages.overview_page import OverviewPage


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
    item_page = ItemPage(browser)
    item = item_page.add_item_into_basket()
    item_page.open_basket()
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
    item_page = ItemPage(browser)
    item_page.add_item_into_basket()
    item_page.open_basket()
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
    item_page = ItemPage(browser)
    item_page.add_item_into_basket()
    item_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.click_on_checkout_button()
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_recipient_form("", "Ivanov", "155258")
    checkout_page.click_on_continue_button()
    checkout_page.should_be_empty_first_name_notify()

@pytest.mark.regress
@allure.title("Оформление заказа с незаполненной фамилией получателя")
def test_order_with_empty_last_name_recipient(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.open_item_page()
    item_page = ItemPage(browser)
    item_page.add_item_into_basket()
    item_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.click_on_checkout_button()
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_recipient_form("Ivan", "", "155258")
    checkout_page.click_on_continue_button()
    checkout_page.should_be_empty_last_name_notify()

@pytest.mark.regress
@allure.title("Оформление заказа с незаполненном индексе получателя")
def test_order_with_empty_last_name_recipient(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.open_item_page()
    item_page = ItemPage(browser)
    item_page.add_item_into_basket()
    item_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.click_on_checkout_button()
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_recipient_form("Ivan", "Ivanov", "")
    checkout_page.click_on_continue_button()
    checkout_page.should_be_empty_postcode_notify()


@pytest.mark.regress
@allure.title("Удаление товара из корзины со страницы товара")
def test_remove_item_from_basket_on_item_page(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.open_item_page()
    item_page = ItemPage(browser)
    item_page.add_item_into_basket()
    name_deleted_item = item_page.click_on_remove_item_button()
    item_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.should_be_not_item_in_basket(name_deleted_item)


@pytest.mark.regress
@allure.title("Удаление всех товаров из корзины со страницы 'Inventory'")
def test_remove_item_from_basket_on_inventory_page(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.add_all_items_into_basket()
    inventory_page.remove_all_items_from_basket()
    inventory_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.should_be_basket_empty()

@pytest.mark.smoke
@allure.title("Выход из системы")
def test_logout(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.open_sidebar()
    inventory_page.click_on_logout_link()


@pytest.mark.smoke
@allure.title("Стандартное оформление заказа")
def test_standard_order(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.open_item_page()
    item_page = ItemPage(browser)
    item_page.add_item_into_basket()
    item_page.open_basket()
    basket_page = BasketPage(browser)
    basket_page.click_on_checkout_button()
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_recipient_form("Ivan", "Ivanov", "12345")
    checkout_page.click_on_continue_button()
    overview_page = OverviewPage(browser)
    overview_page.click_on_finish_button()
    complete_page = CompletePage(browser)
    complete_page.should_be_success_order_header()


@pytest.mark.regress
@allure.title("Открытие страницы социальной сети Twitter")
def test_open_twitter(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.click_on_social_link("twitter")

@pytest.mark.regress
@allure.title("Открытие страницы социальной сети Facebook")
def test_open_facebook(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.click_on_social_link("facebook")

@pytest.mark.regress
@allure.title("Открытие страницы социальной сети Linkedin")
def test_open_linkedin(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.auth("standard_user", "secret_sauce")
    inventory_page = InventoryPage(browser)
    inventory_page.click_on_social_link("linkedin")
