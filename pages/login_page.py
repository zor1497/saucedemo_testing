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
    LANGUAGE_LIST = ("id", "all_languages_list")
    CLOSE_LANGUAGE_LIST_BUTTON = ("xpath", "//div[@class='box_controls_wrap']//button")
    LANGUAGE_SEARCH_FROM = ("id", "language_search_form")
    LANGUAGE_SEARCH_BUTTON = ("xpath", "(//div[@class='ui_search_input_block']//button)[1]")
    LANGUAGE_LINK = ("xpath", "(//a[text()='все языки »'])[1]")
    LANGUAGES_IN_FIRST_COLUMN = ("xpath", "//div[@class='language_column fl_l']//a")
    LOGIN_MOBILE_HEADER = ("xpath", "//div[@class='login_mobile_header']")


    @allure.step("Нажатие на ссылку 'О Вконтакте'")
    def click_on_about_vk_link(self):
        self.wait.until(EC.visibility_of_element_located(self.ABOUT_VK_LINK)).click()

    @allure.step("Нажатие на ссылку 'Разработчикам'")
    def click_on_for_developers_link(self):
        self.wait.until(EC.visibility_of_element_located(self.FOR_DEVELOPERS_LINK)).click()

    @allure.step("Нажатие на ссылку 'Все языки'")
    def click_on_language_link(self):
        self.wait.until(EC.element_to_be_clickable(self.LANGUAGE_LINK)).click()
        self.wait.until(EC.visibility_of_element_located(self.LANGUAGE_LIST))

    def type_text_into_language_search_form(self, text):
        with allure.step(f"Ввод текса {text} в поле поиска языков"):
            language_search_form = self.wait.until(EC.visibility_of_element_located(self.LANGUAGE_SEARCH_FROM))
            language_search_form.send_keys(text)
            assert language_search_form.get_attribute("value") == text

    @allure.step("Нажатие на ссылку английского языка")
    def click_on_english_language(self):
        english_language = ("xpath", "//span[text()='English']")
        self.wait.until(EC.element_to_be_clickable(english_language)).click()

    @allure.step("Заголовок страницы авторизации описывается на английском языке")
    def should_be_english_version(self):
        assert self.wait.until(EC.visibility_of_element_located(self.LOGIN_MOBILE_HEADER)).text == "VK for mobile devices"




