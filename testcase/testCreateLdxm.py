# coding=utf-8
__author__ = 'JACK_CHAN'

import unittest
from time import sleep
from pages.basePage import Page
from common.excel_xlsx import Excel
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

        filename1 = u'D:\\Test\\POM_LDGZ_OLD\\textdata\\登录管理.xlsx'
        login_sheet = Excel(filename1, '登录')

        login_page.open_url()

        login_page.choose_module_ldgz()

        login_page.input_username(login_sheet.get_cell_value('用户名'))

        login_page.input_password(login_sheet.get_cell_value('密码'))

        login_page.click_login_btn()


        ldxm_page.enter_sub_menu('劳动项目与计划管理', '劳动项目')
        sleep(2)

        ldxm_page.click_create_xm_btn()
        sleep(2)

        # 劳动项目信息

        ldxm_page.select_xm_xmlx(ldxm_sheet.get_cell_value('项目类型'))

        ldxm_page.select_xm_xmmc(ldxm_sheet.get_cell_value('项目名称'))

        ldxm_page.input_xm_dwmc(ldxm_sheet.get_cell_value('单位名称'))

        ldxm_page.input_xm_xmfzr(ldxm_sheet.get_cell_value('项目负责人'))

        ldxm_page.input_xm_lxdh(ldxm_sheet.get_cell_value('联系电话'))

        # 客户信息

        ldxm_page.input_xm_hzfdwmc(khxx_sheet.get_cell_value('合作方单位名称'))

        ldxm_page.input_xm_fzr(khxx_sheet.get_cell_value('负责人'))

        ldxm_page.input_xm_dz(khxx_sheet.get_cell_value('地址'))

        ldxm_page.input_xm_yyzzzch(khxx_sheet.get_cell_value('营业执照注册号'))

        ldxm_page.input_xm_khfzrlxdh(khxx_sheet.get_cell_value('客户负责人联系电话'))

        ldxm_page.input_xm_czh(khxx_sheet.get_cell_value('传真号'))

        # 合同信息

        ldxm_page.input_xm_zczj(khxx_sheet.get_cell_value('注册资金'))

        ldxm_page.input_xm_cpxh(htxx_sheet.get_cell_value('产品型号'))

        ldxm_page.input_xm_sl(htxx_sheet.get_cell_value('数量'))

        ldxm_page.input_xm_dj(htxx_sheet.get_cell_value('单价'))

        ldxm_page.input_xm_zje(htxx_sheet.get_cell_value('总金额'))

        ldxm_page.select_xm_scdw(htxx_sheet.get_cell_value('生产单位'))

        ldxm_page.select_xm_khfs(htxx_sheet.get_cell_value('考核方式'))

        ldxm_page.get_htbh_value()

        ldxm_page.input_xm_wcrq(htxx_sheet.get_cell_value('完成日期'))

        ldxm_page.input_xm_fktj(htxx_sheet.get_cell_value('付款条件'))

        ldxm_page.input_xm_tbr(htxx_sheet.get_cell_value('填报人'))

        ldxm_page.input_xm_tbrlxdh(htxx_sheet.get_cell_value('联系电话'))

        ldxm_page.input_xm_htfj(htxx_sheet.get_cell_value('合同附件'))

        # 项目基本资料

        ldxm_page.input_xm_trldlrs(xmjbzl_sheet.get_cell_value('投入劳动力人数'))

        ldxm_page.input_xm_xmtze(xmjbzl_sheet.get_cell_value('项目投资额'))

        ldxm_page.input_xm_sbt(xmjbzl_sheet.get_cell_value('设备台（套）'))

        ldxm_page.input_xm_qyzysb(xmjbzl_sheet.get_cell_value('企业自有设备'))

        ldxm_page.input_xm_khtrsb(xmjbzl_sheet.get_cell_value('客户投入设备'))

        ldxm_page.input_xm_xmnsr(xmjbzl_sheet.get_cell_value('项目年收入'))

        ldxm_page.input_xm_yrjsr(xmjbzl_sheet.get_cell_value('月人均收入'))

        ldxm_page.input_xm_sdfzcb(xmjbzl_sheet.get_cell_value('水电、房租等成本费用'))

        ldxm_page.input_xm_lr(xmjbzl_sheet.get_cell_value('利润'))

        ldxm_page.select_xm_fxdj(xmjbzl_sheet.get_cell_value('风险等级'))

        ldxm_page.input_xm_fxpgfj(xmjbzl_sheet.get_cell_value('风险评估附件'))

        ldxm_page.input_xm_xmpg(xmjbzl_sheet.get_cell_value('项目评估'))

        ldxm_page.input_xm_pgry(xmjbzl_sheet.get_cell_value('评估人员'))

        ldxm_page.input_xm_bz(xmjbzl_sheet.get_cell_value('备注'))

        ldxm_page.click_btn(LdxmPage.xmqx_xp)

        login_page.log_out()

    def tearDown(self):
        self.driver.quit()
