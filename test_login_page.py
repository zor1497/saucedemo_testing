import allure
from pages.about_page import AboutPage
from pages.for_developers_page import ForDevelopersPage
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
    login_page.click_on_about_vk_link()
    about_page = AboutPage(browser)
    about_page.is_opened()

@pytest.mark.regress
@allure.title("Открытие страницы 'Для разработчиков' аккаунта со страницы авторизации")
def test_open_ford_developers_page_from_login_page(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.click_on_for_developers_link()
    for_developers_page = ForDevelopersPage(browser)
    for_developers_page.is_opened()




