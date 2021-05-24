from time import sleep

import page
from base.base import Base
from tool.get_log import GetLog

log = GetLog.get_log()


class PageChat(Base):

    # 消息主页
    def page_chat(self):
        self.base_click(page.chat)

    # 第一条通话信息
    def page_chat_information(self):
        self.base_click(page.chat_information)

    # 用户头像
    def page_chat_portrait(self):
        self.base_click(page.chat_portrait)

    # 聊一聊
    def page_chat_have_a_chat(self):
        self.base_click(page.chat_have_a_chat)

    # 取消注册新账号，点击返回
    def page_login_register_phone_back(self):
        self.base_click(page.login_register_phone_back)

    # 点击 “我” 主页
    def page_chat_combination(self):
        self.base_click(page.chat)
        self.base_click(page.chat_information)
        self.base_click(page.chat_portrait)
        # self.base_click(page.chat_have_a_chat)
        sleep(1)
        self.base_click(page.login_register_phone_back)
        sleep(1)
        self.base_click(page.login_register_phone_back)
