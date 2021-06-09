from time import sleep

import page
from base.base import Base


class PageAddOrder(Base):

    def page_swipe(self):
        # swipe 滑动
        # count = 1
        for x in range(3):
            self.driver.swipe(1000, 1061, 100, 1061, duration=3000)
            # sleep(1)
            # count += 1  # 循环结束

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

    # 点击 发单主页
    def page_click_hair_letter(self):
        self.base_click(page.hair_letter)

    # 点击 带看
    def page_click_hair_take_look(self):
        self.base_click(page.hair_take_look)

    # 点击 大学
    def page_click_hair_big_school(self):
        self.base_click(page.hair_big_school)

    # 点击景区
    def page_click_hair_search(self):
        self.base_click(page.position_manage_scenic_spot)

    # 点击地图指定
    def page_click_map_assignment(self):
        self.base_click(page.hair_university_map_assignment)

    # 点击 清华大学
    def page_click_hair_qh_university(self):
        self.base_click(page.hair_qh_university)

    # 点击 北京大学
    def page_click_hair_bj_university(self):
        self.base_click(page.hair_bj_university)

    # 点击 发布带看订单
    def page_click_hai_details_launch(self):
        self.base_click(page.hai_details_launch)

    # 点击视频方式
    def page_click_hair_video(self):
        self.base_click(page.hair_video)

    # 输入 服务费
    def page_input_hair_service_input_box(self, money):
        self.base_input(page.hair_service_input_box, money)

    # 输入 需求输入框	xpath
    def page_input_hair_requirement_input_box(self, demand):
        self.base_input(page.hair_requirement_input_box, demand)

    # 点击 下一步 id
    def page_click_hair_next_step(self):
        self.base_click(page.hair_next_step)

    # 点击 立即发布 id
    def page_click_hair_publish_now(self):
        self.base_click(page.hair_publish_now)

    # 点击 好的 id
    def page_click_hair_good(self):
        self.base_click(page.hair_good)

    # 点击 发单记录 id
    def page_click_hair_billing_record(self):
        self.base_click(page.hair_billing_record)

    # 点击发单列表（新发单订单）
    def page_click_hair_billing_list(self):
        self.base_click(page.hair_billing_list)

    # 点击 等待接单
    def page_click_hair_waiting_for_order(self):
        self.base_click(page.hair_waiting_for_order)

    # 点击 对方已接单/未付款
    def page_click_hair_order_details_pay_no(self):
        self.base_click(page.hair_order_details_pay_no)

    # 我要取消订单
    def page_hair_page_hair_order_details_pay_not(self):
        self.base_click(page.hair_order_details_pay_no)

    # 点击 取消订单 id
    def page_click_hair_off_order(self):
        self.base_click(page.hair_off_order)

    # 确定 id
    def page_click_hair_determine(self):
        self.base_click(page.hair_determine)

    # 返回 id （订单详情）
    def page_click_hair_return_order_details(self):
        self.base_click(page.hair_return_order_details)

    # 返回 id （发单记录）
    def page_click_hair_return_billing_record(self):
        self.base_click(page.hair_return_Billing_record)

    # 输入 服务标题
    def page_input_add_skill_service_description(self, description):
        self.base_input(page.add_skill_service_description, description)

    # 指定位置
    def page_click_hair_designated_location(self):
        self.base_click(page.hair_designated_location)

    # 选择城市
    def page_click_hair_menu_next(self):
        self.base_click(page.hair_menu_next)

    # 选择地名(甘肃省 酒泉市)
    def page_click_hair_choice_place_name(self):
        self.base_click(page.hair_choice_place_name)

    # 使用该位置
    def page_click_hair_map_use_location(self):
        self.base_click(page.hair_map_use_location)

    # 疫情提示（知道了）
    # def page_click_hair_btn_pos(self):
    #     self.base_click(page.hair_btn_pos)

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
        self.page_login_other()

    # 断言 订单是否接单
    def page_hair_order_details_pay_no(self):
        try:
            # 查找服务标签
            self.base_finds(page.hair_order_details_pay_no, timeout=0.2)
            # 找到了，说明还有未支付订单
            return False
        except:
            # 异常，未找到，说明：删除未支付订单成功
            return True

    def if_order(self):
        self.page_hair_order_details_pay_no()
        # a = self.page_hair_order_details_pay_no()
        # print(self.page_hair_order_details_pay_no())
        if self.page_hair_order_details_pay_no() == False:
            self.page_hair_off_order_mo()

        else:
            self.page_hair_off_order()

    # 组合发单业务方法
    def page_hair(self, money, demand):
        self.driver.implicitly_wait(2)
        self.base_click(page.hair_letter)
        self.base_click(page.hair_take_look)
        self.base_click(page.hair_big_school)
        self.base_click(page.hair_bj_university)
        self.base_click(page.hai_details_launch)
        # self.base_click(page.hair_btn_pos)
        self.base_input(page.hair_service_input_box, money)
        self.base_input(page.hair_requirement_input_box, demand)
        self.base_click(page.hair_next_step)
        self.base_click(page.hair_publish_now)
        self.driver.wait_activity(".ui.Activity_Splash", 2)
        self.base_click(page.hair_good)
        # sleep(1)
        # self.driver.tap([(394, 1333)])

    # # 地图指定组合业务
    # def page_hair_map_assignment(self, money, demand):
    #     self.base_click(page.hair_letter)
    #     self.base_click(page.hair_take_look)
    #     sleep(1)
    #     self.base_click(page.hair_university_map_assignment)
    #     self.base_click(page.hair_designated_location)
    #     self.base_click(page.hair_menu_next)
    #     self.base_click(page.hair_choice_place_name)
    #     self.base_click(page.hair_map_use_location)
    #     self.base_click(page.add_skill_share_minute_charging)
    #     self.base_input(page.hair_service_input_box, money)
    #     self.base_input(page.hair_requirement_input_box, demand)
    #     self.base_click(page.hair_next_step)
    #     self.base_click(page.hair_publish_now)
    #     sleep(1)
    #     self.driver.tap([(394, 1333)])

    # 组合取消未接单订单业务方法
    def page_hair_off_order(self):
        self.base_click(page.hair_waiting_for_order)
        self.base_click(page.hair_off_order)
        self.base_click(page.hair_determine)
        self.base_click(page.hair_return_order_details)
        self.base_click(page.hair_return_Billing_record)

    # 组合取消已接单未支付业务方法
    def page_hair_off_order_mo(self):
        self.base_click(page.hair_order_details_pay_no)
        self.base_click(page.hair_order_details_pay_noo)
        self.base_click(page.hair_determine)
        self.base_click(page.hair_return_order_details)
        self.base_click(page.hair_return_Billing_record)

    def page_hair_add_place(self):
        self.base_click(page.hair_letter)
        self.base_click(page.hair_take_look)
        self.base_click(page.position_manage_scenic_spot)
