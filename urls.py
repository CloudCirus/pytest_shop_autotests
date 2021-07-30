import pytest


class MainLinks:
    MAIN_PAGE = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_PAGE = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
    PROGUCT_PAGE_PROMO = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


class PromoLinks:
    PROMO_LIST = [
        f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
        for num in range(10)
    ]
    PROMO_LIST[7] = pytest.param(PROMO_LIST[7], marks=pytest.mark.xfail)
