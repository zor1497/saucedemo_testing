from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    BASKET_LINK = ("xpath", "//a[@data-test='shopping-cart-link']")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.action = ActionChains(browser)
        self.base_url = "https://www.saucedemo.com"

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator), f"Элемент с локатором {locator} не найден")

    def get_current_url(self):
        return self.browser.current_url

    @allure.step("Открытие корзины")
    def open_basket(self):
        basket_link = self.find_element(self.BASKET_LINK)
        basket_link.click()





