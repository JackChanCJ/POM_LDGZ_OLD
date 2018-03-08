# coding=utf-8
__author__ = 'JACK_CHAN'

import os
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

        #  获取当前目录
        cwd = os.path.abspath('.')
        dlgl_xlsx = unicode(cwd, 'utf-8') + u'\\textdata\\登录管理.xlsx'
        print dlgl_xlsx
        ldxmyjhgl_xlsx = unicode(cwd, 'utf-8') + u'\\textdata\\劳动项目与计划管理.xlsx'

        login_sheet = Excel(dlgl_xlsx, '登录')
        ht_htba_sheet = Excel(ldxmyjhgl_xlsx, '合同_合同备案')
        ht_htmx_sheet = Excel(ldxmyjhgl_xlsx, '合同_合同明细')

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
        # ldht_page.select_ht_xmmc(ht_htba_sheet.get_cell_value('项目名称'))

        ldht_page.get_ht_htbh()

        ldht_page.input_ht_htmc(ht_htba_sheet.get_cell_value('合同名称'))

        ldht_page.input_ht_zje(ht_htba_sheet.get_cell_value('总金额'))

        ldht_page.input_ht_qdrq(ht_htba_sheet.get_cell_value('签订日期'))

        ldht_page.input_ht_wcrq(ht_htba_sheet.get_cell_value('完成日期'))

        ldht_page.select_ht_scdw(ht_htba_sheet.get_cell_value('生产单位'))

        ldht_page.select_ht_khfs(ht_htba_sheet.get_cell_value('考核方式'))

        ldht_page.input_ht_khmc(ht_htba_sheet.get_cell_value('客户名称'))

        ldht_page.input_ht_htnr(ht_htba_sheet.get_cell_value('合同内容'))

        ldht_page.input_ht_fj(ht_htba_sheet.get_cell_value('附件'))

        # 合同明细
        ldht_page.input_ht_xh(ht_htmx_sheet.get_cell_value('型号'))

        ldht_page.input_ht_ks(ht_htmx_sheet.get_cell_value('款式'))

        ldht_page.input_ht_gg(ht_htmx_sheet.get_cell_value('规格'))

        ldht_page.input_ht_pp(ht_htmx_sheet.get_cell_value('品牌'))

        ldht_page.input_ht_sl(ht_htmx_sheet.get_cell_value('数量'))

        ldht_page.input_ht_dj(ht_htmx_sheet.get_cell_value('单价'))

        login_page.log_out()

    def tearDown(self):
        self.driver.quit()

def main():
    cwd = os.getcwd()
    dlgl_xlsx = unicode(cwd, 'utf-8') + u'\\登录管理.xlsx'
    print dlgl_xlsx


if __name__ == "__main__":
    main()
