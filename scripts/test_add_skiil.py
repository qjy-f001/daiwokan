import sys
import os

sys.path.append(os.getcwd())

import pytest
from tool.get_log import GetLog

from tool.read_yaml import read_yaml

from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


def get_data(key):
    arrs = []
    data = read_yaml("add_skiil.yaml").get(key)
    arrs.append(tuple(data.values()))
    return arrs


class TestSkiil:
    # 初始化
    def setup_class(self, ):
        # 获取 PageAddress
        self.add_skiil = PageIn().page_get_pageskiil()
        self.add_skiil.page_get_into_app()
        PageIn().page_get_pagelogin().page_add_skill()

    # 结束
    def teardown_class(self):
        # 关闭driver对象
        GetDriver.quit_driver()

    # 测试添加技能和服务方法
    @pytest.mark.parametrize("description, money, demand", get_data("dwk_add_skiil_001"))
    def test01_add_skiil(self, description, money, demand):
        self.add_skiil.page_add_skill_service_description(description, money, demand)
        try:
            # 断言
            pass
        except Exception as e:
            # 截图
            self.add_skiil.base_get_img()
            # 写日志
            log.error(e)
            # 抛异常
            raise

    # 删除地址
    def test02_add_delete_of_order(self):
        # 调用删除地址业务方法
        self.add_skiil.page_add_delete_of_order()
        try:
            # 断言 是否删除干净
            assert self.add_skiil.page_address_is_exists()
        except Exception as e:
            # 截图
            self.add_skiil.base_get_img()
            # 写日志
            log.error(e)
            # 抛异常
            raise