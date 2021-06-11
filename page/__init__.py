from selenium.webdriver.common.by import By

# from appium.webdriver.common.mobileby import MobileBy

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
login_location = By.XPATH, "//*[@text='仅在使用中允许']"

# 点击 “我” 主页
login_me = By.ID, "com.qjy.teleeye:id/iv_tabbar_me"

# 点击 立即登录
login_log_now = By.ID, "com.qjy.teleeye:id/tv_info_head_name"

# 点击 其他方式登录
login_login_other = By.ID, "com.qjy.teleeye:id/tv_chat_rests_login"

#  昵称
login_nickname = By.ID, "com.qjy.teleeye:id/tv_info_head_name"

# 点击 配置
login_setting = By.ID, "com.qjy.teleeye:id/iv_info_user_setting"

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
hair_take_look = By.XPATH, '//*[@text="分类"]'

# 点击    大学
hair_university = By.XPATH, '//*[@text="16076590382858"]'

# 点击 校园生活
hair_run_shopping = By.XPATH, "//*[@text=找人带看']"

# 点击 跑腿代购
hair_view_single = By.ID, "com.qjy.teleeye:id/tv_adapter_helpleter_text"

# 点击 带看大学
hair_big_school = By.XPATH, '//*[@text="大学"]'

# 点击地图指定
hair_university_map_assignment = By.XPATH, '//*[@text="15994817921857"]'

# 点击北京大学
hair_bj_university = By.XPATH, '//*[@text="北京大学"]'

# 点击清华大学
hair_qh_university = By.XPATH, "//*[@text='清华大学']"

# 点击 发布带看订单
hai_details_launch = By.XPATH, '//*[@text="带我看"]'

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
hair_good = By.ID, "com.qjy.teleeye:id/tv_popup_order_ok"

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

# 取消
hair_order_details_pay_noo = By.ID, "com.qjy.teleeye:id/tv_order_details_over_order"

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
# hair_btn_pos = By.ID, "com.qjy.teleeye:id/btn_pos"

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

# 服务主页
add_skill_category_help = By.ID, "com.qjy.teleeye:id/iv_tabbar_help"

# 服务
add_skill_list_first = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]'

# 111111111111111111111111111111111111

# 头像
add_skill_head_portrait = By.ID, "com.qjy.teleeye:id/iv_seek_help_details_head"

# 个人技能
add_skill_personal_person = By.ID, "com.qjy.teleeye:id/rb_personal_person"

# 技能服务
add_skill_personal_skill = By.ID, "com.qjy.teleeye:id/rb_personal_skill"

add_skill_query_service_list_skill_name = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout'
# 查询服务列表技能名称

# 他的技能服务
add_skill_skills_services = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout'

# 查询服务列表技能服务介绍
add_skill_query_service_list_skill_introduce = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[3]'

# 查询技能标题
add_skill_personal_skill_adapter_title = By.ID, "com.qjy.teleeye:id/tv_personal_skill_adapter_title"

# 服务介绍
add_skill_personal_skill_adapter_demand = By.ID, "com.qjy.teleeye:id/tv_personal_skill_adapter_demand"

# 11111111111111111111111111111111111111

# 立即下单
add_skill_order_now = By.ID, "com.qjy.teleeye:id/tv_seekhelp_place"

# 支付服务费
add_skill_order_payment = By.ID, "com.qjy.teleeye:id/tv_seekhelp_create_pay"

# 选择支付宝支付
add_skill_order_payment_ali = By.ID, "com.qjy.teleeye:id/rb_popup_play_ali"

# 取消订单
add_skill_order_payment_cancel = By.ID, "com.qjy.teleeye:id/tv_popup_play_cancel"

"""以下为发单分页元素模块配置数据"""

# 发单分页
add_billing_home_page = By.XPATH, '//*[@text="带看"]'

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
add_recommended_pagination = By.XPATH, '//*[@text="推荐"]'

# 返回
add_recommended_pagination_return = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]'

# 点击推荐分页地点名称
add_recommended_pagination_name = By.XPATH, "/hierarchy//android.widget.Image"

# 发布带看订单
add_recommended_pagination_release_order = By.XPATH, '//*[@text="带我看"]'

"""以下为校园分页元素模块配置数据"""
# 校园分页
add_high_school = By.XPATH, '//*[@text="校园"]'

# “+”图标
add_high_school_icon = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.widget.Image[1]'

# 修改我的学校
add_high_school_modify = By.XPATH, '//*[@text = "修改我的学校"]'

# 发布带看订单
add_high_school_release_order_web = By.XPATH, '//*[@text = "发布带看订单"]'

# 搜索框
add_high_school_search_box = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[13]/android.view.View[1]'

# 清华大学
add_high_school_qh = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[10]/android.view.View[2]/android.view.View[1]'

