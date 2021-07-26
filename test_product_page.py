from pytest_shop_autotests.pages.login_page import LoginPage
from pytest_shop_autotests.pages.locators import ProductPageLocators
from .urls import MainLinks, PromoLinks
from .pages.product_page import ProductPage
import pytest


def test_guest_can_add_product_to_basket(browser):
    link = MainLinks.product_promo
    page = ProductPage(browser, link)
    page.open()
    page.can_use_add_to_cart_btn()
    page.solve_quiz_and_get_code()
    page.can_add_product_to_basket()


@pytest.mark.skip
@pytest.mark.parametrize('link', PromoLinks.promo_list)
def test_guest_can_add_product_to_basket_promo(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.can_use_add_to_cart_btn()
    page.solve_quiz_and_get_code()
    page.can_add_product_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = MainLinks.product
    page = ProductPage(browser, link)
    page.open()
    page.can_use_add_to_cart_btn()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_cant_see_success_message(browser):
    link = MainLinks.product
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = MainLinks.product
    page = ProductPage(browser, link)
    page.open()
    page.can_use_add_to_cart_btn()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_should_see_login_link_on_product_page(browser):
    link = MainLinks.product
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = MainLinks.product
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
