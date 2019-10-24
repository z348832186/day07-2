from page.page_card import PageCard
from page.page_login import PageLogin
from page.page_order import PageOrder
from page.page_pay import PagePay


class PageIn:

    # 获取PageCard对象
    def page_get_pagecard(self):
        return PageCard()

    # 获取 PageLogin对象
    def page_get_pagelogin(self):
        return PageLogin()

    # 获取 PageOrder对象
    def page_get_pageorder(self):
        return PageOrder()

    # 获取 PagePay对象
    def page_get_pagepay(self):
        return PagePay()