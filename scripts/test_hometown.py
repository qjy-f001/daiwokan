import sys
import os

sys.path.append(os.getcwd())
from time import sleep
import pytest
from tool.get_log import GetLog

from tool.read_yaml import read_yaml

from page.page_in import PageIn
from tool.get_driver import GetDriver


class TestOrderPagination:
    # 初始化
    def setup_class(self):
        self.login = PageIn().page_get_page_login()
        # 点击同意协议并登陆
        self.login.page_get_into_app()
        PageIn().page_get_page_login().page_add_skill()

    # 结束
    def teardown_class(self):
        # 关闭driver对象
        GetDriver.quit_driver()

    def test01_hometown(self, ):
        self.hometown = PageIn().page_get_hometown()
        # 修改我的家乡
        self.hometown.page_my_hometown()

    def test_02hometown_order(self, money="0.1", demand="随便看看"):
        # 发布我的家乡订单
        self.hometown = PageIn().page_get_hometown()
        self.hometown.page_my_hometown_modify()
        self.hair = PageIn().page_get_page_add_order()
        self.hometown.page_my_hometown_order(money, demand)
        sleep(2)
        self.hair.page_login_me()
        self.hair.page_click_hair_billing_record()
        sleep(2)
        self.hair.if_order()
