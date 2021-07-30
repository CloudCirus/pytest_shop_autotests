from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_PAGE_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_PAGE_LINK = (By.CSS_SELECTOR, '.basket-mini .btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')


class LoginPageLocators:
    LOGIN_EMAIL_FORM = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PSS_FORM = (By.CSS_SELECTOR, '#id_login-password')
    REG_EMAIL_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PSS_1_FORM = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PSS_2_FORM = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success .wicon')


class MainPageLocators:
    LOGIN_PAGE_LINK = (By.CSS_SELECTOR, '#login_link')


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    alert_TITLE = (By.CSS_SELECTOR, '.alert-success strong')
    alert_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success strong')
