# coding=utf-8
__author__ = 'JACK_CHAN'

import unittest
import sys
import time
from selenium import webdriver
from common.Excel import Excel
from pages.loginMK.loginPage import LoginPage
reload(sys)
sys.setdefaultencoding("utf-8")

# 劳改系统登录
class TestloginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def testLogin(self):
        # 期望验证的标题
        assert_title = u"全国监狱信息化管理平台V3.0"
        # print assert_title
        login_page = LoginPage(self.driver)
        # filename = u'D:\\Test\\POM_LDGZ_OLD\\textdata\\登录管理.xlsx'
        filename = u"D:\\01____WorkStation\PYTHON\\POM_LDGZ_OLD\\textdata\\登录管理.xlsx"
        login_sheet = Excel(filename, '登录')
        # 启动浏览器，访问劳动改造地址
        login_page.openLDGZHomePage()

        login_page.choose_module_icon()

        login_page.input_username(login_sheet.get_cell_value('用户名'))

        login_page.input_password(login_sheet.get_cell_value('密码'))

        login_page.click_login_btn()

        print u"验证标题"
        self.assertEqual(login_page.driver.title, assert_title)

        login_page.log_out()

    def tearDown(self):
        self.driver.quit()


