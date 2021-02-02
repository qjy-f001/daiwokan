from time import sleep

import page
from base.base import Base


class PagePositionAdminister(Base):
    # 位置管理
    def page_click_position_manage(self):
        self.base_click(page.position_manage)

    # 添加新的位置
    def page_click_position_manage_nuw(self):
        self.base_click(page.position_manage_nuw)

    # 修改已有地点信息
    def page_click_position_manage_modify(self):
        self.base_click(page.position_manage_modify)

    # 我添加或修改的地点
    def page_click_position_manage_nuw_my(self):
        self.base_click(page.position_manage_nuw_my)

    # 返回
    def page_click_position_manage_back(self):
        self.base_click(page.position_manage_back)

    # 点击这里选择位置
    def page_click_position_manage_click_here(self):
        self.base_click(page.position_manage_click_here)

    # 搜索框     （输入西二旗）
    def page_click_position_manage_search_bo(self):
        self.base_click(page.position_manage_search_box)

    # 清空搜索框
    def page_click_position_manage_search_box_empty(self):
        self.base_click(page.position_manage_search_box_empty)

    # 搜索框外     （输入西二旗）
    def page_input_position_manage_search_box_out(self, search):
        self.base_input(page.position_manage_search_box_out, search)

    # 搜索框     （输入西二旗）
    def page_input_position_manage_search_box(self, search):
        self.base_input(page.position_manage_search_box, search)

    # 点击搜索
    def page_click_position_manage_click_search(self):
        self.base_click(page.position_manage_click_search)

    # 点击第一个搜索内容
    def page_click_position_manage_click_first_search_content(self):
        self.base_click(page.position_manage_click_first_search_content)

    # 点击选择此位置
    def page_click_position_manage_choice_position(self):
        self.base_click(page.position_manage_choice_position)

    # 点击这里选择位置类型
    def page_click_position_manage_position_type(self):
        self.base_click(page.position_manage_position_type)

    # 点击景区
    def page_click_position_manage_scenic_spot(self):
        self.base_click(page.position_manage_scenic_spot)

    # 点击这里输入针对这个位置的描述
    def page_click_position_manage_click_describe(self):
        self.base_click(page.position_manage_click_describe)

    # 选择图片
    def page_click_position_manage_select_picture(self):
        self.base_click(page.position_manage_select_picture)

    # 从相册选取
    def page_click_position_manage_photo(self):
        self.base_click(page.position_manage_photo)

    # 位置管理
    def page_click_position_manage_file_management(self):
        self.base_click(page.position_manage_file_management)

    # 相册
    def page_click_position_manage_album(self):
        self.base_click(page.position_manage_album)

    # qq图片
    def page_click_position_manage_qq_picture(self):
        self.base_click(page.position_manage_qq_picture)

    # qq浏览器第一张图片
    def page_click_position_manage_one_picture(self):
        self.base_click(page.position_manage_one_picture)

    # 输入描述信息（北京西二旗地铁站123）
    def page_click_position_manage_describe_information(self, describe):
        self.base_input(page.position_manage_describe_information, describe)

    # 点击保存
    def page_click_position_manage_preservation(self):
        self.base_click(page.position_manage_preservation)

    # 点击创建位置信息
    def page_click_position_manage_found_position_information(self):
        self.base_click(page.position_manage_found_position_information)

    # 点击删除
    def page_click_position_manage_delete(self):
        self.base_click(page.position_manage_delete)

    # 点击5A景区
    def page_click_position_manage_5a(self):
        self.base_click(page.position_manage_5a)

    # 北京颐和园
    def page_click_position_manage_bj_summer_palace(self):
        self.base_click(page.position_manage_bj_summer_palace)

    # 输入您的姓名
    def page_input_position_manage_name(self, name):
        self.base_input(page.position_manage_name, name)

    def page_input_position_manage_phone(self, phone):
        self.base_input(page.position_manage_phone, phone)

    # 地点经营者
    def page_click_position_manage_location_operator(self):
        self.base_click(page.position_manage_location_operator)

    # 备注
    def page_input_position_manage_remarks(self, remarks):
        self.base_input(page.position_manage_remarks, remarks)

    # 提交
    def page_click_position_manage_submit(self):
        self.base_click(page.position_manage_submit)

    # 景区搜索框
    def page_click_position_manage_spot_search(self, search):
        self.base_input(page.position_manage_spot_search, search)

    # 景区添加景点
    def page_click_position_manage_spot_add(self):
        self.base_click(page.position_manage_spot_add)

    # 点击返回
    # 点击返回

    # 组合添加景点并删除业务方法
    def page_position_manage_nuw_position(self, search, describe):
        self.base_click(page.position_manage_nuw)
        self.base_click(page.position_manage_click_here)
        self.base_click(page.position_manage_search_box)
        self.base_click(page.position_manage_search_box_empty)
        sleep(2)
        self.base_input(page.position_manage_search_box_out, search)
        self.base_click(page.position_manage_click_search)
        self.base_click(page.position_manage_click_first_search_content)
        self.base_click(page.position_manage_choice_position)
        self.base_click(page.position_manage_position_type)
        self.base_click(page.position_manage_scenic_spot)
        self.driver.tap([(44, 979)])
        sleep(2)
        self.base_input(page.position_manage_describe_information, describe)
        self.page_select_picture()
        self.base_click(page.position_manage_found_position_information)
        self.base_click(page.position_manage_back)
        self.base_click(page.position_manage_nuw_my)
        self.base_click(page.position_manage_delete)
        sleep(1)
        self.base_click(page.position_manage_back)
        sleep(1)
        self.base_click(page.position_manage_back)

    # 组合添加图片业务方法（没有权限）
    def page_select_picture(self):
        self.base_click(page.position_manage_select_picture)
        sleep(1)
        self.driver.tap([(80, 1990)])
        sleep(1)
        self.driver.tap([(80, 1990)])
        # self.base_click(page.position_manage_select_picture)
        self.base_click(page.position_manage_photo)
        self.base_click(page.position_manage_file_management)
        self.base_click(page.position_manage_album)
        self.base_click(page.position_manage_qq_picture)
        self.base_click(page.position_manage_one_picture)

    # 组合添加图片业务方法（有权限）
    def page_select_picture_no(self):
        self.base_click(page.position_manage_select_picture2)
        # self.driver.tap([(80, 1990)])
        # self.driver.tap([(80, 1990)])
        # self.base_click(page.position_manage_select_picture)
        self.base_click(page.position_manage_photo)
        self.base_click(page.position_manage_file_management)
        self.base_click(page.position_manage_album)
        self.base_click(page.position_manage_qq_picture)
        self.base_click(page.position_manage_one_picture)

    # 修改已有景区业务方法
    def page_click_modify_existing_location_information(self, name, phone, remarks):
        self.base_click(page.position_manage_modify)
        self.base_click(page.position_manage_5a)
        self.base_click(page.position_manage_bj_summer_palace)
        self.base_input(page.position_manage_name, name)
        self.base_input(page.position_manage_phone, phone)
        self.base_click(page.position_manage_location_operator)
        self.base_input(page.position_manage_remarks, remarks)
        self.page_select_picture_no()
        self.base_click(page.position_manage_submit)

    # 景区添加地点业务方法
    def page_add_unknown_scenic_spot(self, search, search1, describe):
        self.base_input(page.position_manage_spot_search, search)
        self.base_click(page.position_manage_spot_add)
        self.base_click(page.position_manage_click_here)
        self.base_click(page.position_manage_search_box)
        self.base_click(page.position_manage_search_box_empty)
        sleep(2)
        self.base_input(page.position_manage_search_box_out, search1)
        self.base_click(page.position_manage_click_search)
        self.base_click(page.position_manage_click_first_search_content)
        self.base_click(page.position_manage_choice_position)
        self.base_input(page.position_manage_describe_information, describe)
        # 添加图片（有权限）
        self.page_select_picture_no()
        self.base_click(page.position_manage_found_position_information)
        self.base_click(page.position_manage_back)

    # 景区删除新增地点业务方法
    def page_delete_position_manage_nuw_my(self):
        self.base_click(page.position_manage_nuw_my)
        self.base_click(page.position_manage_delete)
        sleep(1)
        self.base_click(page.position_manage_back)
        sleep(1)
        self.base_click(page.position_manage_back)

        # self.base_click(page.position_manage_nuw_my)
        # self.base_click(page.position_manage_delete)
        # # 添加选择位置类型
        # self.base_click(page.position_manage_scenic_spot)
        # 添加图片
        # self.base_click(page.position_manage_select_picture2)
        # self.driver.tap([(80, 1990)])
        # self.driver.tap([(80, 1990)])
        # # self.base_click(page.position_manage_select_picture)
        # self.base_click(page.position_manage_photo)
        # self.base_click(page.position_manage_file_management)
        # self.base_click(page.position_manage_album)
        # self.base_click(page.position_manage_qq_picture)
        # self.base_click(page.position_manage_one_picture)
