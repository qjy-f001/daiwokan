from time import sleep

import page
from base.base import Base


class PageHometown(Base):
    # 点击 	仅在使用中允许(定位)
    def page_login_location(self):
        for x in range(3):
            self.base_click(page.login_location)

    def page_swipe(self):
        self.driver.swipe(822, 473, 68, 473, duration=3000)

    # 点击 “我” 主页
    def page_login_me(self):
        self.base_click(page.login_me)

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

    # 全国
    def page_click_add_hometown_whole_country(self):
        self.base_click(page.add_hometown_whole_country)

    # 北京市
    def page_click_add_hometown_bj(self):
        self.base_click(page.add_hometown_bj)

    # # 市
    # def page_click_add_hometown_city(self):
    #     self.base_click(page.add_hometown_city)

    # 市辖区
    def page_click_add_hometown_city_jurisdiction(self):
        self.base_click(page.add_hometown_city_jurisdiction)

    # # 区县
    # def page_click_add_hometown_area_county(self):
    #     self.base_click(page.add_hometown_area_county)

    # 东城区
    def page_click_add_hometown_dongcheng_district(self):
        self.base_click(page.add_hometown_dongcheng_district)

    # 东华门街道
    def page_click_add_hometown_township(self):
        self.base_click(page.add_hometown_township)

    # 多福巷社区
    def page_click_add_hometown_olympic_village_street(self):
        self.base_click(page.add_hometown_olympic_village_street)

    # # 村 / 街道
    # def page_click_add_hometown_village_street(self):
    #     self.base_click(page.add_hometown_village_street)

    # # 北沙滩社区
    # def page_click_add_hometown_north_beach_community(self):
    #     self.base_click(page.add_hometown_north_beach_community)

    # 选择此处为我的家乡
    def page_click_add_hometown_choose_here_as_my_hometown(self):
        self.base_click(page.add_hometown_choose_here_as_my_hometown)

    # 发布带看订单（web）
    def page_click_add_hometown_publish_with_order_web(self):
        self.base_click(page.add_hometown_publish_with_order_web)

    # 发布带看订单（安卓）
    def page_click_add_hometown_release_order_with_android(self):
        self.base_click(page.add_hometown_release_order_with_android)

    # 店铺转让
    def page_click_add_hometown_shop_transfer(self):
        self.base_click(page.add_hometown_shop_transfer)

    # 发布按钮
    def page_click_add_hometown_publish_button(self):
        self.base_click(page.add_hometown_publish_button)

    # 转让 店铺/生意（未发布过动态信息时显示）
    def page_click_add_hometown_transfer_shop(self):
        self.base_click(page.add_hometown_transfer_shop)

    # 选择店铺类型
    def page_click_add_hometown_select_store_type(self):
        self.base_click(page.add_hometown_select_store_type)

    # 店铺类型：写字楼
    def page_click_add_hometown_office_building(self):
        self.base_click(page.add_hometown_office_building)

    # 点击选好了
    def page_click_add_hometown_dynamic_yes(self):
        self.base_click(page.add_hometown_dynamic_yes)

    # 输入标题选项
    def page_input_add_hometown_title_options(self, title):
        self.base_input(page.add_hometown_title_options, title)

    # 填写转让店铺信息/原因
    def page_input_add_hometown_information_transfer(self, transfer):
        self.base_input(page.add_hometown_information_transfer, transfer)

    # 选择上传图片/视频
    def page_click_add_hometown_up_image(self):
        self.base_click(page.add_hometown_up_image)

    # 拍一张
    def page_click_add_hometown_take_a_picture(self):
        self.base_click(page.add_hometown_take_a_picture)

    # 相机
    def page_click_add_hometown_camera(self):
        self.base_click(page.add_hometown_camera)

    # 拍摄
    def page_click_add_hometown_shot(self):
        self.base_click(page.add_hometown_shot)

    # 确认图片
    def page_click_add_hometown_ok_picture(self):
        self.base_click(page.add_hometown_ok_picture)

    # 输入面积
    def page_input_add_hometown_input_area(self, area):
        self.base_input(page.add_hometown_input_area, area)

    # 输入装让费
    def page_input_add_hometown_input_charge(self, charge):
        self.base_input(page.add_hometown_input_charge, charge)

    # 选择经营行业
    def page_click_add_hometown_business(self):
        self.base_click(page.add_hometown_business)

    # 餐饮美食
    def page_click_add_hometown_beverage(self):
        self.base_click(page.add_hometown_beverage)

    # 食堂
    def page_click_add_hometown_canteen(self):
        self.base_click(page.add_hometown_canteen)

    # 完成
    def page_click_add_hometown_complete(self):
        self.base_click(page.add_hometown_complete)

    # 输入电话
    def page_input_add_hometown_input_phone(self, phone):
        self.base_input(page.add_hometown_input_phone, phone)

    # 提交
    def page_input_add_hometown_submit(self):
        self.base_click(page.add_hometown_submit)

    # 个人中心
    def page_click_add_hometown_personal_center(self):
        self.base_click(page.add_hometown_personal_center)

    # 多选按钮
    def page_click_add_hometown_multiple_choice_button(self):
        self.base_click(page.add_hometown_multiple_choice_button)

    # 删除动态
    def page_click_add_hometown_delete_dynamic(self):
        self.base_click(page.add_hometown_delete_dynamic)

    # 退出
    def page_click_add_hometown_sign_out(self):
        self.base_click(page.add_hometown_sign_out)

    # 组合修改我的家乡业务方法
    def page_my_hometown(self):
        self.base_click(page.hair_letter)
        self.base_click(page.add_hometown)
        self.base_click(page.add_hometown_my)
        sleep(2)
        self.base_click(page.add_hometown_whole_country)
        sleep(2)
        self.base_click(page.add_hometown_bj)
        sleep(2)
        # self.base_click(page.add_hometown_city)
        self.base_click(page.add_hometown_city_jurisdiction)
        sleep(3)
        self.base_click(page.add_hometown_dongcheng_district)
        sleep(2)
        self.base_click(page.add_hometown_township)
        sleep(2)
        self.base_click(page.add_hometown_olympic_village_street)
        self.driver.implicitly_wait(2)
        self.base_click(page.add_hometown_choose_here_as_my_hometown)

    # 组合我的家乡页面业务方法
    def page_my_hometown_modify(self):
        self.base_click(page.hair_letter)
        self.base_click(page.add_hometown)
        # self.base_click(page.add_hometown_icon)
        self.base_click(page.add_hometown_publish_with_order_web)
        # self.base_click(page.add_hometown_release_order_with_android)

    # 我的家乡发订单业务
    def page_my_hometown_order(self, money, demand):
        # self.base_click(page.add_billing_home_billing_time)
        # sleep(1)
        self.base_click(page.hair_btn_pos)
        self.base_input(page.add_billing_home_service_money, money)
        self.driver.implicitly_wait(2)
        self.base_input(page.add_billing_home_demand, demand)
        self.base_click(page.add_billing_home_create_pay)
        self.base_click(page.add_billing_home_preview_issue)
        sleep(1)
        self.driver.tap([(394, 1333)])

    def page_my_hometown_dynamic(self, building="写字楼", title="写字楼", transfer="123456", area="8888", charge="999",
                                 phone="13511112222"):
        self.base_click(page.hair_letter)
        self.base_click(page.add_hometown)
        sleep(2)
        self.page_swipe()
        self.base_click(page.add_hometown_shop_transfer)
        sleep(2)
        self.base_click(page.add_hometown_transfer_shop)
        self.base_click(page.add_hometown_select_store_type)
        self.base_click(page.add_hometown_office_building)
        self.base_click(page.add_hometown_dynamic_yes)
        sleep(1)
        self.base_input(page.add_hometown_title_options, title)
        self.base_input(page.add_hometown_information_transfer, transfer)
        self.base_input(page.add_hometown_input_area, area)
        # sleep(1)
        # self.driver.tap([(343, 1576)])
        self.base_input(page.add_hometown_input_charge, charge)
        self.base_click(page.add_hometown_business)
        self.base_click(page.add_hometown_beverage)
        self.base_click(page.add_hometown_canteen)
        self.base_click(page.add_hometown_complete)
        self.base_input(page.add_hometown_input_phone, phone)
        self.base_click(page.add_hometown_up_image)
        self.page_login_location()
        self.base_click(page.add_hometown_take_a_picture)
        self.base_click(page.add_hometown_camera)
        self.base_click(page.add_hometown_shot)
        self.base_click(page.add_hometown_ok_picture)
        self.base_click(page.add_hometown_submit)

    def page_hometown_delete_dynamic(self):
        self.base_click(page.login_me)
        self.base_click(page.add_hometown_personal_center)
        self.base_click(page.add_hometown_multiple_choice_button)
        # self.driver.wait_activity(".ui.Activity_Splash", 2)
        self.base_click(page.add_hometown_delete_dynamic)
        self.base_click(page.add_hometown_sign_out)
