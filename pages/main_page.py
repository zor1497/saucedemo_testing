from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    USERNAME_FIELD = ("id", "user-name")
    PASSWORD_FIELD = ("id", "password")
    LOGIN_BUTTON = ("id", "login-button")
    LOGIN_ERROR_NOTIFY = ("xpath", "//h3[@data-test='error']")

    @allure.step("Открытие главной страницы")
    def open(self):
        self.browser.get(self.base_url)

    def auth(self, login, password):
        with allure.step(f"Ввод в поле логина значения: {login if login != '' else 'пустое значение'}"):
            self.type_login(login)
        with allure.step(f"Ввод в поле пароля значения: {password if password != '' else 'пустое значение'}"):
            self.type_password(password)
        with allure.step(f"Нажатие на кнопку авторизации"):
            self.click_on_login_button()

    def type_login(self, login):
        username_field = self.find_element(self.USERNAME_FIELD)
        username_field.send_keys(login)

    def type_password(self, password):
        password_field = self.find_element(self.PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_on_login_button(self):
        login_button = self.find_element(self.LOGIN_BUTTON)
        login_button.click()

    @allure.step("Открытие страницы Inventory")
    def should_be_open_inventory_page(self):
        assert "inventory" in self.get_current_url(), "Страница Inventory не открылась"

    @allure.step("Отображение уведомления о незаполненном логине")
    def should_be_error_about_empty_login(self):
        login_error_notify = self.find_element(self.LOGIN_ERROR_NOTIFY)
        assert login_error_notify.text == "Epic sadface: Username is required",\
            "Уведомление о незаполненном логине не отображается"

    @allure.step("Отображение уведомления о незаполненном пароле")
    def should_be_error_about_empty_password(self):
        login_error_notify = self.find_element(self.LOGIN_ERROR_NOTIFY)
        assert login_error_notify.text == "Epic sadface: Password is required", \
            "Уведомление о незаполненном пароле не отображается"



