# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
import textdata
import unittest
from openpyxl import Workbook
from openpyxl import load_workbook
from time import sleep
from selenium.webdriver.common.keys import Keys
from pages.basePage import Page


reload(sys)
sys.setdefaultencoding("utf-8")

class LoginPage(Page, unittest.TestCase):
    ldgz_icon = u"//img[@src='images/ldgz.png']"     # 劳动改造   图标
    username_input = u"//*[@id='user']"     # 用户名   输入框
    password_input = u"//*[@id='password']"     # 用户密码   输入框
    login_btn = u"//*[@class='login_btn_login']"      # 登录   按钮
    logout_btn = u"html/body/div[3]/div[1]"                #注销    按钮

    filename = u'D:\\Test\\POM_LDGZ_OLD\\textdata\\登录管理.xlsx'
    # filename = u"D:\\01____WorkStation\PYTHON\\POM_LDGZ_OLD\\textdata\\登录管理.xlsx"

    def __init__(self, driver):
        Page.__init__(self, driver)

    def openLDGZHomePage(self):
        print u"打开劳动改造首页:  ", self.base_url
        self.driver.get(self.base_url)

    def choose_module_icon(self):
        print u"选择  劳动改造系统图标"
        self.choose_xt(self.ldgz_icon)

    def input_username(self, username):
        self.username = username
        self.input_text(self.username_input).send_keys(username)
        print u"输入  用户名", username
        sleep(2)

    def input_password(self, password):
        self.password = password
        self.input_text(self.password_input).send_keys(password)
        print u"输入  用户密码", password
        sleep(2)

    def input_username_parameter(self, data):
        self.data = data
        username = self.username
        print u"输入  用户名", username
        self.input_text(self.username_input, username)
        sleep(2)

    def input_password_parameter(self, data):
        self.data = data
        password = self.password
        print u"输入  用户密码", password
        self.input_text(self.password_input, password)
        sleep(2)

    def click_login_btn(self):
        print u"点击  登陆  按钮"
        self.click(self.login_btn)
        sleep(5)

    # 注销并退出
    def log_out(self):
        print
        print u"注销  退出系统"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('topFrame')
        self.click(self.logout_btn)
        sleep(1)
        al = self.driver.switch_to.alert
        print u"弹出框:  ", al.text
        al.accept()
        print u"确定"
        sleep(2)

    # 登录并进入首页
    def log_in(self):
        print u"登录并进入首页"
        # 启动浏览器，访问劳动改造地址
        self.openLDGZHomePage()

        self.choose_module_icon()

        self.input_username()

        self.input_password()

        self.click_login_btn()

        # print u"验证标题"
        # sec = u"全国监狱信息化管理平台V3.0"
        # fst = self.driver.title
        # self.assertEqual(fst, sec)












