from appium import webdriver
import page


class GetDriver:
    driver = None
    package = page.app_appPackage
    activity = page.app_appActivity
    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 定义空字典
            desired_caps = {}
            # 指定平台名称 必须写对
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            # 不能为空，可以随便写
            desired_caps['deviceName'] = 'emulator-5554'
            # 包名/
            desired_caps['appPackage'] = GetDriver.package
            # 启动名
            desired_caps['appActivity'] = GetDriver.activity
            # 中文
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # 声明⼿机驱动对象
            cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls.driver

    # 关闭driver
    @classmethod
    def close_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 必须置空 大坑
            cls.driver = None

if __name__ == '__main__':
    print(GetDriver.get_driver())
    GetDriver.close_driver()
    print(GetDriver.get_driver())