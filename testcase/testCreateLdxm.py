# coding=utf-8
__author__ = 'JACK_CHAN'

import unittest
import sys
from time import sleep
from pages.basePage import Page
from selenium import webdriver
from pages.ldxmglMK.ldxmPage import LdxmPage
from pages.loginMK.loginPage import LoginPage

reload(sys)
sys.setdefaultencoding("utf-8")

class TestCreateLdxm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def testCreateLdxm(self):
        driver = self.driver
        login_Page = LoginPage(driver)
        login_Page.openLDGZHomePage()
        login_Page.choose_mokuai_icon()
        login_Page.input_username()
        login_Page.input_password()
        login_Page.click_login_btn()

        ldxm_Page = LdxmPage(driver)

        ldxm_Page.enter_ldxm_page()
        sleep(2)

        ldxm_Page.click_create_xm_btn()
        sleep(2)

        ldxm_Page.create_xm()

        print u"alldone"

    def tearDown(self):
        pass

