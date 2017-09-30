# coding=utf-8
__author__ = 'JACK_CHAN'

import unittest
from time import sleep
from selenium import webdriver
from common.excel_xlsx import Excel
from pages.ldxmglMK.ldxmPage import LdxmPage
from pages.loginMK.loginPage import LoginPage

class TestCreateLdht(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def testCreateLdht(self):
        login_page = LoginPage(self.driver)
        ldht_page = LdxmPage(self.driver)

        filename1 = u'D:\\Test\\POM_LDGZ_OLD\\textdata\\登录管理.xlsx'
        login_sheet = Excel(filename1, '登录')

        login_page.open_url()

        login_page.choose_module_ldgz()

        login_page.input_username(login_sheet.get_cell_value('用户名'))

        login_page.input_password(login_sheet.get_cell_value('密码'))

        login_page.click_login_btn()

        ldht_page.enter_sub_menu('劳动项目与计划管理', '劳动项目')
        sleep(2)

        ldht_page.click_create_ht_btn()
        sleep(2)

        # 合同备案


        ldht_page.create_ht()

        ldht_page.log_out()

    def tearDown(self):
        self.driver.quit()

