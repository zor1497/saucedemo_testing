from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    LINK = "https://vk.com"
    LOGIN_FIELD = ("xpath", "//input[@name='login']")
    SIGN_IN_BUTTON = ("xpath", "//button[@type='submit']")
    ABOUT_VK_LINK = ("xpath", "(//a[@href='/about'])[2]")
    RULES_LINK = ("xpath", "(//a[@href='/terms'])[1]")
    CREATE_ACC_BUTTON = ("xpath", "//span[text()='Создать аккаунт']")
    FOR_DEVELOPERS_LINK = ("xpath", "(//a[@href='https://dev.vk.com'])[1]")

    @allure.step("Нажатие на ссылку 'О Вконтакте'")
    def click_on_about_vk_link(self):
        self.wait.until(EC.visibility_of_element_located(self.ABOUT_VK_LINK)).click()

    @allure.step("Нажатие на ссылку 'Разработчикам'")
    def click_on_for_developers_link(self):
        self.wait.until(EC.visibility_of_element_located(self.FOR_DEVELOPERS_LINK)).click()