# 发布带看订单
add_high_school_release_order_android = By.XPATH, '//*[@text="带我看"]'

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
add_high_school_search = By.XPATH, '/hierarchy//android.view.View[6]//android.widget.EditText'

# 搜索清华
add_high_school_search_qh = By.XPATH, '/hierarchy//android.view.View[6]/android.view.View[2]/android.view.View[1]'

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
add_hometown_my = By.XPATH, '//*[@text=""]'

# 全国
add_hometown_whole_country = By.XPATH, '//*[@text="全国"]'

# 北京市
add_hometown_bj = By.XPATH, '//*[@text="北京市"]'

# 市
# add_hometown_city = By.XPATH, '//*[@text="市辖区"]'

# 市辖区
add_hometown_city_jurisdiction = By.XPATH, '//*[@text="市辖区"]'

# 区县
# add_hometown_area_county = By.XPATH, '//*[@text = "区县"]'

# 东城区
add_hometown_dongcheng_district = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[2]'

# 东华门街道
add_hometown_township = By.XPATH, '//*[@text="东华门街道"]'

# 多福巷社区
add_hometown_olympic_village_street = By.XPATH, '//*[@text="多福巷社区"]'

# # 村 / 街道
# add_hometown_village_street = By.XPATH, '//*[@text = "村/街道"]'

# # 北沙滩社区
# add_hometown_north_beach_community = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[8]/android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View[1]/android.view.View[3]'


# 市辖区					//*[@text="市辖区"]
#
#
# 东城区					//*[@text="东城区"]
#
#
# 东华门街道				//*[@text="东华门街道"]
#
#
# 多福巷社区				//*[@text="多福巷社区"]
#
#
# 多福巷社区（确认）		//*[@resource-id="app"]/android.view.View[4]/android.view.View[1]
#
#
# 选为我的家乡			//android.widget.Image


# 选择此处为我的家乡
add_hometown_choose_here_as_my_hometown = By.XPATH, '//*[@resource-id="app"]/android.view.View[5]'

# 发布带看订单（web）
add_hometown_publish_with_order_web = By.XPATH, '//*[@text="带我看"]'

# 发布带看订单（安卓）
add_hometown_release_order_with_android = By.ID, "com.qjy.teleeye:id/tv_home_recommend_details_launch"

# 家乡动态元素id-------------------------------------

# 店铺转让
add_hometown_shop_transfer = By.XPATH, '//*[@text="店铺转让"]'

# 发布按钮
add_hometown_publish_button = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.widget.Image[1]'

# 转让 店铺/生意（未发布过动态信息时显示）
add_hometown_transfer_shop = By.XPATH, '/hierarchy//android.view.View[4]'

# 选择店铺类型
add_hometown_select_store_type = By.XPATH, '//*[@text="选择店铺类型"]'

# 店铺类型：写字楼
add_hometown_office_building = By.XPATH, '//*[@text="写字楼"]'

# 点击选好了
add_hometown_dynamic_yes = By.XPATH, '//*[@text="选好了"]'

# 输入标题选项
add_hometown_title_options = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.EditText'

# 填写转让店铺信息/原因
add_hometown_information_transfer = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.widget.EditText'

# 选择上传图片/视频
add_hometown_up_image = By.XPATH, '//*[@text="图片/视频"]'

# 拍一张
add_hometown_take_a_picture = By.XPATH, '//*[@text="拍一张"]'

# 相机
add_hometown_camera = By.XPATH, '//*[@text="相机"]'

# 拍摄
add_hometown_shot = By.ID, "com.android.camera:id/shutter_button_horizontal"

# 确认图片
add_hometown_ok_picture = By.ID, "com.android.camera:id/done_button"

# 点击图片
add_hometown_up_picture = By.XPATH, '//*[@resource-id="com.qjy.teleeye:id/bt_addimage_photo"]'

# 点击图片
add_hometown_choice_picture = By.XPATH, '//*[@resource-id="com.qjy.teleeye:id/mRecyclerView"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'

# 输入面积
add_hometown_input_area = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[3]/android.widget.EditText'

# 输入转让费
add_hometown_input_charge = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[7]/android.view.View[2]/android.widget.EditText'

# 选择经营行业
add_hometown_business = By.XPATH, '//*[@text="经营行业"]'

# 餐饮美食
add_hometown_beverage = By.XPATH, '//*[@text="餐饮美食"]'

# 食堂
add_hometown_canteen = By.XPATH, '//*[@text="食堂"]'

# 完成
add_hometown_complete = By.XPATH, '//*[@text="完成"]'

# 输入电话
add_hometown_input_phone = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[9]/android.view.View[1]/android.widget.EditText'

# 提交
add_hometown_submit = By.XPATH, '//*[@text="提交"]'

# 我的发布
add_hometown_personal_center = By.XPATH, '//*[@text="我的发布"]'

# 多选按钮
add_hometown_multiple_choice_button = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]'

