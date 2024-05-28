from selenium import webdriver
import pytest




@pytest.fixture(scope='function', autouse=True)
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

