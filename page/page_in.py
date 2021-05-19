from page.page_add_order import PageAddOrder
from page.page_login import PageLogin
from page.page_add_skiil import PageSkiil
from page.page_hair_single import PageHairSingle
from page.page_recommend import PageRecommend
from page.page_hometown import PageHometown
from page.page_campus import PageCampus
from page.page_position import PagePosition
from tool.get_driver import GetDriver
from page.page_chat import PageChat


class PageIn:
    def __init__(self):
        self.driver = GetDriver.get_driver()

    # 获取 登录页面对象
    def page_get_page_login(self):
        return PageLogin(self.driver)

    # 获取 地址管理页面对象
    def page_get_page_add_order(self):
        return PageAddOrder(self.driver)

    # 获取 地址管理页面对象
    def page_get_page_skiil(self):
        return PageSkiil(self.driver)

    # 获取 发单分页
    def page_get_page_hair_single(self):
        return PageHairSingle(self.driver)

    # 获取 推荐页面对象
    def page_get_recommend(self):
        return PageRecommend(self.driver)

    # 获取 家乡页面对象
    def page_get_hometown(self):
        return PageHometown(self.driver)

    # 获取 校园页面对象
    def page_get_campus(self):
        return PageCampus(self.driver)

    # 获取 位置管理页面对象
    def page_get_position(self):
        return PagePosition(self.driver)

    # 获取 聊天页面对象
    def page_get_chat(self):
        return PageChat(self.driver)
