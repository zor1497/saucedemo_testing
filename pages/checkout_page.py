import allure
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # LOCATORS
    FIRST_NAME_FIELD = ("id", "first-name")
    LAST_NAME_FIELD = ("id", "last-name")
    POSTAL_FIELD = ("id", "postal-code")
    CANCEL_BUTTON = ("id", "cancel")
    CONTINUE_BUTTON = ("id", "continue")
    ERROR_NOTIFY = ("xpath", "//h3[@data-test='error']")

    # ACTIONS

    @allure.step("Заполнение данных о получателе")
    def fill_recipient_form(self, first_name, last_name, postal_code):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_postal_code(postal_code)

    @allure.step("Заполнение имени")
    def fill_first_name(self, first_name):
        first_name_field = self.find_element(self.FIRST_NAME_FIELD)
        first_name_field.send_keys(first_name)
        assert first_name_field.get_attribute("value") == first_name

    @allure.step("Заполнение фамилии")
    def fill_last_name(self, last_name):
        last_name_field = self.find_element(self.LAST_NAME_FIELD)
        last_name_field.send_keys(last_name)
        assert last_name_field.get_attribute("value") == last_name

    @allure.step("Заполнение почтового индекса")
    def fill_postal_code(self, postal_code):
        postal_field = self.find_element(self.POSTAL_FIELD)
        postal_field.send_keys(postal_code)
        assert postal_field.get_attribute("value") == postal_code

    @allure.step("Переход на страницу подтверждения заказа")
    def click_on_continue_button(self):
        self.find_element(self.CONTINUE_BUTTON).click()

    # SHOULD BE
    @allure.step("Проверка отображения уведомления о незаполненном имени получателя")
    def should_be_empty_first_name_notify(self):
        error_notify = self.find_element(self.ERROR_NOTIFY).text
        assert error_notify == "Error: First Name is required"

    @allure.step("Проверка отображения уведомления о незаполненной фамилии получателя")
    def should_be_empty_last_name_notify(self):
        error_notify = self.find_element(self.ERROR_NOTIFY).text
        assert error_notify == "Error: Last Name is required"

    @allure.step("Проверка отображения уведомления о незаполненном индексе получателя")
    def should_be_empty_postcode_notify(self):
        error_notify = self.find_element(self.ERROR_NOTIFY).text
        assert error_notify == "Error: Postal Code is required"


