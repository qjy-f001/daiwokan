import sys
import os

sys.path.append(os.getcwd())
from time import sleep
import pytest
from tool.get_log import GetLog

from tool.read_yaml import read_yaml

from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


def get_data():
    arrs = []
    for data in read_yaml("add_order.yaml").values():
        arrs.append(tuple(data.values()))
    return arrs


class TestAddOrder:
    # 初始化
    def setup_class(self):
        self.login = PageIn().page_get_page_login()
        # 点击同意协议并登陆
        self.login.page_get_into_app()
        PageIn().page_get_page_login().page_add_skill()

    # 结束
    def teardown_class(self):
        # 关闭driver驱动对象
        GetDriver.quit_driver()

    @pytest.mark.parametrize("money, demand", get_data())
    def test01_add_hair(self, money, demand):
        self.hair = PageIn().page_get_page_add_order()
        self.hair.page_hair(money, demand)
        self.hair.page_login_me()
        self.hair.page_click_hair_billing_record()
        sleep(2)
        self.hair.if_order()

