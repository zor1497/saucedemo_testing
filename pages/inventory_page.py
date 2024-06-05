import allure
from pages.base_page import BasePage


class InventoryPage(BasePage):

    # LOCATORS
    ITEM = ("xpath", "//div[@data-test='inventory-item']")
    ITEM_NAME = ("xpath", ".//div[@data-test='inventory-item-name']")
    ITEM_DESC = ("xpath", ".//div[@data-test='inventory-item-desc']")
    ITEM_PRICE = ("xpath", ".//div[@data-test='inventory-item-price']")
    ADD_ITEM_TO_BASKET_BUTTON = ("xpath", ".//button[@id[contains(.,'add')]]")
    REMOVE_ITEM_FROM_BASKET_BUTTON = ("xpath", ".//button[@id[contains(.,'remove')]]")

    # ACTIONS
    @allure.step("Добавление одного товара в корзину")
    def add_one_item_into_basket(self):
        item = {
            "name": self.find_element(self.ITEM).find_element(*self.ITEM_NAME).text,
            "desc": self.find_element(self.ITEM).find_element(*self.ITEM_DESC).text,
            "price": self.find_element(self.ITEM).find_element(*self.ITEM_PRICE).text
        }
        add_item_to_basket_button = self.find_element(self.ITEM).find_element(*self.ADD_ITEM_TO_BASKET_BUTTON)
        add_item_to_basket_button.click()
        assert "Remove" == self.find_element(self.ITEM).find_element(*self.REMOVE_ITEM_FROM_BASKET_BUTTON).text
        return item

    @allure.step("Добавление всех товаров в корзину")
    def add_all_items_into_basket(self):
        items = []
        for _item in self.browser.find_elements(*self.ITEM):
            item = {
                'name': _item.find_element(*self.ITEM_NAME).text,
                'desc': _item.find_element(*self.ITEM_DESC).text,
                'price': _item.find_element(*self.ITEM_PRICE).text
            }
            add_item_to_basket_button = _item.find_element(*self.ADD_ITEM_TO_BASKET_BUTTON)
            add_item_to_basket_button.click()
            assert "Remove" == self.find_element(self.ITEM).find_element(*self.REMOVE_ITEM_FROM_BASKET_BUTTON).text
            items.append(item)
        return items












