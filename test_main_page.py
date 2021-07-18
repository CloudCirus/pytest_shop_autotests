from .pages.main_page import MainPage
from .urls import main_page_link


def test_guest_can_go_to_login_page(browser):
    link = main_page_link
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
