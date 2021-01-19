import sys
import os

sys.path.append(os.getcwd())
from page.page_in import PageIn
from time import sleep
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
import pytest
from tool.get_driver import GetDriver

log = GetLog.get_log()


def get_data(key):
    arrs = []
    data = read_yaml("pagination.yaml").get(key)
    arrs.append(tuple(data.values()))
    return arrs


class TestOrderPagination:
    # 初始化
    def setup_class(self):
        self.hair = PageIn().page_get_pagehair()
        # 点击同意协议并登陆
        self.hair.page_get_into_app()
        PageIn().page_get_pagelogin().page_add_skill()

    # 结束
    def teardown_class(self):
        # 关闭driver驱动对象
        GetDriver.quit_driver()

    @pytest.mark.parametrize("search,money, demand,expect", get_data("dwk_order_pagination1"))
    def test_order_pagination(self, search, money, demand, expect):
        self.order_pagination = PageIn().page_get_pagepagination()
        self.order_pagination.page_click_hair_letter()
        self.order_pagination.page_add_billing_home_combination(search, money, demand, expect)
        # 取消订单
        self.hair = PageIn().page_get_pagehair()
        self.hair.page_login_me()
        self.hair.page_click_hair_billing_record()
        sleep(2)
        self.hair.if_order()

    def test2_add_hair(self, money="0.1", demand="随便看看"):
        self.page_order_pagination = PageIn().page_get_pagepagination()
        self.page_order_pagination.page_hair_map_assignment(money, demand)
        self.hair = PageIn().page_get_pagehair()
        self.hair.page_login_me()
        self.hair.page_click_hair_billing_record()
        sleep(2)
        self.hair.if_order()

    def test3_page_earn_money_order(self, search="西二旗"):
        self.page_order_pagination = PageIn().page_get_pagepagination()
        self.page_order_pagination.page_earn_money_order(search)

    def test4(self, search="西二旗"):
        self.page_order_pagination = PageIn().page_get_pagepagination()
        self.page_order_pagination.page_earn_money_order_u2(search)
        # self.page_order_pagination(base)
    #