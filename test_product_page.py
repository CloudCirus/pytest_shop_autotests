from typing import Union
from .urls import MainLinks
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = MainLinks.product
    page = ProductPage(browser, link)
    page.open()
    page.can_use_add_to_cart_btn()
    page.solve_quiz_and_get_code()
    page.can_add_product_to_basket()
