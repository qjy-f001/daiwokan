from time import sleep

import page
from base.base import Base


class PageHighSchool(Base):
    # 校园分页
    def page_click_add_high_school(self):
        self.base_click(page.add_high_school)

    # “+”图标
    def page_click_add_high_school_icon(self):
        self.base_click(page.add_high_school_icon)

    # 修改我的学校
    def page_click_add_high_school_modify(self):
        self.base_click(page.add_high_school_modify)

    # 发布带看订单
    def page_click_add_high_school_release_order_web(self):
        self.base_click(page.add_high_school_release_order_web)

    # def page_click_
    # 搜索框（输入清华大学）
    def page_input_add_high_school_search_box(self, box):
        self.base_input(page.add_high_school_search_box, box)

    # 清华大学
    def page_click_add_high_school_qh(self):
        self.base_click(page.add_high_school_qh)

    # 发布带看订单
    def page_click_add_high_school_release_order_android(self):
        self.base_click(page.add_high_school_release_order_android)

    # 校园活动
    def page_click_add_high_school_campus_activities(self):
        self.base_click(page.add_high_school_campus_activities)

    # 高中投票
    def page_click_add_high_school_high_school_voting(self):
        self.base_click(page.add_high_school_high_school_voting)

    # 大学投票
    def page_click_add_high_school_university_voting(self):
        self.base_click(page.add_high_school_university_voting)

    # 学校 （上地学校）
    def page_click_add_high_school_shangdi(self):
        self.base_click(page.add_high_school_shangdi)

    # 八维学校
    def page_click_add_high_school_bawei(self):
        self.base_click(page.add_high_school_bawei)

    # 投上一票
    def page_click_add_high_school_vote_for_it(self):
        self.base_click(page.add_high_school_vote_for_it)

    # 给母校发单
    def page_click_add_high_school_dear_school(self):
        self.base_click(page.add_high_school_dear_school)

    # 校园搜索框输入清华
    def page_input_add_high_school_search(self, qh):
        self.base_input(page.add_high_school_search, qh)

    # 搜索清华
    def page_click_add_high_school_search_qh(self):
        self.base_click(page.add_high_school_search_qh)

    # 点击按分钟计费
    def page_click_add_skill_share_minute_charging(self):
        self.base_click(page.add_skill_share_minute_charging)

    # 组合修改我的学校业务
    def page_modify_my_school(self, qh):
        self.base_click(page.hair_letter)
        self.base_click(page.add_high_school)
        self.base_click(page.add_high_school_icon)
        self.base_click(page.add_high_school_modify)
        sleep(2)
        # self.driver.switch_to.active_element()
        # self.base_finds(page.add_high_school_search)
        # print(self.base_finds(page.add_high_school_search))
        self.driver.tap([(462, 632)])
        self.base_input(page.add_high_school_search, qh)
        #
        self.base_click(page.add_high_school_search_qh)

    # 组合修改我的学校发单业务
    def page_my_school_order(self, money, demand):
        self.base_click(page.hair_letter)
        self.base_click(page.add_high_school)
        self.base_click(page.add_high_school_icon)
        self.base_click(page.add_high_school_release_order_web)
        self.base_click(page.add_high_school_release_order_android)

        self.base_click(page.add_skill_share_minute_charging)
        self.base_input(page.add_billing_home_service_money, money)
        sleep(2)
        self.base_input(page.add_billing_home_demand, demand)
        self.base_click(page.add_billing_home_create_pay)
        self.base_click(page.add_billing_home_preview_issue)
        sleep(1)
        self.driver.tap([(394, 1333)])