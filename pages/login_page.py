import time
from .base_page import BasePage
from .locators import LoginPageLocators, ProductPageLocators


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
        assert all(
            input_fields), '>>> in LOGIN FORM SOME FIELD(s) is not presented!'

    def should_be_register_form(self):
        input_fields = (
            self.is_element_present(*LoginPageLocators.REG_EMAIL_FORM),
            self.is_element_present(*LoginPageLocators.REG_PSS_1_FORM),
            self.is_element_present(*LoginPageLocators.REG_PSS_2_FORM),
        )
        assert all(
            input_fields), '>>> in REGISTRATION FORM SOME FIELD(s) is not presented!'

    def should_not_be_success_massage(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            '>>> SUCCESS MASSAGE IS PRESENT, but should not be!'

    def register_new_user(self, email: str, password: str):
        login = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FORM)
        login.send_keys(email)
        pss_1 = self.browser.find_element(*LoginPageLocators.REG_PSS_1_FORM)
        pss_1.send_keys(password)
        pss_2 = self.browser.find_element(*LoginPageLocators.REG_PSS_2_FORM)
        pss_2.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.REG_BTN)
        btn.click()
        success_text = self.browser.find_element(
            *LoginPageLocators.SUCCESS_MESSAGE).text
        assert success_text == 'Спасибо за регистрацию!', '>>> REGISTRATION IS FAILED'
