from .pages.login_page import LoginPage
from .urls import MainLinks


def test_guest_should_see_login_page(browser):
    link = MainLinks.login_page
    form = LoginPage(browser, link)
    form.open()
    form.should_be_login_page()
