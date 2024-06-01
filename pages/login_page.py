from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    BASE_URL = "https://vk.com"
    LOGIN_FIELD = ("xpath", "//input[@name='login']")
    SIGN_IN_BUTTON = ("xpath", "//button[@type='submit']")
    ABOUT_VK_LINK = ("xpath", "(//a[@href='/about'])[2]")
    RULES_LINK = ("xpath", "(//a[@href='/terms'])[1]")
    CREATE_ACC_BUTTON = ("xpath", "//span[text()='Создать аккаунт']")
    FOR_DEVELOPERS_LINK = ("xpath", "(//a[@href='https://dev.vk.com'])[1]")
    MESSAGE_ERROR_AREA = ("xpath", "//div[@class='VkIdForm__messageError']")

    @allure.step("Нажатие на ссылку 'О Вконтакте'")
    def click_on_about_vk_link(self):
        self.wait.until(EC.visibility_of_element_located(self.ABOUT_VK_LINK)).click()

    @allure.step("Нажатие на ссылку 'Разработчикам'")
    def click_on_for_developers_link(self):
        self.wait.until(EC.visibility_of_element_located(self.FOR_DEVELOPERS_LINK)).click()

    @allure.step("Очистка поля логина")
    def clear_login_field(self):
        login_field = self.wait.until(EC.visibility_of_element_located(self.LOGIN_FIELD))
        login_field.clear()

    def type_text_into_login_field(self, text):
        with allure.step(f"Ввод значения '{text}' в поле логина"):
            login_field = self.wait.until(EC.visibility_of_element_located(self.LOGIN_FIELD))
            login_field.send_keys(text)
            assert login_field.get_attribute("value") == text

    @allure.step("Нажатие на кнопку 'Войти'")
    def click_on_sign_in_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SIGN_IN_BUTTON)).click()

    @allure.step("Отображение сообщения об ошибке")
    def should_be_message_error(self):
        self.wait.until(EC.visibility_of_element_located(self.MESSAGE_ERROR_AREA))






