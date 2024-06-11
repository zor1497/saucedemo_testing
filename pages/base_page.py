from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    BASKET_LINK = ("xpath", "//a[@data-test='shopping-cart-link']")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)
        self.action = ActionChains(browser)
        self.base_url = "https://www.saucedemo.com/"


    # BASE_ACTIONS
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator), f"Элемент с локатором {locator} не найден")

    def find_elements(self, locator):
        try:
            elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            return []

    def get_current_url(self):
        return self.browser.current_url

    def is_opened_page(self, exp_page, act_page):
        return exp_page == act_page

    def is_present_element(self, locator):
        from selenium.common import NoSuchElementException
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True


    # ACTIONS
    @allure.step("Открытие страницы корзины")
    def open_basket(self):
        basket_link = self.find_element(self.BASKET_LINK)
        basket_link.click()
        assert self.is_opened_page(self.get_current_url(), "https://www.saucedemo.com/cart.html")





