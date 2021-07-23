from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_PAGE_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_EMAIL_FORM = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PSS_FORM = (By.CSS_SELECTOR, '#id_login-password')
    REG_EMAIL_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PSS_1_FORM = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PSS_2_FORM = (By.CSS_SELECTOR, '#id_registration-password2')