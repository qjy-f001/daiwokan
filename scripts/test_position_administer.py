# import sys
# import os
#
# sys.path.append(os.getcwd())
# from time import sleep
# import pytest
# from tool.get_log import GetLog
#
# from tool.read_yaml import read_yaml
#
# from page.page_in import PageIn
# from tool.get_driver import GetDriver
#
# log = GetLog.get_log()
#
#
# def get_data(key):
#     arrs = []
#     data = read_yaml("hair.yaml").get(key)
#     arrs.append(tuple(data.values()))
#     return arrs
#
#
# class TestHair:
#     # 初始化
#     def setup_class(self):
#         self.hair = PageIn().page_get_pagehair()
#         # 点击同意协议并登陆
#         self.hair.page_get_into_app()
#         PageIn().page_get_pagelogin().page_add_skill()
#
#     # 结束
#     def teardown_class(self):
#         # 关闭driver驱动对象
#         GetDriver.quit_driver()
#
#     # def test01_position_manage(self, search="西二旗", describe="北京西二旗地铁站123"):
#     #     self.position_manage = PageIn().page_get_positionadminister()
#     #     self.position_manage.page_click_position_manage()
#     #     self.position_manage.page_position_manage_nuw_position(search, describe)
#
#     def test02(self, name="123", phone="13511112222", remarks="北京颐和园，随便看看"):
#         self.position_manage = PageIn().page_get_positionadminister()
#         self.position_manage.page_click_position_manage()
#         self.position_manage.page_click_modify_existing_location_information(name, phone, remarks)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#         # self.hair = PageIn().page_get_pagehair()
#         #
#         # self.hair.page_hair(money, demand)
#         # self.hair.page_login_me()
#         # self.hair.page_click_hair_billing_record()
#         # sleep(2)
#         # self.hair.if_order()