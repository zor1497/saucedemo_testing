from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)


    def open(self):
        with allure.step(f"Открытие страницы {self.LINK}"):
            self.browser.get(self.LINK)

    def is_opened(self):
        with allure.step(f"Проверка, что открылась страница {self.LINK}"):
            self.wait.until(EC.url_contains(self.LINK))
