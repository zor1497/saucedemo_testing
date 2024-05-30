import allure
from pages.about_page import AboutPage
from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
@allure.title("Открытие страницы авторизации")
def test_open_login_page(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.is_opened()


@pytest.mark.regress
@allure.title("Открытие страницы 'О Вконтакте' со страницы авторизации")
def test_open_about_page_from_login_page(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.open_about_page_from_login_page()
    about_page = AboutPage(browser)
    about_page.is_opened()