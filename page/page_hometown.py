# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from appium import webdriver
import os
from time import sleep

from appium.webdriver.mobilecommand import MobileCommand

import page
from base.base import Base


class PageHometown(Base):
    def switch_h5(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.tencent.mobileqq:mini"})

    def switch_app(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})

    # 点击 	仅在使用中允许(定位)
    def scroll_down(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        x = width / 2
        starty = height * 0.75
        endy = height * 0.20
        self.driver.swipe(x, starty, x, endy, 500)

    # 点击 	仅在使用中允许(定位)
    def page_login_locations(self):
        # # for x in range(3):
        # self.base_get_texts_click(page.login_location())
        # self.base_get_texts_click("仅在使用中允许")
        # self.base_click(page.login_location)
        # self.base_get_texts_click("仅在使用中允许")
        try:
            self.base_finds("仅在使用中允许", timeout=2)
            return True
        except:
            return False

    def page_login_location1(self):
        el = self.page_login_locations()
        while len(el):
            if el == True:
                self.base_click(page.login_location)
                # self.base_get_texts_click("仅在使用中允许")
            else:
                break
            # for i in el:
            #     i = self.base_click(page.page_login_locations())
            #     if i == False:
            #         break

        #     self.base_click(page.login_location)
        # elif self.page_login_location() == False:
        #     break

    # # for x in range(3):
    # self.base_click(page.login_location)

    def page_swipe(self):
        # for x in range(3):
        #     width = self.driver.get_window_size()['width']
        #     height = self.driver.get_window_size()['height']
        #     width*1.31,
        #     print(width, height)
        #     self.driver.swipe(width % 1.31,
        #                       height % 4.88,
        #                       width % 15.88,
        #                       height % 4.88, duration=3000)
        # print(width % 1.313868613138686131,
        #       height % 4.883720930232558139,
        #       width % 15.88235294117647059,
        #       height % 4.883720930232558139)
        # print(width % 0.0131,
        #       height % 0.0488,
        #       width % 15.88,
        #       height % 4.88)
        self.driver.swipe(822, 473, 68, 473, duration=3000)

    def page_swipe1(self):
        for x in range(11):
            self.driver.swipe(535, 2200, 535, 325, duration=3000)

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

    # 资讯
    def page_click_add_hometown_dynamic(self):
        self.base_click(page.add_hometown_dynamic)

    # 111
    def page_click_add_hometown_dynamic_details(self):
        self.base_click(page.add_hometown_dynamic_details)

    # 资讯详情
    def page_click_add_hometown_information_details(self):
        self.base_click(page.add_hometown_information_details)

    # 收藏
    def page_click_add_hometown_collection(self):
        self.base_click(page.add_hometown_collection)

    # 关注
    def page_click_add_hometown_information_collect(self):
        self.base_click(page.add_hometown_information_collect)

    def page_click_add_hometown_information_zx(self):
        self.base_click(page.add_hometown_information_zx)

    # 返回
    def page_login_register_phone_back(self):
        self.base_click(page.login_register_phone_back)

    def page_click_add_hometown_cancel_collection(self):
        self.base_click(page.add_hometown_cancel_collection)

    def page_click_add_hometown_information_zx2(self):
        self.base_click(page.add_hometown_information_exit)

    # 本地好店
    def page_click_home_shop(self):
        self.base_click(page.home_shop)

    # 发布
    def page_click_home_shop_release(self):
        self.base_click(page.home_shop_release)

    # 商品名称
    def page_input_home_trade_name(self, name):
        self.base_input(page.home_trade_name, name)

    # 店铺介绍
    def page_click_home_shop_introduction(self, introduce):
        self.base_input(page.home_shop_introduction, introduce)

    # 经营类别
    def page_click_home_business_category(self):
        self.base_click(page.home_business_category)

    # 小吃店
    def page_click_home_business_snack_bar(self):
        self.base_click(page.home_business_snack_bar)

    # 完成
    def page_click_home_business_complete(self):
        self.base_click(page.home_business_complete)

    # 地址
    def page_click_home_shop_address(self):
        self.base_click(page.home_shop_address)
        # 点击选择此位置

    def page_click_position_manage_choice_position(self):
        self.base_click(page.position_manage_choice_position)

    # 商户电话（选填)
    def page_click_home_merchant_telephone(self):
        self.base_click(page.home_merchant_telephone)

    # 删除店铺
    def page_click_home_dle_stores(self):
        self.base_click(page.home_dle_stores)

    # 商品管理
    def page_click_home_stores_administration(self):
        self.base_click(page.home_stores_administration)

    # 商品
    def page_click_home_commodity(self):
        self.base_click(page.home_commodity)

    # 发布按钮
    def page_click_home_commodity_release(self):
        self.base_click(page.home_commodity_release)

    # 发布+
    def page_click_home_release(self):
        self.base_click(page.home_release)

    # 家乡风景
    def page_click_home_scenery(self):
        self.base_click(page.home_scenery)

    # 选择图片
    def page_click_home_choice_picture(self):
        self.base_click(page.home_choice_picture)

    # # 完成
    def page_click_home_complete(self):
        self.base_click(page.home_complete)

    # 输入动图信息
    def page_input_home_input_dynamic_information(self, information):
        self.base_input(page.home_input_dynamic_information, information)

    # 发布按钮
    def page_input_home_input_describe(self, describe):
        self.base_input(page.home_input_describe, describe)

    # 发布按钮
    def page_click_home_dynamic_release(self):
        self.base_click(page.home_dynamic_release)

    # 点击 	仅在使用中允许(定位)
    def page_login_location(self):
        self.base_click(page.login_location)

    # 组合修改我的家乡业务方法
    def page_my_hometown(self):
        self.base_click(page.hair_letter)
        self.base_click(page.add_hometown)
        sleep(2)
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
        # self.driver.implicitly_wait(2)
        # self.base_click(page.add_hometown_choose_here_as_my_hometown)

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
        # self.base_click(page.hair_btn_pos)
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
        # self.page_login_location1()

        self.base_click(page.login_location)
        self.base_click(page.login_location)

        self.base_click(page.add_hometown_take_a_picture)
        self.base_click(page.add_hometown_camera)
        self.base_click(page.add_hometown_shot)
        self.base_click(page.add_hometown_ok_picture)
        sleep(1)
        self.base_click(page.add_hometown_submit)

    # 删除动态业务方法
    def page_hometown_delete_dynamic(self):
        self.base_click(page.login_me)
        self.base_click(page.add_hometown_personal_center)
        self.base_click(page.add_hometown_multiple_choice_button)
        # self.driver.wait_activity(".ui.Activity_Splash", 2)
        self.base_click(page.add_hometown_delete_dynamic)
        self.base_click(page.add_hometown_sign_out)
        # self.driver.get_window_size()['height']
        # driver.manage().window().getSize().width

    # 关注咨询
    def page_hometown_consulting(self):
        self.base_click(page.hair_letter)
        self.base_click(page.add_hometown)
        self.base_click(page.add_hometown_dynamic)
        sleep(3)
        self.base_click(page.add_hometown_dynamic_details)
        # sleep(2)
        # self.base_click(page.add_hometown_information_details)
        # print("当前所有环境：", self.driver.contexts)
        # print(self.driver.page_source)
        # sleep(3)
        # self.page_swipe1()
        self.switch_app()
        sleep(1)
        # print("当前所有环境：", self.driver.contexts)
        self.driver.switch_to.context("WEBVIEW_com.qjy.teleeye")
        self.base_click(page.add_hometown_collection)
        self.driver.switch_to.context("NATIVE_APP")
        self.base_click(page.login_register_phone_back)
        sleep(1)
        self.base_click(page.login_register_phone_back)

    # 取消关注的咨询
    def page_hometown_cancel_consulting(self):
        self.base_click(page.login_me)
        self.base_click(page.add_hometown_information_collect)
        self.driver.switch_to.context("WEBVIEW_com.qjy.teleeye")
        # self.base_click(page.add_hometown_information_collect)
        self.base_click(page.add_hometown_information_zx)
        # sleep(3)
        # self.page_swipe1()
        print("当前环境：", self.driver.context)
        # # sleep(2)
        # self.driver.tap([(553, 1912)])
        # self.driver.switch_to.context("NATIVE_APP")
        sleep(3)
        self.base_click_text("已收藏")
        self.driver.switch_to.context("NATIVE_APP")
        sleep(1)
        self.base_click(page.login_register_phone_back)
        self.base_click(page.add_hometown_information_exit)
        # self.base_click(page.login_register_phone_back)

    # 本地好店业务方法
    def page_local_stores(self, name, introduce):
        self.driver.implicitly_wait(5)
        self.base_click(page.hair_letter)
        self.base_click(page.add_hometown)
        self.base_click(page.home_shop)
        self.base_click(page.home_shop_release)
        self.base_input(page.home_trade_name, name)
        self.base_input(page.home_shop_introduction, introduce)
        self.base_click(page.home_business_category)
        self.base_click(page.home_business_snack_bar)
        self.base_click(page.home_business_complete)
        self.base_click(page.home_shop_address)
        self.base_click(page.position_manage_choice_position)
        self.driver.swipe(320, 1733, 320, 1460)
        self.base_click(page.home_commodity_release)

    # 图文动态业务方法
    def page_chart_dynamic(self, information, describe):
        self.driver.implicitly_wait(5)
        self.base_click(page.hair_letter)
        self.base_click(page.add_hometown)
        self.base_click(page.home_release)
        self.base_click(page.home_scenery)
        # self.base_click(page.home_release)
        self.base_click(page.home_release_scenery)  # 发布家乡风景
        self.base_click(page.home_picture_video)  # 选择图片

        # self.base_click(page.login_location)
        # self.base_click(page.login_location)

        self.base_click(page.home_choose_photo)  # 选照片
        self.base_click(page.home_choice_picture)
        self.base_click(page.home_complete)
        self.base_input(page.home_input_dynamic_information, information)
        sleep(2)
        self.base_input(page.home_input_describe, describe)
        self.base_click(page.home_dynamic_release)
