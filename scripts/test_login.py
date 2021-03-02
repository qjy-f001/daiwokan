import sys
import os

sys.path.append(os.getcwd())
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
import pytest
from time import sleep
from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


def get_data():
    arrs = []
    for data in read_yaml("login.yaml").values():
        arrs.append(tuple(data.values()))
    return arrs


class TestLogin:
    # 初始化
    def setup_class(self):
        # 实例化获取PageLogin
        self.login = PageIn().page_get_pagelogin()
        self.login.page_get_into_app()

    # 结束
    def teardown_class(self):
        # 关闭driver驱动对象
        GetDriver.quit_driver()

    # 登录测试方法
    @pytest.mark.parametrize("phone, pwd, expect, success", get_data())
    def test_login(self, phone, pwd, expect, success):
        # 调用业务方法
        self.login.page_login(phone, pwd)

        if success == "1":
            try:
                # # 断言 昵称
                nickname = self.login.page_get_nickname()
                print("获取的昵称为：", nickname)
                assert self.login.page_get_nickname() == expect

            except Exception as e:
                # 截图 、日志
                self.login.base_get_img()
                log.error(e)
                # 抛异常
                raise

            finally:
                # sleep(1)
                # 点击 退出登录业务
                self.login.page_logout()
                # 点击 立即登录
                self.login.page_login_log_now()
                self.login.page_login_other()

        elif success == "3":
            try:
                register = self.login.page_get_register_phone()
                print("该账号未注册需要：", register)
                assert self.login.page_get_register_phone() == expect

            except Exception as e:
                # 截图 、日志
                self.login.base_get_img()
                log.error(e)
                # 抛异常
                raise
            finally:
                self.login.page_login_register_phone_back()

        else:
            try:
                # 断言 toast消息
                err_msg = self.login.page_get_toast(expect)
                print("获取的toast消息为：", err_msg)
                assert err_msg == expect
            except Exception as e:
                # 截图
                log.error(e)
                self.login.base_get_img()
                # 抛异常
                raise

            finally:
                pass
