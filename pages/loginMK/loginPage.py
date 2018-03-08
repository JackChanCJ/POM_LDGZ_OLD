# coding=utf-8
__author__ = 'JACK_CHAN'

import unittest
from time import sleep
from pages.basePage import Page

class LoginPage(Page, unittest.TestCase):
    ldgz_icon_xp = u"//img[@src='images/ldgz.png']"  # 劳动改造   图标
    username_xp = u"//*[@id='user']"  # 用户名   输入框
    password_xp = u"//*[@id='password']"  # 用户密码   输入框
    login_btn_xp = u"//*[@class='login_btn_login']"  # 登录   按钮
    logout_btn_xp = u"html/body/div[3]/div[1]"  # 注销    按钮

    def __init__(self, driver):
        Page.__init__(self, driver)

    def open_url(self):
        self.driver.get(self.base_url)
        print u"打开劳动改造首页:  ", self.base_url

    def choose_module_ldgz(self):
        self.choose_xt(self.ldgz_icon_xp)
        print u"选择图标  劳动改造"

    def input_username(self, username):
        self.input_text(self.username_xp).send_keys(username)
        print u"输入  用户名", username
        sleep(2)

    def input_password(self, password):
        self.password = password
        self.input_text(self.password_xp).send_keys(password)
        print u"输入  用户密码", password
        sleep(2)

    def click_login_btn(self):
        self.click_btn(self.login_btn_xp)
        print u"点击  登陆  按钮"
        sleep(5)

    # 注销并退出
    def log_out(self):
        print u"\n注销  退出系统"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('topFrame')
        self.click_btn(self.logout_btn_xp)
        sleep(1)
        al = self.driver.switch_to.alert
        print u"弹出框:  ", al.text
        al.accept()
        print u"确定"
        sleep(2)













