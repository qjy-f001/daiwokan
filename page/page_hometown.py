from time import sleep

import page
from base.base import Base


class PageHometown(Base):
    # 家乡分页
    def page_click_add_hometown(self):
        self.base_click(page.add_hometown)

    # 家乡活动
    def page_click_add_hometown_activity(self):
        self.base_click(page.add_hometown_activity)

    # “+”号图标
    def page_click_add_hometown_icon(self):
        self.base_click(page.add_hometown_icon)

    # 修改我的家乡
    def page_click_add_hometown_my(self):
        self.base_click(page.add_hometown_my)

    # 北京市
    def page_click_add_hometown_bj(self):
        self.base_click(page.add_hometown_bj)

    # 市
    def page_click_add_hometown_city(self):
        self.base_click(page.add_hometown_city)

    # 市辖区
    def page_click_add_hometown_city_jurisdiction(self):
        self.base_click(page.add_hometown_city_jurisdiction)

    # 区县
    def page_click_add_hometown_area_county(self):
        self.base_click(page.add_hometown_area_county)

    # 朝阳区
    def page_click_add_hometown_chaoyang_district(self):
        self.base_click(page.add_hometown_chaoyang_district)

    # 乡镇
    def page_click_add_hometown_township(self):
        self.base_click(page.add_hometown_township)

    # 奥运村街道
    def page_click_add_hometown_olympic_village_street(self):
        self.base_click(page.add_hometown_olympic_village_street)

    # 村 / 街道
    def page_click_add_hometown_village_street(self):
        self.base_click(page.add_hometown_village_street)

    # 北沙滩社区
    def page_click_add_hometown_north_beach_community(self):
        self.base_click(page.add_hometown_north_beach_community)

    # 选择此处为我的家乡
    def page_click_add_hometown_choose_here_as_my_hometown(self):
        self.base_click(page.add_hometown_choose_here_as_my_hometown)

    # 发布带看订单（web）
    def page_click_add_hometown_publish_with_order_web(self):
        self.base_click(page.add_hometown_publish_with_order_web)

    # 发布带看订单（安卓）
    def page_click_add_hometown_release_order_with_android(self):
        self.base_click(page.add_hometown_release_order_with_android)

    # 组合修改我的家乡业务方法
    def page_my_hometown(self):
        self.base_click(page.hair_letter)
        self.base_click(page.add_hometown)
        # print(self.driver.current_context)
        # print(self.driver.contexts)
        self.base_click(page.add_hometown_icon)
        self.base_click(page.add_hometown_my)
        self.base_click(page.add_hometown_bj)
        self.base_click(page.add_hometown_city)
        self.base_click(page.add_hometown_city_jurisdiction)
        self.base_click(page.add_hometown_area_county)
        self.base_click(page.add_hometown_chaoyang_district)
        self.base_click(page.add_hometown_township)
        self.base_click(page.add_hometown_olympic_village_street)
        self.base_click(page.add_hometown_village_street)
        self.base_click(page.add_hometown_north_beach_community)
        self.base_click(page.add_hometown_choose_here_as_my_hometown)

    # 组合我的家乡页面业务方法
    def page_my_hometown_modify(self):
        self.base_click(page.hair_letter)
        self.base_click(page.add_hometown)
        self.base_click(page.add_hometown_icon)
        self.base_click(page.add_hometown_publish_with_order_web)
        self.base_click(page.add_hometown_release_order_with_android)

    # 我的家乡发单业务
    def page_my_hometown_order(self, money, demand):
        # self.base_click(page.add_billing_home_billing_time)
        # sleep(1)
        self.base_input(page.add_billing_home_service_money, money)
        sleep(2)
        self.base_input(page.add_billing_home_demand, demand)
        self.base_click(page.add_billing_home_create_pay)
        self.base_click(page.add_billing_home_preview_issue)
        sleep(1)
        self.driver.tap([(394, 1333)])
