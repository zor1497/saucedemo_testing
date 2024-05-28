from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    LINK = "https://vk.com"
    LOGIN_FIELD = ("xpath", "//input[@name='login']")
    SIGN_IN_BUTTON = ("xpath", "//button[@type='submit']")
    ABOUT_VK_LINK = ("xpath", "(//a[@href='/about'])[2]")
    RULES_LINK = ("xpath", "(//a[@href='/terms'])[1]")

    @allure.step("Нажатие на ссылку 'О Вконтакте'")
    def open_about_page_from_login_page(self):
        self.wait.until(EC.visibility_of_element_located(self.ABOUT_VK_LINK)).click()
