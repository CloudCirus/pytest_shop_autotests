from selenium import webdriver
from typing import Union


class BasePage():
    def __init__(self, browser: Union[webdriver.Chrome, webdriver.Firefox], url) -> None:
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
