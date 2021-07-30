from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def can_use_add_to_basket_btn(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        btn.click()

    def can_add_product_to_basket(self):

        def get_value(locator, browser=self.browser):
            element = browser.find_element(*locator).text
            return element

        title = get_value(ProductPageLocators.TITLE)
        price = get_value(ProductPageLocators.PRICE)
        alert_title = get_value(ProductPageLocators.alert_TITLE)
        alert_price = get_value(ProductPageLocators.alert_PRICE)

        assert title == alert_title and price == alert_price, '>>> PRODUCT not added to basket!'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            '>>> SUCSESS MESAGE is presented, but should not be!'

    def message_should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            '>>> SUCCESS MESSAGE IS NOT dissapear!'
