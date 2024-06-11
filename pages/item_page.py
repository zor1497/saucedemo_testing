from pages.base_page import BasePage
import allure


class ItemPage(BasePage):
    ITEM = ("xpath", "//div[@data-test='inventory-item']")
    ITEM_NAME = ("xpath", ".//div[@data-test='inventory-item-name']")
    ITEM_DESC = ("xpath", ".//div[@data-test='inventory-item-desc']")
    ITEM_PRICE = ("xpath", ".//div[@data-test='inventory-item-price']")
    ADD_ITEM_TO_BASKET_BUTTON = ("xpath", ".//button[@id[contains(.,'add')]]")
    REMOVE_ITEM_FROM_BASKET_BUTTON = ("xpath", ".//button[@id[contains(.,'remove')]]")

    # ACTIONS
    @allure.step("Добавление товара в корзину")
    def add_item_into_basket(self):
        item = {
            "name": self.find_element(self.ITEM).find_element(*self.ITEM_NAME).text,
            "desc": self.find_element(self.ITEM).find_element(*self.ITEM_DESC).text,
            "price": self.find_element(self.ITEM).find_element(*self.ITEM_PRICE).text
        }
        add_item_to_basket_button = self.find_element(self.ITEM).find_element(*self.ADD_ITEM_TO_BASKET_BUTTON)
        add_item_to_basket_button.click()
        assert "Remove" == self.find_element(self.ITEM).find_element(*self.REMOVE_ITEM_FROM_BASKET_BUTTON).text
        return item

    @allure.step("Удаление товара из корзины")
    def click_on_remove_item_button(self):
        name_deleted_item = self.find_element(self.ITEM_NAME).text
        self.find_element(self.REMOVE_ITEM_FROM_BASKET_BUTTON).click()
        assert self.is_present_element(self.REMOVE_ITEM_FROM_BASKET_BUTTON) == False
        return name_deleted_item
