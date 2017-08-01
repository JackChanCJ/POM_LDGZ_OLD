# coding=utf-8
__author__ = 'JACK_CHAN'

import unittest
import sys
from time import sleep
from selenium import webdriver
from pages.ldxmglMK.ldxmPage import LdxmPage
from pages.loginMK.loginPage import LoginPage

reload(sys)
sys.setdefaultencoding("utf-8")

class TestCreateLdht(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def testCreateLdht(self):

        login_Page = LoginPage()

        login_Page.log_in()

        ldht_Page = LdxmPage()

        ldht_Page.enter_ldxm_page()
        sleep(2)

        ldht_Page.click_create_ht_btn()
        sleep(2)

        ldht_Page.create_ht()

        login_Page.log_out()

    def tearDown(self):
        self.driver.quit()

