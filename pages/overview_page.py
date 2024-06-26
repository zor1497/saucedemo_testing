import allure

from pages.base_page import BasePage


class OverviewPage(BasePage):
    # LOCATORS
    FINISH_BUTTON = ("id", "finish")
    CANCEL_BUTTON = ("id", "cancel")

    # ACTIONS
    @allure.step("Переход на страницу 'Complete'")
    def click_on_finish_button(self):
        self.find_element(self.FINISH_BUTTON).click()

    @allure.step("Возврат на страницу 'Inventory'")
    def click_on_cancel_button(self):
        self.find_element(self.CANCEL_BUTTON).click()
        assert "inventory" in self.get_current_url()