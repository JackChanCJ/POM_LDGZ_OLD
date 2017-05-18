# coding=utf-8
__author__ = 'JACK_CHAN'

import unittest
import sys
import time
from selenium import webdriver
from pages.loginMK.loginPage import LoginPage
reload(sys)
sys.setdefaultencoding("utf-8")

# 百度搜索测试
class TestloginPage(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Chrome()
    def testLogin(self):
        driver = self.driver
        # 百度网址
        url = u"http://localhost:7001"
        # 期望验证的标题
        assert_title = u"全国监狱信息化管理平台V3.0"
        # print assert_title
        login_Page = LoginPage(driver, url)
        # 启动浏览器，访问劳动改造地址
        login_Page.openLDGZHomePage()

        login_Page.choose_mokuai_icon()

        login_Page.input_username()

        login_Page.input_password()

        login_Page.click_login_btn()
        time.sleep(5)
        print u"验证标题"
        self.assertEqual(login_Page.driver.title, assert_title)
    def tearDown(self):
        self.driver.quit()


