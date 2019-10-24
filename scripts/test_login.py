import sys
import os
sys.path.append(os.getcwd())


import pytest

from page.page_login import PageLogin


def get_data():
    return [("itheimama","123456"),("itheima","1234567"),("itheima","123456")]


class TestLogin:
    # 初始化
    def setup_class(self):
        # 获取PageLogin对象
        self.login = PageLogin()
        # 点击 弹窗
        self.login.page_close_alert()
        # 点击 我
        self.login.page_click_me()
        # 点击 已有账号，去登录
        self.login.page_click_username_exists()

    # 结束
    def teardown_class(self):
        # 关闭 driver
        self.login.driver.quit()

    # 测试方法
    @pytest.mark.parametrize("username,pwd",get_data())
    def test_login(self, username, pwd):
        # 调用 登录组合业务方法
        self.login.page_login(username, pwd)