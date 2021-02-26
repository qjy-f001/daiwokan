from time import sleep

import page
from base.base import Base

from tool.get_log import GetLog

log = GetLog.get_log()


class PageRecommend(Base):
    # 点击 首页主页
    def page_click_hair_letter(self):
        self.base_click(page.hair_letter)

    # 推荐分页
    def page_click_add_recommended_pagination(self):
        self.base_click(page.add_recommended_pagination)

    def page_recommended_pagination_swipe1(self):
        # swipe 滑动
        count = 1
        while count <= 3:
            self.driver.swipe(530, 1950, 530, 255, duration=3000)
            sleep(1)
            count += 1  # 循环结束

    def page_recommended_pagination_swipe2(self):
        # swipe 滑动
        self.driver.swipe(530, 255, 530, 1950, duration=3000)

    # 返回
    def page_click_add_recommended_pagination_return(self):
        self.base_click(page.add_recommended_pagination_return)

    # 点击推荐分页地点名称
    def page_click_recommended_pagination_name(self):
        self.base_click(page.add_recommended_pagination_name)

    # 发布打开订单
    def page_click_add_recommended_pagination_release_order(self):
        self.base_click(page.add_recommended_pagination_release_order)

    # 点击 首页业务组合方法
    def page_add_recommended_pagination_combination(self):
        self.base_click(page.hair_letter)
        self.base_click(page.add_recommended_pagination)
        self.page_recommended_pagination_swipe1()
        self.page_recommended_pagination_swipe2()
        self.base_click(page.add_recommended_pagination_return)
        self.base_click(page.add_recommended_pagination_name)
        self.base_click(page.add_recommended_pagination_release_order)
