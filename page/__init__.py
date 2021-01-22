from selenium.webdriver.common.by import By

"""以下为登录模块配置数据"""
# 手机号
login_phone = By.ID, "com.qjy.teleeye:id/et_reginster_phone_number"

# 密码
login_pwd = By.ID, "com.qjy.teleeye:id/et_reginster_phone_code"

# 登录按钮
login_btn = By.ID, "com.qjy.teleeye:id/tv_register_enter"

# 点击 同意并登陆
login_agree = By.ID, "com.qjy.teleeye:id/tv_home_dialog_ok"

#  点击 立即体验
login_now = By.ID, "com.qjy.teleeye:id/tv_go_app"

# 点击 	仅在使用中允许(定位)
login_location = By.XPATH, "//*[@text='仅在使用中允许'"

# 点击 “我” 主页
login_me = By.ID, "com.qjy.teleeye:id/iv_tabbar_me"

# 点击 立即登录
login_log_now = By.ID, "com.qjy.teleeye:id/tv_info_head_name"

# 点击 其他方式登录
login_login_other = By.ID, "com.qjy.teleeye:id/tv_chat_rests_login"

#  昵称
login_nickname = By.ID, "com.qjy.teleeye:id/tv_info_head_name"

# 点击 配置
login_setting = By.ID, "com.qjy.teleeye:id/tv_me_setting"

# 点击 点击退出登录
login_log_out = By.ID, "com.qjy.teleeye:id/rl_config_log_out"

# 点击 点击确认
login_confirm = By.ID, "com.qjy.teleeye:id/btn_pos"

# 点击 返回
login_sign_out = By.ID, "com.qjy.teleeye:id/iv_chat_back"

# 注册手机号
login_register_phone = By.ID, "com.qjy.teleeye:id/tv_register_phone_title"

# 点击 返回
login_register_phone_back = By.ID, "com.qjy.teleeye:id/tv_action_bar_menu_back"
"""以下为发单模块配置数据"""

# 点击 首页主页
hair_letter = By.ID, "com.qjy.teleeye:id/iv_tabbar_letter"

# 点击带看
hair_take_look = By.XPATH, '//*[@text="带看"]'

# 点击    大学
hair_university = By.XPATH, '//*[@text="16076590382858"]'

# 点击 校园生活
hair_run_shopping = By.XPATH, "//*[@text=找人带看']"

# 点击 跑腿代购
hair_view_single = By.ID, "com.qjy.teleeye:id/tv_adapter_helpleter_text"

# 点击 带看大学
hair_big_school = By.XPATH, '//*[@text="16076590382858"]'

# 点击地图指定
hair_university_map_assignment = By.XPATH, '//*[@text="15994817921857"]'

# 点击北京大学
hair_bj_university = By.XPATH, '//*[@text="北京大学"]'

# 点击清华大学
hair_qh_university = By.XPATH, "//*[@text='清华大学']"

# 点击 发布带看订单
hai_details_launch = By.XPATH, '//*[@resource-id="com.qjy.teleeye:id/tv_home_recommend_details_launch"]'

# 点击视频方式
hair_video = By.ID, "com.qjy.teleeye:id/rb_order_create_service_video"

# 输入 服务费
hair_service_input_box = By.ID, "com.qjy.teleeye:id/et_order_create_service_money"

# 输入 需求输入框	xpath
hair_requirement_input_box = By.ID, "com.qjy.teleeye:id/et_order_create_demand"

# 点击 下一步 id
hair_next_step = By.ID, "com.qjy.teleeye:id/tv_order_create_pay"

# 点击 立即发布 id
hair_publish_now = By.ID, "com.qjy.teleeye:id/tv_order_preview_issue"

# # 点击 好的 id
# hair_good = By.ID, "com.qjy.teleeye:id/tv_popup_order_ok"

# 点击 发单记录 id
hair_billing_record = By.ID, "com.qjy.teleeye:id/ll_me_info_bill"

# 点击订单查看详情（等待接单）
hair_billing_list = By.ID, "com.qjy.teleeye:id/tv_order_record_adapter_state"

# 点击 取消订单 id
hair_off_order = By.ID, "com.qjy.teleeye:id/tv_order_details_check_off"

# 等待接单
hair_waiting_for_order = By.XPATH, '//*[@text="等待接单"]'

# 对方已接单/未付款
hair_order_details_pay_no = By.XPATH, '//*[@text="对方已接单/未付款"]'

# 我要取消订单
hair_order_details_pay_noo = By.ID, "com.qjy.teleeye:id/tv_order_details_pay_no"

