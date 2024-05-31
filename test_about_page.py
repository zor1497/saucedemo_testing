import allure
from pages.about_page import AboutPage
from pages.login_page import LoginPage
import pytest


@pytest.mark.smoke
@allure.title("Открытие страницы авторизации со страницы 'О Вконтакте'")
def test_open_login_page_from_about_page(browser):
    about_page = AboutPage(browser)
    about_page.open()
    about_page.click_on_register_link()
    login_page = LoginPage(browser)
    login_page.is_opened()