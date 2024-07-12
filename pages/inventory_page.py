import allure
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select


class InventoryPage(BasePage):

    # LOCATORS
    ITEM = ("xpath", "//div[@data-test='inventory-item']")
    ITEM_NAME = ("xpath", ".//div[@data-test='inventory-item-name']")
    ITEM_DESC = ("xpath", ".//div[@data-test='inventory-item-desc']")
    ITEM_PRICE = ("xpath", ".//div[@data-test='inventory-item-price']")
    ADD_ITEM_TO_BASKET_BUTTON = ("xpath", ".//button[@id[contains(.,'add')]]")
    REMOVE_ITEM_FROM_BASKET_BUTTON = ("xpath", ".//button[@id[contains(.,'remove')]]")
    PRODUCT_SORT_CONTAINER = ("xpath", "//select[@data-test='product-sort-container']")

    # ACTIONS

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

    @allure.step("Добавление указанного количества товаров в корзину")
    def add_specified_count_items_into_basket(self, count):
        items = []
        for _item in self.browser.find_elements(*self.ITEM)[0:count]:
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

    @allure.step("Открытие страницы товара")
    def open_item_page(self):
        item = self.find_element(self.ITEM)
        item.find_element(*self.ITEM_NAME).click()

    @allure.step("Сортировка товаров по параметру")
    def sort_items(self, sort_type):
        sort_container = Select(self.find_element(self.PRODUCT_SORT_CONTAINER))
        sort_container.select_by_value(sort_type)

    @allure.step("Удаление всех товаров из корзины")
    def remove_all_items_from_basket(self):
        remove_buttons = self.find_elements(self.REMOVE_ITEM_FROM_BASKET_BUTTON)
        assert len(remove_buttons) > 0, "Товаров в корзине нет"
        for button in remove_buttons:
            button.click()
        assert len(self.find_elements(self.REMOVE_ITEM_FROM_BASKET_BUTTON)) == 0, "В корзине остались товары"


    # SHOULD BE
    @allure.step("Проверка сортировки товаров по возрастанию цены")
    def should_be_items_sort_low_high_price(self):
        items_price = self.browser.find_elements(*self.ITEM_PRICE)
        min_price = float(items_price[0].text[1:])
        for item in items_price:
            item_price = float(item.text[1:])
            assert min_price <= item_price
            min_price = item_price

    @allure.step("Проверка сортировки товаров по убыванию цены")
    def should_be_items_sort_high_low_price(self):
        items_price = self.browser.find_elements(*self.ITEM_PRICE)
        max_price = float(items_price[0].text[1:])
        for item in items_price:
            item_price = float(item.text[1:])
            assert max_price >= item_price
            max_price = item_price

    @allure.step("Проверка сортировки товаров по возрастанию названия")
    def should_be_items_sort_a_z(self):
        items_name = self.browser.find_elements(*self.ITEM_NAME)
        min_name = items_name[0].text.lower()
        for item in items_name:
            item_name = item.text.lower()
            assert min_name <= item_name
            min_name = item_name

    @allure.step("Проверка сортировки товаров по убыванию названия")
    def should_be_items_sort_z_a(self):
        items_name = self.browser.find_elements(*self.ITEM_NAME)
        max_name = items_name[0].text.lower()
        for item in items_name:
            item_name = item.text.lower()
            assert max_name >= item_name
            max_name = item_name
















