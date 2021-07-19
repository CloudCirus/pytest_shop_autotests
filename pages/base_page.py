import selenium
from conftest import browser
from selenium import webdriver
from typing import Union
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser: Union[webdriver.Chrome, webdriver.Firefox], url, timeout=5) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

