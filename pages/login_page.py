from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '>>> LOGIN LINK is not presented in URL!'

    def should_be_login_form(self):
        input_fields = (
            self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FORM),
            self.is_element_present(*LoginPageLocators.LOGIN_PSS_FORM),
        )
        assert all(input_fields), '>>> in LOGIN FORM SOME FIELD(s) is not presented!'

    def should_be_register_form(self):
        input_fields = (
            self.is_element_present(*LoginPageLocators.REG_EMAIL_FORM),
            self.is_element_present(*LoginPageLocators.REG_PSS_1_FORM),
            self.is_element_present(*LoginPageLocators.REG_PSS_2_FORM),
        )
        assert all(input_fields), '>>> in REGISTRATION FORM SOME FIELD(s) is not presented!'
