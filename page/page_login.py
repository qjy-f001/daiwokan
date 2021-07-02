import page

from base.base import Base
from tool.get_log import GetLog
from asyncio import sleep

log = GetLog.get_log()


class PageLogin(Base):

    def page_swipe(self):
        # for x in range(3):
        # width = self.driver.get_window_size()['width']
        # height = self.driver.get_window_size()['height']
        # self.driver.swipe(width - 80, height - 1000, width - 1000, height - 1000, duration=3000)
        # # swipe 滑动
        # # count = 1
        for x in range(3):
            self.driver.swipe(1000, 1061, 100, 1061, duration=3000)
        #     # sleep(1)
        #     # count += 1  # 循环结束

    # 点击 同意并登陆
    def page_login_agree(self):
        self.base_click(page.login_agree)

    #  点击 立即体验
    def page_login_now(self):
        self.base_click(page.login_now)

    # 点击 	仅在使用中允许(定位)
    def page_login_location(self):
        self.base_click(page.login_location)

    # 点击 “我” 主页
    def page_login_me(self):
        self.base_click(page.login_me)

    # 点击 立即登录
    def page_login_log_now(self):
        self.base_click(page.login_log_now)

    # 点击 其他方式登录
    def page_login_other(self):
        self.base_click(page.login_login_other)

    # 输入用户名
    def page_input_phone(self, phone):
        # 调用 输入方法
        self.base_input(page.login_phone, phone)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    #  返回 昵称
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 获取 toast消息 ->登录失败
    def page_get_toast(self, msg):
        return self.base_get_toast(msg)

    # 返回注册手机号
    def page_get_register_phone(self):
        return self.base_get_text(page.login_register_phone)

    # 点击 配置
    def page_click_login_setting(self):
        self.base_click(page.login_setting)

    # 点击 点击退出登录
    def page_click_log_out(self):
        self.base_click(page.login_log_out)

    # 点击 点击确认
    def page_login_confirm(self):
        self.base_click(page.login_confirm)

    # 点击 返回
    def page_login_sign_out(self):
        self.base_click(page.login_sign_out)

    # 取消注册新账号，点击返回
    def page_login_register_phone_back(self):
        self.base_click(page.login_register_phone_back)

    # 点击 微信登录
    def page_login_chat_login(self):
        self.base_click(page.login_chat_login)

    # 退出登陆业务方法
    def page_logout(self):
        log.info("正在执行退出登录业务方法")
        self.page_click_login_setting()
        self.page_click_log_out()
        self.page_login_confirm()

    # 进入APP登陆页面
    def page_get_into_app(self):
        self.page_login_agree()
        # 滑动引导页
        self.page_swipe()
        #  点击 立即体验
        self.page_login_now()
        # 点击 	仅在使用中允许(定位)
        self.base_click(page.login_location)
        # 点击 “我” 主页
        self.page_login_me()
        # 点击 立即登陆
        self.page_login_log_now()
        self.base_click(page.login_check_agreement)
        # 点击 微信登录
        self.base_click(page.login_chat_login)
        # self.page_login_other()

    # 组合业务方法
    def page_login(self, phone, pwd):
        log.info("【登录业务】正在执行登录操作，用户名：{} 密码：{}".format(phone, pwd))
        # self.page_click_login_btn()
        # self.page_login_other()
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    def page_add_skill(self, phone='13511112222', pwd='123456'):
        # self.base_click(page.login_log_now)
        # self.base_click(page.login_login_other)
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        sleep(1)
        self.page_click_login_btn()
