from page.page_hair import PageHair
from page.page_login import PageLogin
from page.page_add_skiil import PageSkiil
from page.page_pagination import PagePagination
from page.page_recommendation import PageRecommendation
from page.page_hometown import PageHometown
from page.page_high_school import PageHighSchool
from page.page_position_administer import PagePositionAdminister
from tool.get_driver import GetDriver


class PageIn:
    def __init__(self):
        self.driver = GetDriver.get_driver()

    # 获取 登录页面对象
    def page_get_pagelogin(self):
        return PageLogin(self.driver)

    # 获取 地址管理页面对象
    def page_get_pagehair(self):
        return PageHair(self.driver)

    # 获取 地址管理页面对象
    def page_get_pageskiil(self):
        return PageSkiil(self.driver)

    # 获取 发单分页
    def page_get_pagepagination(self):
        return PagePagination(self.driver)

    # 获取 推荐页面对象
    def page_get_recommendation(self):
        return PageRecommendation(self.driver)

    # 获取 家乡页面对象
    def page_get_hometown(self):
        return PageHometown(self.driver)

    # 获取 校园页面对象
    def page_get_highschool(self):
        return PageHighSchool(self.driver)

    # 获取 校园页面对象
    def page_get_positionadminister(self):
        return PagePositionAdminister(self.driver)
