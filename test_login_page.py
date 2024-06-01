import allure
from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
@allure.title("Авторизация с незаполненным логином")
def test_auth_with_empty_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.clear_login_field()
    login_page.click_on_sign_in_button()
    login_page.should_be_message_error()

@pytest.mark.smoke
@allure.title("Авторизация с логином, состоящим из одних пробелов")
def test_auth_with_tabs_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.clear_login_field()
    login_page.type_text_into_login_field("   ")
    login_page.click_on_sign_in_button()
    login_page.should_be_message_error()


