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
        login_page = LoginPage(self.driver)

        login_page.log_in()

        ldxm_page = LdxmPage(self.driver)

        ldxm_page.enter_ldxm_sub_page()
        sleep(2)

        ldxm_page.click_create_xm_btn()
        sleep(2)

        ldxm_page.create_xm()

        login_page.log_out()

    def tearDown(self):
        self.driver.quit()

