# import sys
# import os
#
# sys.path.append(os.getcwd())
# from time import sleep
# from tool.get_log import GetLog
# from tool.read_yaml import read_yaml
# import pytest
#
# from page.page_in import PageIn
# from tool.get_driver import GetDriver
#
# log = GetLog.get_log()
#
#
# class TestOrderPagination:
#     # 初始化
#     def setup_class(self):
#         self.login = PageIn().page_get_page_login()
#         # 点击同意协议并登陆
#         self.login.page_get_into_app()
#         PageIn().page_get_page_login().page_add_skill()
#
#     # 结束
#     def teardown_class(self):
#         # 关闭driver驱动对象
#         GetDriver.quit_driver()
#
#     # 首页业务组合方法
#     def test_recommendation_order(self, money="0.1", demand="随便看看"):
#         self.recommendation = PageIn().page_get_recommend()
#         self.recommendation.page_add_recommended_pagination_combination()
#         self.order = PageIn().page_get_page_hair_single()
#         self.order.page_add_recommendation_order(money, demand)
#         sleep(1)
#         self.hair = PageIn().page_get_page_add_order()
#         self.hair.page_login_me()
#         self.hair.page_click_hair_billing_record()
#         sleep(2)
#         self.hair.if_order()