# 删除动态
add_hometown_delete_dynamic = By.XPATH, '//*[@text="个人中心"]/android.view.View[2]'

# 退出
add_hometown_sign_out = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]'

# --------------
# 资讯
add_hometown_dynamic = By.XPATH, '//*[@text="资讯"]'

# 111
add_hometown_dynamic_details = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]'

# 资讯详情
add_hometown_information_details = By.XPATH, '//*[@text="资讯详情"]'

# 收藏
add_hometown_collection = By.XPATH, '//body//div//p[@class="footer-collection"]'

# add_hometown_collection = By.XPATH, '//*[contains(@text,"收藏")]'
# add_hometown_collection = (MobileBy.XPATH, "//*[contains(@text,'收藏')]")

# 关注
add_hometown_information_collect = By.ID, 'com.qjy.teleeye:id/ll_info_collect_manage'

add_hometown_information_zx = By.XPATH, '//body//div[@class="van-tabs__content"]'

# 取消收藏
add_hometown_cancel_collection = By.XPATH, '/html/body/van-number-keyboard/div/div/div/div[2]/p[2]/span'

# 退出
add_hometown_information_exit = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]'

# --------------------------------------
# 本地好店
home_shop = By.XPATH, '//*[@text="本地好店"]'

# 发布
home_shop_release = By.XPATH, '//*[@text="立即免费开店"]'

# 商户名称
home_trade_name = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.EditText'

# 店铺介绍
home_shop_introduction = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[6]/android.view.View[2]/android.widget.EditText[1]'

# 经营类别
home_business_category = By.XPATH, '//*[@text="请正确选择>"]'

# 小吃店
home_business_snack_bar = By.XPATH, '//*[@text="小吃店"]'

# 完成
home_business_complete = By.XPATH, '//*[@text="完成"]'

# 地址
home_shop_address = By.XPATH, '//*[@text="定位并选择>"]'

# 商户电话（选填)
home_merchant_telephone = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[9]/android.view.View[2]'

# 我的店铺
home_my_stores = By.XPATH, '//*[@text="我的店铺"]'

# 删除店铺
home_dle_stores = By.XPATH, '//*[@text="删除"]'

# 商品管理
home_stores_administration = By.XPATH, '//*[@text="商品管理"]'

# 商品
home_commodity = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]'

# 发布按钮
home_commodity_release = By.XPATH, '//*[@text="发布"]'

#
home_commodity_signout = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[2]/android.view.View[1]'
# 家乡风景--------------------------

# 发布+
home_release = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.widget.Image[1]'

# 家乡风景
home_scenery = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View/android.widget.Image'

# 发布家乡风景
home_release_scenery = By.XPATH, '//*[@text="发布家乡风景"]'

# 选择图片
home_picture_video = By.XPATH, '//*[@text="图片/视频"]'

# 选照片
home_choose_photo = By.XPATH, '//*[@text="选照片"]'


# 选择图片
home_choice_picture = By.XPATH, '//*[@resource-id="com.qjy.teleeye:id/mRecyclerView"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.CheckBox[1]'

# 完成
home_complete = By.XPATH, '//*[@resource-id="com.qjy.teleeye:id/tv_rightBtn"]'

# 输入动图信息
home_input_dynamic_information = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.EditText'

# 输入描述
home_input_describe = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.widget.EditText'

# 发布
home_dynamic_release = By.XPATH, '//*[@text="提交"]'

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
position_manage_search_box_out = By.XPATH, "/hierarchy/android.widget.FrameLayout//android.widget.EditText"

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

# 位置管理添加图片
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
position_manage_select_picture = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.view.View"
# 选择图片

position_manage_select_picture2 = By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.view.View"

# 输入描述信息（北京西二旗地铁站123）
position_manage_describe_information = By.XPATH, '/hierarchy/android.widget.FrameLayout//android.widget.EditText'

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

# 景区搜索框
position_manage_spot_search = By.ID, "com.qjy.teleeye:id/et_spot_search"

# 景区添加暂无景点
position_manage_spot_add = By.ID, "com.qjy.teleeye:id/tv_spot_add"

# 景区添加新的景点
position_manage_spot_add_nuw = "com.qjy.teleeye:id/tv_action_bar_menu_next"

"""以下为聊天元素模块配置数据"""

# 消息主页
chat = By.ID, "com.qjy.teleeye:id/iv_tabbar_goods"

# 第一条通话信息
chat_information = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[5]'

# 用户头像
chat_portrait = By.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Image[1]'
# 聊一聊
chat_have_a_chat = By.XPATH, '//*[@text="聊一聊"]'

# resource-id
# com.qjy.teleeye:id/tv_action_bar_menu_back
#
# resource-id
# com.qjy.teleeye:id/tv_action_bar_menu_back
#
# resource-id
# com.qjy.teleeye:id/tv_action_bar_menu_back
