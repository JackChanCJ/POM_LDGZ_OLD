# coding=utf-8
__author__ = 'JACK_CHAN'

import unittest
import sys
import time
import os
from selenium import webdriver
from common.excel_xlsx import Excel
from pages.loginMK.loginPage import LoginPage

# 劳改系统登录
class TestloginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def testLogin(self):
        # 期望验证的标题
        assert_title = u"全国监狱信息化管理平台V3.0"
        # print assert_title
        login_page = LoginPage(self.driver)
        #  获取当前登录管理.xlsx相对路径
        cwd = os.path.abspath('.')
        dlgl_xlsx = unicode(cwd, 'utf-8') + u'\\textdata\\登录管理.xlsx'
        login_sheet = Excel(dlgl_xlsx, '登录')
        # 启动浏览器，访问劳动改造地址
        login_page.open_url()

        login_page.choose_module_ldgz()

        login_page.input_username(login_sheet.get_cell_value('用户名'))

        login_page.input_password(login_sheet.get_cell_value('密码'))

        login_page.click_login_btn()

        print u"验证标题"
        self.assertEqual(login_page.get_title(), assert_title)

        login_page.log_out()

    def tearDown(self):
        self.driver.quit()


