import allure
from pages.base_page import BasePage


class CompletePage(BasePage):
    # LOCATORS
    BACK_HOME_BUTTON = ("id", "back-to-products")
    HEADER = ("xpath", "//h2[@data-test='complete-header']")

    # ACTIONS
    @allure.step("Переход на страницу 'Inventory'")
    def click_on_back_home_button(self):
        self.find_element(self.BACK_HOME_BUTTON).click()
        with allure.step('Проверка открытия страницы "Inventory"'):
            assert "inventory" in self.get_current_url()

    # SHOULD_BE
    @allure.step("Проверка отображения уведомления благодарности за заказ")
    def should_be_success_order_header(self):
        assert self.find_element(self.HEADER).text == "Thank you for your order!"