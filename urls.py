import pytest


class MainLinks:
    main_page = 'http://selenium1py.pythonanywhere.com/'
    login_page = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    product = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


class PromoLinks:
    promo_list = [
        f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}' \
        for num in range(10)
    ]
    promo_list[7] = pytest.param(promo_list[7], marks=pytest.mark.xfail)
