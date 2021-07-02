from time import sleep

import page
from base.base import Base


class PageCommodity(Base):

    # # 商品
    def page_commodity_homepage(self):
        self.base_click(page.commodity_homepage)

    # 首个商品
    def page_commodity_first_product(self):
        self.base_click(page.commodity_first_product)

    # 发起拼团
    def page_commodity_launch_group(self):
        self.base_click(page.commodity_launch_group)

    # 我的订单
    def page_commodity_my_order(self):
        self.base_click(page.commodity_my_order)

    # 首个订单
    def page_commodity_first_order(self):
        self.base_click(page.commodity_first_order)

    # 取消订单
    def page_commodity_cancel_order(self):
        self.base_click(page.commodity_cancel_order)

    # 确认
    def page_commodity_confirm(self):
        self.base_click(page.commodity_confirm)

    # 下单业务方法
    def page_place_an_order(self):
        self.base_click(page.commodity_homepage)
        self.base_click(page.commodity_first_product)
        self.base_click(page.commodity_launch_group)
        self.base_click(page.position_manage_back)
        self.base_click(page.position_manage_back)

    # 取消订单业务方法
    def page_cancel_order(self):
        self.base_click(page.login_me)
        self.base_click(page.commodity_my_order)
        self.base_click(page.commodity_first_order)
        self.base_click(page.commodity_cancel_order)
        self.base_click(page.commodity_confirm)
        self.base_click(page.position_manage_back)
        self.base_click(page.position_manage_back)