# 确定 id
hair_determine = By.ID, "com.qjy.teleeye:id/btn_pos"

# 返回 id （订单详情）
hair_return_order_details = By.ID, "com.qjy.teleeye:id/tv_order_details_back"

# 返回 id （发单记录）
hair_return_Billing_record = By.ID, "com.qjy.teleeye:id/tv_action_bar_menu_back"

# 指定位置
hair_designated_location = By.XPATH, '//*[@resource-id="com.qjy.teleeye:id/ll_order_create_type_location"]/android.widget.ImageView[1]'

# 选择城市
hair_menu_next = By.ID, "com.qjy.teleeye:id/tv_action_bar_menu_next"

# 选择地名
hair_choice_place_name = By.XPATH, '//*[@text="阿克塞哈萨克族自治县(甘肃省 酒泉市)"]'

# 使用该位置
hair_map_use_location = By.ID, "com.qjy.teleeye:id/tv_help_map_use_location"

# 疫情提示（知道了）
hair_btn_pos = By.ID, "com.qjy.teleeye:id/btn_pos"


"""以下为发服务模块配置数据"""

# 点击 添加技能和服务	id
add_skill_add_skills_services = By.ID, "com.qjy.teleeye:id/tv_me_info_add_skill"

# 输入服务标题
add_skill_service_description = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.widget.EditText[1]'

# 点击 按次计费
add_skill_share_second_charging = By.XPATH, '//*[@text="按次计费"]'

# 点击按分钟计费
add_skill_share_minute_charging = By.XPATH, '//*[@text="按分钟计费"]'

# 输入服务费
add_skill_service_money = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[3]/android.view.View[3]/android.widget.EditText[1]'

# 点击语音
add_skill_voice = By.XPATH, '//*[@text="语音"]'

# 点击视频
add_skill_video = By.XPATH, '//*[@text="视频"]'

# 输入服务介绍
add_skill_service_demand = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[5]/android.view.View[1]/android.widget.EditText[1]'

# 点击 发布服务
add_skill_service_issue = By.XPATH, '//*[@text="发布服务"]'

# 点击 我的服务   id
add_skill_service_text = By.ID, 'com.qjy.teleeye:id/iv_adapter_me_service_img'

# 点击技能列表	id
add_skill_skill_service_message_descriptions = By.XPATH, '//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[3]'

# 点击删除服务	id
add_skill_details_delete = By.XPATH, '//*[@text="删除服务"]'

# 点击确定		id
add_skill_btn_pos = By.XPATH, '//*[@text="确认"]'

# 点击返回		id
add_skill_menu_back = By.ID, "com.qjy.teleeye:id/tv_action_bar_menu_back"

# 获取服务标签
add_skill_category_title = By.XPATH, '//*[contains(@text(),"服务费：")]'

"""以下为发单分页元素模块配置数据"""

# 发单分页
add_billing_home_page = By.XPATH, '//*[@text="发单"]'

# 搜索
add_billing_home_location_search = By.ID, "com.qjy.teleeye:id/iv_help_map_location_search"

# 发订单，找此位置的人为我视频带看
add_billing_home_use_location = By.ID, "com.qjy.teleeye:id/tv_help_map_use_location"

# 搜索框（输入西二旗）
add_billing_home_baidumap_search = By.ID, "com.qjy.teleeye:id/et_baidumap_search"

# 西二旗（第一个搜索内容）
add_billing_home_search_content = By.XPATH, '//*[@resource-id="com.qjy.teleeye:id/lv_baidumap_search"]/android.widget.LinearLayout[1]'

# 按分钟计费
add_billing_home_billing_time = By.ID, 'com.qjy.teleeye:id/rb_order_create_billing_time'

# 服务费
add_billing_home_service_money = By.ID, "com.qjy.teleeye:id/et_order_create_service_money"

# 需求（西二旗带看）
add_billing_home_demand = By.ID, "com.qjy.teleeye:id/et_order_create_demand"

# 下一步
add_billing_home_create_pay = By.ID, "com.qjy.teleeye:id/tv_order_create_pay"

# 立即带看
add_billing_home_preview_issue = By.ID, "com.qjy.teleeye:id/tv_order_preview_issue"

# 断言标题（找人带看>西二旗-地铁站）
add_billing_home_preview_type = By.ID, "com.qjy.teleeye:id/tv_order_preview_type"

# 断言需求（西二旗带看）
add_billing_home_preview_demand = By.ID, "com.qjy.teleeye:id/tv_order_preview_demand"

