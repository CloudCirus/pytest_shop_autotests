from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_PAGE_LINK = (By.CSS_SELECTOR, '#login_link')


class MainPageLocators:
    LOGIN_PAGE_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_EMAIL_FORM = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PSS_FORM = (By.CSS_SELECTOR, '#id_login-password')
    REG_EMAIL_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PSS_1_FORM = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PSS_2_FORM = (By.CSS_SELECTOR, '#id_registration-password2')


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    alert_TITLE = (By.CSS_SELECTOR, '.alert-success strong')
    alert_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success strong')
