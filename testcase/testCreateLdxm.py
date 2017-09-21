# coding=utf-8
__author__ = 'JACK_CHAN'

import unittest
from time import sleep
from pages.basePage import Page
from common.Excel import Excel
from selenium import webdriver
from pages.ldxmglMK.ldxmPage import LdxmPage
from pages.loginMK.loginPage import LoginPage

class TestCreateLdxm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def testCreateLdxm(self):
        login_page = LoginPage(self.driver)
        ldxm_page = LdxmPage(self.driver)
        filename = u'D:\\Test\\POM_LDGZ_OLD\\textdata\\劳动项目与计划管理.xlsx'
        # filename = u"D:\\01____WorkStation\PYTHON\\POM_LDGZ_OLD\\textdata\\登录管理.xlsx"
        ldxm_sheet = Excel(filename, '劳动项目')
        khxx_sheet = Excel(filename, '客户信息')
        htxx_sheet = Excel(filename, '合同信息')
        xmjbzl_sheet = Excel(filename, '项目基本资料')
        ldht_sheet = Excel(filename, '劳动合同')
        htmx_sheet = Excel(filename, '合同明细')
        scjh_sheet = Excel(filename, '生产计划')


        login_page.log_in()

        ldxm_page.enter_sub_menu('劳动项目与计划管理', '劳动项目')
        sleep(2)

        ldxm_page.click_create_xm_btn()
        sleep(2)

        ldxm_page.select_xm_xmlx(ldxm_sheet.get_cell_value('项目类型'))

        login_page.log_out()

    def tearDown(self):
        self.driver.quit()