# 立即发布
add_billing_home_order_preview_issue = By.ID, "com.qjy.teleeye:id/tv_order_preview_issue"

# 好的
add_billing_home_popup_order_ok = By.ID, "com.qjy.teleeye:id/tv_popup_order_ok"

"""以下为推荐分页元素模块配置数据"""

# 推荐分页
add_recommended_pagination = By.XPATH, '//*[@resource-id="com.qjy.teleeye:id/tab_action_bar"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.TextView[1]'

# 返回
add_recommended_pagination_return = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]'

# 发布带看订单
add_recommended_pagination_release_order = By.XPATH, '//*[@resource-id="com.qjy.teleeye:id/tv_home_recommend_details_launch"]'

"""以下为校园分页元素模块配置数据"""
# 校园分页
add_high_school = By.XPATH, '//*[@text="校园"]'

# “+”图标
add_high_school_icon = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[7]/android.view.View[1]/android.view.View[1]'

# 修改我的学校
add_high_school_modify = By.XPATH, '//*[@text = "修改我的学校"]'

# 发布带看订单
add_high_school_release_order_web = By.XPATH, '//*[@text = "发布带看订单"]'

# 搜索框
add_high_school_search_box = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[10]/android.view.View[1]/android.view.View[2]'

# 清华大学
add_high_school_qh = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[10]/android.view.View[2]/android.view.View[1]'

# 发布带看订单
add_high_school_release_order_android = By.XPATH, '//*[@resource-id="com.qjy.teleeye:id/tv_home_recommend_details_launch"]'

# 校园活动
add_high_school_campus_activities = By.XPATH, '//android.widget.Image'

# 高中投票
add_high_school_high_school_voting = By.XPATH, '//*[@text="gz.f7a4cf00"]'

# 大学投票
add_high_school_university_voting = By.XPATH, '//*[@text="dx_xz.0b052768"]'

# 学校 （上地学校）
add_high_school_shangdi = By.XPATH, '//*[@resource-id="app"]/android.view.View[3]/android.view.View[5]/android.view.View[1]/android.view.View[1]/android.view.View[1]'

# 八维学校
add_high_school_bawei = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[1]'

# 投上一票
add_high_school_vote_for_it = By.XPATH, '//*[@text="投上一票"]'

# 给母校发单
add_high_school_dear_school = By.XPATH, '//*[@text="给母校发单"]'

# 校园搜索框输入清华
add_high_school_search = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[10]/android.view.View[1]/android.view.View[2]/android.widget.EditText'

# 搜索清华
add_high_school_search_qh = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[10]/android.view.View[2]/android.view.View[1]'

# 查询修改后大学名称
add_high_school_after_modification = By.XPATH, '//*[@text="清华大学"]'

"""以下为推荐分页元素模块配置数据"""

# 家乡分页
add_hometown = By.XPATH, '//*[@text="家乡"]'

# 家乡活动
add_hometown_activity = By.XPATH, '//android.widget.Image'

# “+”号图标
add_hometown_icon = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[6]/android.view.View[1]/android.view.View[1]'

# 修改我的家乡
add_hometown_my = By.XPATH, '//*[@text = "修改我的家乡"]'

# 北京市
add_hometown_bj = By.XPATH, '//*[@resource-id = "app"]/android.view.View[1]/android.view.View[1]/android.view.View[8]/android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View[1]/android.view.View[5]'

# 市
add_hometown_city = By.XPATH, '//*[@text = "市"]'

# 市辖区
add_hometown_city_jurisdiction = By.XPATH, '//*[@resource-id = "app"]/android.view.View[1]/android.view.View[1]/android.view.View[8]/android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View[1]/android.view.View[3]'

# 区县
add_hometown_area_county = By.XPATH, '//*[@text = "区县"]'

# 朝阳区
add_hometown_chaoyang_district = By.XPATH, '// *[@resource-id = "app"]/android.view.View[1]/android.view.View[1]/android.view.View[8]/android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View[1]/android.view.View[3]'

# 乡镇
add_hometown_township = By.XPATH, '//*[@text = "乡镇"]'

# 奥运村街道
add_hometown_olympic_village_street = By.XPATH, '// *[@resource-id = "app"]/android.view.View[1]/android.view.View[1]/android.view.View[8]/android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View[1]/android.view.View[4]'

# 村 / 街道
add_hometown_village_street = By.XPATH, '//*[@text = "村/街道"]'

# 北沙滩社区
add_hometown_north_beach_community = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[8]/android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View[1]/android.view.View[3]'

