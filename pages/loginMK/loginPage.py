# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
from pages.basePage import Page
from time import sleep
reload(sys)
sys.setdefaultencoding("utf-8")

class LoginPage(Page):
    ldgz_icon = u"//img[@src='images/ldgz.png']"     #劳动改造图标
    username_input = u"//*[@id='user']"     #用户名 输入框
    password_input = u"//*[@id='password']"     #用户密码 输入框
    login_btn = u"//*[@class='login_btn_login']"      #登录 按钮

    def __init__(self, driver, base_url=u"http://192.168.10.201:7001"):
        Page.__init__(self, driver, base_url)

    def openLDGZHomePage(self):
        print u"打开劳动改造首页：", self.base_url
        self.driver.get(self.base_url)

    def choose_mokuai_icon(self):
        print u"选择 劳动改造系统图标"
        self.choose_xt(self.ldgz_icon)

    def input_username(self, text="999999"):
        print u"输入 用户名", text
        self.input_text(self.username_input, text)
        sleep(2)

    def input_password(self, text="000000"):
        print u"输入 用户密码", text
        self.input_text(self.password_input, text)
        sleep(2)

    def click_login_btn(self):
        print u"点击 登陆 按钮"
        self.click(self.login_btn)
        sleep(5)
