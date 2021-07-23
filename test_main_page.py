from selenium import webdriver
from typing import Union
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .urls import main_page_link


def test_guest_can_go_to_login_page(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = main_page_link
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()


def test_guest_should_see_login_link(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = main_page_link
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
