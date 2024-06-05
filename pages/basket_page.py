import allure
from pages.base_page import BasePage


class BasketPage(BasePage):

    # LOCATORS

    ITEM = ("xpath", "//div[@data-test='inventory-item']")
    ITEM_NAME = ("xpath", ".//div[@data-test='inventory-item-name']")
    ITEM_DESC = ("xpath", ".//div[@data-test='inventory-item-desc']")
    ITEM_PRICE = ("xpath", ".//div[@data-test='inventory-item-price']")
    REMOVE_ITEM_FROM_BASKET_BUTTON = ("xpath", ".//button")


    # SHOULD BE

    @allure.step("Проверка присутствия добавленного товара в корзине")
    def should_be_item_in_basket(self, inv_item):
        bask_item = {
            "name": self.find_element(self.ITEM).find_element(*self.ITEM_NAME).text,
            "desc": self.find_element(self.ITEM).find_element(*self.ITEM_DESC).text,
            "price": self.find_element(self.ITEM).find_element(*self.ITEM_PRICE).text
        }
        assert inv_item["name"] == bask_item["name"], "Название товара не совпадает"
        assert inv_item["desc"] == bask_item["desc"], "Описание товара не совпадает"
        assert inv_item["price"] == bask_item["price"], "Цена товара не совпадает"

    @allure.step("Проверка присутствия всех добавленных товаров в корзине")
    def should_be_all_items_in_basket(self, inv_items):
        bask_items = []
        for _item in self.browser.find_elements(*self.ITEM):
            item = {
                'name': _item.find_element(*self.ITEM_NAME).text,
                'desc': _item.find_element(*self.ITEM_DESC).text,
                'price': _item.find_element(*self.ITEM_PRICE).text
            }
            bask_items.append(item)
        assert len(bask_items) == len(inv_items), "Количество товаров в корзине не соотв. количеству добавленных товаров"
        for inv_item in inv_items:
            assert any(inv_item['name'] == bask_item['name'] and
                       inv_item['desc'] == bask_item['desc'] and
                       inv_item['price'] == bask_item['price']
                       for bask_item in bask_items)