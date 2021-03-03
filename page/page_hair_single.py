# from page.page_in import PageIn
from time import sleep

import page
from base.base import Base
from selenium.webdriver.support.ui import WebDriverWait
from tool.get_log import GetLog

log = GetLog.get_log()


class PageHairSingle(Base):
    # 点击 首页主页
    def page_click_hair_letter(self):
        self.base_click(page.hair_letter)

    #  发单分页
    def page_click_add_billing_home_page(self):
        self.base_click(page.add_billing_home_page)

    # 搜索
    def page_click_add_billing_home_location_search(self):
        self.base_click(page.add_billing_home_location_search)

    # 搜索框（输入西二旗）
    def page_input_add_billing_home_baidumap_search(self, search):
        self.base_input(page.add_billing_home_baidumap_search, search)

    # 西二旗（第一个搜索内容）
    def page_click_add_billing_home_search_content(self):
        self.base_click(page.add_billing_home_search_content)

    # 按分钟计费
    def page_click_add_billing_home_billing_time(self):
        self.base_click(page.add_billing_home_billing_time)

    # 服务费
    def page_input_add_billing_home_service_money(self, money):
        self.base_input(page.add_billing_home_service_money, money)

    # 需求（西二旗带看）
    def page_input_add_billing_home_demand(self, demand):
        self.base_input(page.add_billing_home_demand, demand)

    # 下一步
    def page_click_add_billing_home_create_pay(self):
        self.base_click(page.add_billing_home_create_pay)

    # 立即带看
    def page_click_add_billing_home_preview_issue(self):
        self.base_click(page.add_billing_home_preview_issue)

    # 立即发布
    def page_click_add_billing_home_order_preview_issue(self):
        self.base_click(page.add_billing_home_order_preview_issue)

    # 点击 好的 id
    def page_click_hair_good(self):
        self.driver.tap([(394, 1333), ])

    # 断言标题（找人带看>西二旗-地铁站）
    def page_get_add_billing_home_preview_type(self):
        return self.base_get_text(page.add_billing_home_preview_type)

    # 断言需求（西二旗带看）
    def page_get_add_billing_home_preview_demand(self):
        return self.base_get_text(page.add_billing_home_preview_demand)

    # 挣钱主页
    def page_click_add_earn_money_homepage(self):
        self.base_click(page.add_earn_money_homepage)

    # 地点分类
    def page_click_add_earn_money_location_classification(self):
        self.base_click(page.add_earn_money_location_classification)

    # 按位置搜索
    def page_add_earn_money_location_search_by_location(self):
        self.base_click(page.add_earn_money_location_search_by_location)

    # 点击搜索
    def page_click_add_earn_money_location_site(self):
        self.base_click(page.add_earn_money_location_site)

    # 不限地点
    def page_click_add_earn_money_location_site_unlimited(self):
        self.base_click(page.add_earn_money_location_site_unlimited)

    # 景区搜索框
    def page_input_scenic_spot_search_box(self, search):
        self.base_input(page.position_manage_spot_search, search)

    # 景区添加景点
    def page_click_position_manage_spot_add(self):
        self.base_click(page.position_manage_spot_add)

    # 断言标题
    def page_assertion_preview_type(self, expect):
        data = self.page_get_add_billing_home_preview_type()
        # data = 1
        # print(data)
        if expect == data:
            try:
                preview_type = self.page_get_add_billing_home_preview_type()
                print("获取正确的服务标题为：", preview_type)
                assert self.page_get_add_billing_home_preview_type() == expect
                # data = self.page_get_add_billing_home_preview_type()
                # return data

            except Exception as e:
                # 截图 、日志
                self.base_get_img()
                log.error(e)
                # 抛异常
                raise
            finally:
                pass

        else:
            try:
                preview_type = self.page_get_add_billing_home_preview_type()
                print("获取错误的服务标题为：", preview_type)

            except Exception as e:
                # 截图 、日志
                self.base_get_img()
                log.error(e)
                # 抛异常
                raise

            finally:
                pass

    # 断言需求
    def page_assert_demand(self, demand):
        data = self.page_get_add_billing_home_preview_demand()
        # data = 2
        # print(data)
        if demand == data:
            try:
                preview_demand = self.page_get_add_billing_home_preview_demand()
                print("获取正确的需求为：", preview_demand)
                # self
                assert self.page_get_add_billing_home_preview_demand() == demand

            except Exception as e:
                # 截图 、日志
                self.base_get_img()
                log.error(e)
                # 抛异常
                raise
            finally:
                pass
        else:
            try:
                preview_demand = self.page_get_add_billing_home_preview_demand()
                print("获取的错误的需求为：", preview_demand)
                # self
                assert self.page_get_add_billing_home_preview_demand() == demand

            except Exception as e:
                # 截图 、日志
                self.base_get_img()
                log.error(e)
                # 抛异常
                raise
            finally:
                pass

    # 组合发单分页业务
    def page_add_billing_home_combination(self, search, money, demand, expect):
        self.base_click(page.add_billing_home_page)
        self.base_click(page.add_billing_home_location_search)
        # self.base_click(page.hair_btn_pos)
        sleep(1)
        self.base_input(page.add_billing_home_baidumap_search, search)
        self.base_click(page.add_billing_home_search_content)
        self.base_click(page.hair_btn_pos)
        self.base_click(page.add_billing_home_billing_time)
        sleep(1)
        self.base_input(page.add_billing_home_service_money, money)
        sleep(2)
        self.base_input(page.add_billing_home_demand, demand)
        self.base_click(page.add_billing_home_create_pay)
        self.page_assertion_preview_type(expect)
        self.page_assert_demand(demand)
        self.base_click(page.add_billing_home_preview_issue)
        self.driver.wait_activity(".ui.Activity_Splash", 2)
        self.base_click(page.hair_good)

    # 组合发单分页输入订单信息业务
    def page_add_recommendation_order(self, money, demand, ):
        self.base_click(page.hair_btn_pos)
        self.base_click(page.add_billing_home_billing_time)
        sleep(1)
        self.base_input(page.add_billing_home_service_money, money)
        sleep(2)
        self.base_input(page.add_billing_home_demand, demand)
        self.base_click(page.add_billing_home_create_pay)
        self.base_click(page.add_billing_home_preview_issue)
        self.driver.wait_activity(".ui.Activity_Splash", 2)
        self.base_click(page.hair_good)

    # 发单主页地图指定组合业务
    def page_hair_map_assignment(self, money, demand):
        self.base_click(page.hair_letter)
        self.base_click(page.add_billing_home_page)
        self.base_click(page.add_billing_home_use_location)
        self.base_click(page.hair_btn_pos)
        self.base_click(page.hair_designated_location)
        self.base_click(page.hair_menu_next)
        self.base_click(page.hair_choice_place_name)
        self.base_click(page.hair_map_use_location)
        self.base_click(page.add_skill_share_minute_charging)
        self.base_input(page.hair_service_input_box, money)
        self.base_input(page.hair_requirement_input_box, demand)
        self.base_click(page.hair_next_step)
        self.base_click(page.hair_publish_now)
        self.driver.wait_activity(".ui.Activity_Splash", 2)
        self.base_click(page.hair_good)

    # 挣钱主页按订单发单业务
    def page_earn_money_order(self, search):
        self.base_click(page.add_earn_money_homepage)
        self.base_click(page.add_earn_money_location_classification)
        self.driver.implicitly_wait(30)
        self.driver.tap([(41, 1061)])
        self.driver.implicitly_wait(30)
        # self.driver.wait_activity(".ui.Activity_Splash", 2)
        # self.base_click(page.add_earn_money_location_search_by_location)
        self.base_click(page.add_earn_money_location_site)
        self.driver.implicitly_wait(30)
        self.base_input(page.add_billing_home_baidumap_search, search)
        self.base_click(page.add_billing_home_search_content)

        self.base_click(page.hair_map_use_location)
        self.base_click(page.add_earn_money_location_classification)
        self.driver.implicitly_wait(30)
        self.driver.tap([(69, 375)])

    # 挣钱主页按订单发单业务
    def page_earn_money_order_u2(self, search):
        self.base_click(page.add_earn_money_homepage)
        self.base_click(page.add_earn_money_location_classification)
        self.driver.implicitly_wait(30)
        # self.driver.execute_script('arguments[0].click()', webElement)

        self.driver.tap([(41, 1061)])
        self.driver.implicitly_wait(30)
        self.base_click(page.add_earn_money_location_site)
        self.driver.implicitly_wait(30)
        self.base_input(page.add_billing_home_baidumap_search, search)
        self.base_click(page.add_billing_home_search_content)
        self.base_click(page.hair_map_use_location)
        self.base_click(page.add_earn_money_location_classification)
        self.driver.implicitly_wait(30)
        self.driver.tap([(69, 375)])
        # self.driver.implicitly_wait(10)

    # # 景区添加地点前置业务方法
    # def page_search_add_place(self, search):
    #     self.base_click(page.hair_letter)
    #     self.base_click(page.add_billing_home_page)
    #
    #
    #     self.base_input(page.position_manage_spot_search, search)
    #     self.base_click(page.position_manage_spot_add)