# 选择此处为我的家乡
add_hometown_choose_here_as_my_hometown = By.XPATH, '//*[@text = "选择此处为我的家乡"]'

# 发布带看订单（web）
add_hometown_publish_with_order_web = By.XPATH, '//*[@text = "发布带看订单"]'

# 发布带看订单（安卓）
add_hometown_release_order_with_android = By.ID, "com.qjy.teleeye:id/tv_home_recommend_details_launch"

"""以下为挣钱主页元素模块配置数据"""

# 挣钱主页
add_earn_money_homepage = By.ID, "com.qjy.teleeye:id/iv_tabbar_money"

# 地点分类
add_earn_money_location_classification = By.ID, "com.qjy.teleeye:id/tv_make_money_site"

# 按位置搜索
add_earn_money_location_search_by_location = By.ID, "com.qjy.teleeye:id/tv_popup_make_site_location"

# 点击搜索
add_earn_money_location_site = By.ID, "com.qjy.teleeye:id/tv_help_map_location_site"

# 不限地点
add_earn_money_location_site_unlimited = By.ID, "com.qjy.teleeye:id/tv_popup_make_site_unlimited"

"""以下为位置管理元素模块配置数据"""

# 位置管理
position_manage = By.ID, "com.qjy.teleeye:id/tv_me_location_manage"

# 添加新的位置
position_manage_nuw = By.ID, "com.qjy.teleeye:id/bt_add_location"

# 修改已有地点信息
position_manage_modify = By.ID, "com.qjy.teleeye:id/bt_change_location"

# 我添加或修改的地点
position_manage_nuw_my = By.ID, "com.qjy.teleeye:id/bt_me_location"

# 返回
position_manage_back = By.ID, "com.qjy.teleeye:id/tv_action_bar_menu_back"

# 点击这里选择位置
position_manage_click_here = By.XPATH, '//*[@text="景点地址： 点击这里选择位置"]'

# 清空搜索框
position_manage_search_box_empty = By.XPATH, '//*[@text=""]'

# 搜索框     （输入西二旗）
position_manage_search_box = By.XPATH, '//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[2]'

# 搜索框外     （输入西二旗）
position_manage_search_box_out = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText"

# 点击搜索
position_manage_click_search = By.XPATH, '//*[@text="搜索"]'

# 点击第一个搜索内容
position_manage_click_first_search_content = By.XPATH, '//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]'

# 点击选择此位置
position_manage_choice_position = By.XPATH, '//*[@text="选择此位置"]'

# 点击这里选择位置类型
position_manage_position_type = By.XPATH, '//*[@text="点击这里选择位置类型"]'

# 点击景区
position_manage_scenic_spot = By.XPATH, '//*[@text="景区"]'

# 从相册选取
position_manage_photo = By.ID, "com.qjy.teleeye:id/bt_addimage_photo"

# 位置管理
position_manage_file_management = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView'

# 相册
position_manage_album = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView'

# qq图片
position_manage_qq_picture = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout'

# qq浏览器第一张图片
position_manage_one_picture = By.XPATH, '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[3]/android.widget.FrameLayout[2]/android.view.View[1]'

# 点击这里输入针对这个位置的描述
position_manage_click_describe = By.XPATH, '//*[@text="点击这里输入针对这个位置的描述"]'

# 选择图片
position_manage_select_picture = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.view.View"

# 选择图片
position_manage_select_picture2 = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View"

# 输入描述信息（北京西二旗地铁站123）
position_manage_describe_information = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[5]/android.view.View[2]/android.widget.EditText'

# 点击保存
position_manage_preservation = By.XPATH, '//*[@text="保存"]'

# 点击创建位置信息
position_manage_found_position_information = By.XPATH, '//*[@text="创建位置信息"]'

# 点击删除
position_manage_delete = By.XPATH, '//*[@text="删除"]'

# 点击5A景区
position_manage_5a = By.XPATH, '//*[@text="景区"]'

# 北京颐和园
position_manage_bj_summer_palace = By.XPATH, '//*[@text="北京颐和园"]'

# 输入您的姓名
position_manage_name = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.widget.EditText'

# 输入联系方式
position_manage_phone = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.widget.EditText'

# 地点经营者
position_manage_location_operator = By.XPATH, '//*[@text="地点经营者"]'

# 备注
position_manage_remarks = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[5]/android.view.View[2]/android.widget.EditText'

# 提交
position_manage_submit = By.XPATH, '//*[@text="提交"]'
