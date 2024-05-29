from selenium.common import ElementClickInterceptedException

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure



class AboutPage(BasePage):
    LINK = "https://vk.com/about"
    REGISTER_LINK = ("xpath", "//a[@href='/join']")

    @allure.step("Нажатие на ссылку 'Регистрация'")
    def click_on_register_link(self):
        element = self.wait.until(EC.element_to_be_clickable(self.REGISTER_LINK))
        self.browser.execute_script("arguments[0].click();", element)

