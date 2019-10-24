"""
    方法:
        1. 根据操作步骤，将每步操作单独封装成一个方法，根据需求组合业务方法
        2. 组合业务方法：将1个页面中所有操作，组合；
"""
import page
from base.base import Base


class PageLogin(Base):
    # 关闭 弹窗
    def page_close_alert(self):
        self.base_click(page.login_close_alert)

    # 点击 我
    def page_click_me(self):
        self.base_click(page.login_me)

    # 点击 已有账号，去登录
    def page_click_username_exists(self):
        self.base_click(page.login_username_exists)

    # 输入 用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入 密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击 登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 组合业务方法
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()