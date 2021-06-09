import sys
import os

sys.path.append(os.getcwd())
from time import sleep
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
import pytest

from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


class TestCampus:
    # 初始化
    def setup_class(self):
        # 实例化获取PageLogin
        self.login = PageIn().page_get_page_login()
        self.login.page_get_into_app()
        PageIn().page_get_page_login().page_add_skill()

    # 结束
    def teardown_class(self):
        # 关闭driver驱动对象
        GetDriver.quit_driver()

    # def test_campus(self, qh="清华大学"):
    #     self.test_high_school = PageIn().page_get_campus()
    #     # 修改我的母校
    #     self.test_high_school.page_modify_my_school(qh)
    #
    # def test_campus_order(self, money="0.1", demand="随便看看"):
    #     self.test_high_school = PageIn().page_get_campus()
    #     # 导入我的家乡发单业务
    #     self.test_high_school.page_my_school_order(money, demand)
    #     self.hair = PageIn().page_get_page_add_order()
    #     # 删除我的订单
    #     self.hair.page_login_me()
    #     self.hair.page_click_hair_billing_record()
    #     self.hair.if_order()
