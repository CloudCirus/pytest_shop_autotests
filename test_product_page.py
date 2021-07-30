from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
from .urls import MainLinks, PromoLinks
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time


@pytest.mark.new
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = MainLinks.LOGIN_PAGE
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(
            email=f'{str(time.time())}@somemail.org', password='JcpBqTNxXn5Ev2q')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = MainLinks.PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            '>>> SUCCESS MASAGE IS PRESENT, but should not be!'

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = MainLinks.PROGUCT_PAGE_PROMO
        page = ProductPage(browser, link)
        page.open()
        page.can_use_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.can_add_product_to_basket()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = MainLinks.PROGUCT_PAGE_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.can_use_add_to_basket_btn()
    page.solve_quiz_and_get_code()
    page.can_add_product_to_basket()


@pytest.mark.skip
@pytest.mark.parametrize('link', PromoLinks.PROMO_LIST)
def test_guest_can_add_product_to_basket_promo(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.can_use_add_to_basket_btn()
    page.solve_quiz_and_get_code()
    page.can_add_product_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = MainLinks.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.can_use_add_to_basket_btn()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = MainLinks.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = MainLinks.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.can_use_add_to_basket_btn()
    page.message_should_dissapear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = MainLinks.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = MainLinks.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = MainLinks.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product()
    basket_page.should_be_empty_basket_message()
