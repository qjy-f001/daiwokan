from time import sleep

import page
from base.base import Base

from tool.get_log import GetLog

log = GetLog.get_log()


class PageSkiil(Base):

        # def page_swipe(self):
        #     # swipe 滑动
        #     # count = 1
        #     for x in range(3):
        #         self.driver.swipe(1000, 1061, 100, 1061, duration=3000)
        #         # sleep(1)
        #         # count += 1  # 循环结束

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

    # 点击 添加技能和服务	id
    def page_click_add_skill_add_skills_services(self):
        self.base_click(page.add_skill_add_skills_services)

    # 输入 服务报价 id
    def page_click_add_skill_service_money(self, money):
        self.base_input(page.add_skill_service_money, money)

    # 输入服务介绍	id
    def page_click_add_skill_service_demand(self, demand):
        self.base_input(page.add_skill_service_demand, demand)

    # 点击 发布服务	id
    def page_click_add_skill_service_issue(self):
        self.base_click(page.add_skill_service_issue)

    # 获取服务标签
    def page_get_category_title(self):
        return self.base_get_list_text(page.add_skill_category_title)

    # 点击 我的服务   id
    def page_click_add_skill_service_text(self):
        self.base_click(page.add_skill_service_text)

    # 点击技能列表	id
    def page_click_add_skill_skill_service_message_descriptions(self):
        self.base_click(page.add_skill_skill_service_message_descriptions)

    # 点击删除服务	id
    def page_click_add_skill_details_delete(self):
        self.base_click(page.add_skill_details_delete)

    # 点击确定		id
    def page_click_add_skill_btn_pos(self):
        self.base_click(page.add_skill_btn_pos)

    # 输入 服务标题
    def page_input_add_skill_service_description(self, description):
        self.base_input(page.add_skill_service_description, description)

    def page_click_add_skill_share_second_charging(self):
        self.base_click(page.add_skill_share_second_charging)

    # 点击语音
    def page_click_add_skill_voice(self):
        self.base_click(page.add_skill_voice)

    # 点击视频
    def page_click_add_skill_video(self):
        self.base_click(page.add_skill_video)

    # 点击按分钟计费
    def page_click_add_skill_share_minute_charging(self):
        self.base_click(page.add_skill_share_minute_charging)

    # 断言 服务是否删除干净
    def page_address_is_exists(self):
        try:
            # 查找服务标签
            self.base_find(page.add_skill_skill_service_message_descriptions, timeout=2)
            # 找到了，说明删除服务失败
            return False
        except:
            # 异常，未找到，说明：删除地址成功
            return True

    # 点击返回		id
    def page_click_add_skill_menu_back(self):
        self.base_click(page.add_skill_menu_back)

    # 服务主页
    def page_click_add_skill_category_help(self):
        self.base_click(page.add_skill_category_help)

    # 服务
    def page_click_add_skill_list_first(self):
        self.base_click(page.add_skill_list_first)

    # 头像
    def page_click_add_skill_head_portrait(self):
        self.base_click(page.add_skill_head_portrait)

    # 个人技能
    def page_click_add_skill_personal_person(self):
        self.base_click(page.add_skill_personal_person)

    # 技能服务
    def page_click_add_skill_personal_skill(self):
        self.base_click(page.add_skill_personal_skill)

    # 他的技能服务
    def page_click_add_skill_skills_services(self):
        self.base_click(page.add_skill_skills_services)

    # 查询服务列表技能名称
    def page_find_add_skill_query_service_list_skill_name(self):
        self.base_find(page.add_skill_query_service_list_skill_name)

    # 查询服务列表技能服务介绍
    def page_find_add_skill_query_service_list_skill_introduce(self):
        self.base_find(page.add_skill_query_service_list_skill_introduce)

    # 查询技能标题
    def page_click_add_skill_personal_skill_adapter_title(self):
        self.base_find(page.add_skill_personal_skill_adapter_title)

    # 服务介绍
    def page_click_add_skill_personal_skill_adapter_demand(self):
        self.base_find(page.add_skill_personal_skill_adapter_demand)

    # 立即下单
    def page_click_add_skill_order_now(self):
        self.base_click(page.add_skill_order_now)

    # 支付服务费
    def page_click_add_skill_order_payment(self):
        self.base_click(page.add_skill_order_payment)

    # 选择支付宝支付
    def page_click_add_skill_order_payment_ali(self):
        self.base_click(page.add_skill_order_payment_ali)

    # 取消订单
    def page_click_add_skill_order_payment_cancel(self):
        self.base_click(page.add_skill_order_payment_cancel)

    # def page_click_

    # # 进入APP登陆页面
    # def page_get_into_app(self):
    #     self.base_click(page.login_agree)
    #     # 滑动引导页
    #     self.page_swipe()
    #     #  点击 立即体验
    #     self.base_click(page.login_now)
    #     # 点击 	仅在使用中允许(定位)
    #     self.base_click(page.login_location)
    #     # 点击 “我” 主页
    #     self.page_login_me()
    #     # 点击 立即登陆
    #     self.page_login_log_now()
    #     self.page_login_other()

    # 组合业务 新增技能和服务
    def page_add_skill_service_description(self, description, money, demand):
        self.base_click(page.add_skill_add_skills_services)
        # sleep(2)
        self.driver.implicitly_wait(5)
        self.base_input(page.add_skill_service_description, description)
        self.driver.implicitly_wait(5)
        self.base_click(page.add_skill_share_minute_charging)
        self.driver.implicitly_wait(5)
        self.base_input(page.add_skill_service_money, money)
        self.driver.implicitly_wait(5)
        self.base_click(page.add_skill_video)
        self.driver.implicitly_wait(5)
        self.base_input(page.add_skill_service_demand, demand)
        self.driver.implicitly_wait(5)
        self.base_click(page.add_skill_service_issue)

    # 组合业务 删除服务
    def page_add_delete_of_order(self):
        self.base_click(page.add_skill_service_text)
        el = self.base_get_list_text(page.add_skill_skill_service_message_descriptions)
        for i in range(len(el)):
            self.base_click(page.add_skill_skill_service_message_descriptions)
            self.base_click(page.add_skill_details_delete)
            self.base_click(page.add_skill_btn_pos)
            sleep(1)
        self.base_click(page.add_skill_menu_back)

    # 查看服务业务方法
    def page_see_skiil(self):
        self.base_click(page.add_skill_category_help)
        self.base_click(page.add_skill_list_first)
        self.base_click(page.add_skill_head_portrait)
        self.base_click(page.add_skill_personal_person)
        self.base_click(page.add_skill_personal_skill)
        self.base_click(page.add_skill_skills_services)
        self.base_click(page.add_skill_order_now)
        self.base_click(page.add_skill_order_payment)
        # co = self.driver.page_source
        # print(co)
        sleep(1)
        self.driver.tap([(889, 1931)])
        sleep(1)
        self.driver.tap([(355, 2087)])

        # self.driver.background_app(5)
        # self.driver.wait_activity(".ui.Activity_Splash", 2)
        # self.base_click(page.add_skill_order_payment_ali)
        # self.base_click(page.add_skill_order_payment_cancel)
