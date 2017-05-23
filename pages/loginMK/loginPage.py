# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
import xlrd
from pages.basePage import Page
from time import sleep
reload(sys)
sys.setdefaultencoding("utf-8")

class LoginPage(Page):
    ldgz_icon = u"//img[@src='images/ldgz.png']"     # 劳动改造   图标
    username_input = u"//*[@id='user']"     # 用户名   输入框
    password_input = u"//*[@id='password']"     # 用户密码   输入框
    login_btn = u"//*[@class='login_btn_login']"      # 登录   按钮

    # 读取xls中的值
    data = xlrd.open_workbook(u'D:\Test\POM_LDGZ_OLD\\textdata\登录管理.xls')
    table = data.sheet_by_name(u"登录")
    username = table.row(1)[0].value
    password = table.col(1)[1].value


    def __init__(self, driver, base_url=u"http://192.168.10.201:7001"):
        Page.__init__(self, driver, base_url)

    def openLDGZHomePage(self):
        print u"打开劳动改造首页：", self.base_url
        self.driver.get(self.base_url)

    def choose_mokuai_icon(self):
        print u"选择 劳动改造系统图标"
        self.choose_xt(self.ldgz_icon)

    def input_username(self):
        username = self.username
        print u"输入 用户名", username
        self.input_text(self.username_input, username)
        sleep(2)

    def input_password(self):
        password = self.password
        print u"输入 用户密码", password
        self.input_text(self.password_input, password)
        sleep(2)

    def click_login_btn(self):
        print u"点击 登陆 按钮"
        self.click(self.login_btn)
        sleep(5)
