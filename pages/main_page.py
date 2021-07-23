from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(
            *MainPageLocators.LOGIN_PAGE_LINK)
        login_link.click()
        assert LoginPage(
            self.browser, url=self.browser.current_url), '>>> LOGIN PAGE is not relevant!'

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_PAGE_LINK), '>>> LOGIN LINK is not presented !!! <<<'
