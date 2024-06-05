from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    # LOCATORS
    USERNAME_FIELD = ("id", "user-name")
    PASSWORD_FIELD = ("id", "password")
    LOGIN_BUTTON = ("id", "login-button")
    LOGIN_ERROR_NOTIFY = ("xpath", "//h3[@data-test='error']")

    # ACTIONS
    @allure.step("Открытие главной страницы")
    def open(self):
        self.browser.get(self.base_url)
        assert self.is_opened_page(self.base_url, self.get_current_url())

    @allure.step("Прохождение авторизации")
    def auth(self, login, password):
        self.type_login(login)
        self.type_password(password)
        self.click_on_login_button()

    @allure.step("Ввод значения в поле логина")
    def type_login(self, login):
        username_field = self.find_element(self.USERNAME_FIELD)
        username_field.send_keys(login)
        assert username_field.get_attribute("value") == login

    @allure.step("Ввод значения в поле пароля")
    def type_password(self, password):
        password_field = self.find_element(self.PASSWORD_FIELD)
        password_field.send_keys(password)
        assert password_field.get_attribute("value") == password

    @allure.step("Нажатие на кнопку авторизации")
    def click_on_login_button(self):
        self.find_element(self.LOGIN_BUTTON).click()

    # SHOULD BE

    @allure.step("Проверка открытия страницы Inventory")
    def should_be_open_inventory_page(self):
        assert "inventory" in self.get_current_url(), "Страница Inventory не открылась"

    @allure.step("Проверка отображения уведомления о незаполненном логине")
    def should_be_error_about_empty_login(self):
        login_error_notify = self.find_element(self.LOGIN_ERROR_NOTIFY)
        assert login_error_notify.text == "Epic sadface: Username is required",\
            "Уведомление о незаполненном логине не отображается"

    @allure.step("Проверка отображения уведомления о незаполненном пароле")
    def should_be_error_about_empty_password(self):
        login_error_notify = self.find_element(self.LOGIN_ERROR_NOTIFY)
        assert login_error_notify.text == "Epic sadface: Password is required", \
            "Уведомление о незаполненном пароле не отображается"

    @allure.step("Проверка отображения уведомления о заблокированном пользователе")
    def should_be_error_about_locked_user(self):
        login_error_notify = self.find_element(self.LOGIN_ERROR_NOTIFY)
        assert login_error_notify.text == "Epic sadface: Sorry, this user has been locked out.", \
            "Уведомление о заблокированном пользователе не отображается"




