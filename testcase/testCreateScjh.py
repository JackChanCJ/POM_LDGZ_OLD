# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
import unittest
from time import sleep
from SELENIUM import webdriver
from pages.basePage import Page
from pages.loginMK.loginPage import LoginPage
from pages.ldxmglMK.scjhPage import ScjhPage

reload(sys)
sys.setdefaultencoding("utf-8")

class TestCreateScjh(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def testCreateScjh(self):
        driver = self.driver
        login_page = LoginPage()
        scjh_page = ScjhPage()

        login_page.log_in()

        scjh_page.enter_scjh_sub_page()

        scjh_page.enter_jhzd_page()

        scjh_page.add_jh()

    def tearDown(self):
        pass
        # self.driver.quit()


