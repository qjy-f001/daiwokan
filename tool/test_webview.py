from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

caps = {}
# 必填-且正确
caps['platformName'] = 'Android'
# 必填-且正确
# caps['platformVersion'] = '10'
caps['platformVersion'] = '5.1.1'
# 必填
# caps['deviceName'] = '10826625'
caps['deviceName'] = '127.0.0.1.61001'
# toast
caps['automationName'] = 'Uiautomator2'
# APP包名 /
caps['appPackage'] = 'com.tencent.news'
# 中文
caps['unicodeKeyboard'] = True
caps['resetKeyboard'] = True
# 启动名 # /
caps['appActivity'] = 'activity.SplashActivity'
# 获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
# 当前环境
print("当前环境：", driver.context)
print("当前所有环境：", driver.contexts)
# 隐式等待
driver.implicitly_wait(30)
# 新闻
driver.find_element_by_xpath("//*[contains(@text,'同意并进入')]").click()
# driver.find_element_by_xpath("//*[contains(@text,'仅在使用中')]").click()
driver.find_element_by_xpath("//*[contains(@text,'习近平为何')]").click()
print("点击后所有环境：", driver.contexts)
driver.find_element_by_xpath("//*[contains(@text,'第一观察')]").click()
sleep(2)
driver.swipe(500, 200, 500, 800, duration=3000)
driver.find_element_by_xpath("//*[contains(@text,'时隔四年')]").click()
test = (MobileBy.XPATH, "//*[contains(@text,'时隔四年')]").clkck()

# 点击后所有环境
print("点击后所有环境：", driver.contexts)
# 切换环境 selenium环境
# driver.switch_to.context("WEBVIEW_com.tencent.news")
# result = driver.find_element_by_css_selector("p").text
# print(result)
