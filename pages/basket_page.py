import allure
from pages.base_page import BasePage


class BasketPage(BasePage):

    # LOCATORS

    ITEM = ("xpath", "//div[@data-test='inventory-item']")
    ITEM_NAME = ("xpath", ".//div[@data-test='inventory-item-name']")
    ITEM_DESC = ("xpath", ".//div[@data-test='inventory-item-desc']")
    ITEM_PRICE = ("xpath", ".//div[@data-test='inventory-item-price']")
    REMOVE_ITEM_FROM_BASKET_BUTTON = ("xpath", ".//button")
    CHECKOUT_BUTTON = ("id", "checkout")
    CONTINUE_SHOPPING_BUTTON = ("id", "continue-shopping")

    # ACTIONS
    @allure.step("Открытие страницы заполнения данных о получателе")
    def click_on_checkout_button(self):
        self.find_element(self.CHECKOUT_BUTTON).click()
        assert self.browser.current_url == "https://www.saucedemo.com/checkout-step-one.html"

    @allure.step("Нажатие на кнопку 'Continue Shopping'")
    def click_on_continue_shopping_button(self):
        self.find_element(self.CONTINUE_SHOPPING_BUTTON).click()
        with allure.step("Проверка открытия страницы 'Inventory'"):
            assert "inventory" in self.get_current_url()

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


    @allure.step("Проверка отсутствия конкретного товара в корзине")
    def should_be_not_item_in_basket(self, deleted_item_name):
        if len(self.find_elements(self.ITEM)) > 0:
            is_deleted_flag = True
            items = self.find_elements(self.ITEM_NAME)
            for item in items:
                item_name = item.text
                if deleted_item_name == item_name:
                    is_deleted_flag = False
                    break
            assert is_deleted_flag

    @allure.step("Проверка отсутствия товаров в корзине")
    def should_be_basket_empty(self):
        assert len(self.find_elements(self.ITEM_NAME)) == 0



