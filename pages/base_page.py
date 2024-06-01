from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 20)
        self.action = ActionChains(browser)

    def open(self):
        with allure.step(f"Открытие страницы {self.BASE_URL}"):
            self.browser.get(self.BASE_URL)



