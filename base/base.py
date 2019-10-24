"""
    类名：以大驼峰形式将模块名抄进来，有下划线，去掉下划线
    方法：
        1. 去分析要实现的用例步骤，将步骤公共方法抽取出来；
        2. 命名：base_+实意单词
"""
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化->driver
    def __init__(self):
        # 定义空字典
        desired_caps = {}
        # 指定平台名称 必须写对
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        # 不能为空，可以随便写
        desired_caps['deviceName'] = 'emulator-5554'
        # 包名/
        desired_caps['appPackage'] = 'com.yunmall.lc'
        # 启动名
        desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
        # 中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明⼿机驱动对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 隐式等待
        self.driver.implicitly_wait(10)

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        # loc 为元组或列表
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击
    def base_click(self, loc):
        # 调用查找元素
        self.base_find(loc).click()

    # 输入
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)
