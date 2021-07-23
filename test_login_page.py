from .pages.login_page import LoginPage
from .urls import login_page_link


def test_guest_should_see_login_page(browser):
    link = login_page_link
    form = LoginPage(browser, link)
    form.open()
    form.should_be_login_page()
