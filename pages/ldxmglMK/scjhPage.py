# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
import re
import os
from time import sleep
from openpyxl import load_workbook
from pages.basePage import Page
from textdata import read_excel_by_cellname
from textdata import write_excel_by_cellname
from selenium.webdriver.support.select import Select

class ScjhPage(Page):
    cwd = os.getcwd()
    cwd = os.path.abspath(os.path.dirname(cwd) + os.path.sep + "..")

    ldxmyjhgl_xlsx = unicode(cwd, 'utf-8') + u'\\textdata\\劳动项目与计划管理.xlsx"'
    sub_menu = u'劳动项目与计划管理'
    sub_page = u'监狱劳动生产计划'

    jhzd_btn = u"//a[text()='计划制定']"

    add_jh_btn = u"//a[text()='新增']"
    delete_btn = u"//a[text()='删除']"
    export_btn = u"//a[text()='导出']"
    return_btn = u"//a[text()='返回']"

    jhlx_select = u"//select[@id='jhlx']"
    htmc_value = read_excel_by_cellname(filename=ldxmyjhgl_xlsx,
                                        sheet_name='劳动合同',
                                        cell_num='C2')
    cpxh_value = read_excel_by_cellname(filename=ldxmyjhgl_xlsx,
                                        sheet_name='合同明细',
                                        cell_num='A2')
    scdw_value = read_excel_by_cellname(filename=ldxmyjhgl_xlsx,
                                        sheet_name='劳动合同',
                                        cell_num='G2')
    jhnr_value = read_excel_by_cellname(filename=ldxmyjhgl_xlsx,
                                        sheet_name='生产计划',
                                        cell_num='L2')
    bz_textarea = u"//textarea[@id='bz']"
    bz_value = read_excel_by_cellname(filename=ldxmyjhgl_xlsx,
                                        sheet_name='生产计划',
                                        cell_num='M2')
    cancel_btn = u"//input[@value='取消']"

    def __init__(self, driver):
        Page.__init__(self, driver)

    # 进入生产计划页面
    def enter_scjh_sub_page(self):
        self.enter_sub_menu(self.sub_menu, self.sub_page)
        print u"进入  %s-->%s  页面" % (self.sub_menu, self.sub_page)

    # 进入计划制定页面
    def enter_jhzd_page(self):
        print u"点击  计划制定 按钮，跳转至计划制定页面"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        self.click_btn(self.jhzd_btn)

    # 进入新增计划页面
    def enter_jhxz_page(self):
        print u"点击  新增 按钮，跳转至计划制定新增页面"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        self.click_btn(self.add_jh_btn)

    # 获取计划代号
    def get_jh_jhdh(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        jhdh_input = u"//input[@id='jhdh']"
        jhdh_value = self.driver.get_text_value(jhdh_input)
        print ("获取  '计划代号'的值%s" % jhdh_value)

    def select_jh_xmmc(self, xmmc):
        xmmc_xp = u"//select[@id='xmbh']"
        Select(xmmc_xp).select_by_visible_text(xmmc)
        print ("选择  '计划——项目名称", xmmc)

    def input_jh_jhqr(self, jhqr):
        jhqr_input = u"//input[@id='jhqr']"
        self.input_text(jhqr_input).send_keys(jhqr)
        print ("输入  计划起日", jhqr)

    def select_jh_htmc(self, htmc):
        htmc_select = u"//select[@id='htbh']"
        Select(htmc_select).select_by_visible_text(htmc)
        print ("选择  '计划——项目名称", htmc)

    def input_jh_jhzr(self, jhzr):
        jhzr_input = u"//input[@id='jhzr']"
        self.input_text(jhzr_input).send_keys(jhzr)
        print ("输入  计划止日", jhzr)

    def select_jh_cpxh(self, cpxh):
        cpxh_select = u"//select[@id='kh']"
        Select(cpxh_select).select_by_visible_text(cpxh)
        print ("选择  '计划——产品型号", cpxh)

    def get_jh_jysl(self):
        jhsl_input = u"//input[@id='jhscsl']"
        jysl_value = self.driver.get_text_value(jhsl_input)
        print ("获取  计划——计划数量", jysl_value)

    def select_jh_scdw(self, scdw):
        scdw_select = u"//select[@id='scdw']"
        Select(scdw_select).select_by_visible_text(scdw)
        print ("选择  计划——生产单位", scdw)

    def get_jy_jyhsje(self):
        jyhsje_input = u"//input[@id='jyhsje']"
        jyhsje_value = self.driver.get_text_value(jyhsje_input)
        print ("获取  计划——监狱核算金额", jyhsje_value)

    def get_jh_zrjhwcsl(self):
        zrjhwcsl_input = u"//input[@id='zrwcsl']"
        zrjhwcsl_value = self.driver.get_text_value(zrjhwcsl_input)
        print ("获取  计划——逐日计划完成数量", zrjhwcsl_value)

    def input_jh_jhnr(self, jhnr):
        jhnr_textarea = u"//textarea[@id='jhnr']"
        jhnr_value = self.driver.get_text_value(jhnr_textarea)
        print ("输入  计划——计划内容", jhnr)

    def click_jh_save(self):
        jh_save = u"//input[@value='保存']"
        self.driver.click_btn(jh_save)


'''
    # 新增计划
    def add_jh(self):
        self.click_btn(self.add_jh_btn)
        sleep(3)
        jhdh_value = self.get_input_text(self.jhdh_input, "value")
        write_excel_by_cellname(w_value=jhdh_value,
                                filename=ldxmyjhgl_xlsx,
                                sheet_index=6,
                                cell_num='A2')
        print '获取   "计划代号"的值：%s，写入excel' %jhdh_value
        # 用唯一的项目编号来匹配项目名称并进行选择
        hq_xmmc_value = read_excel_by_cellname(filename=ldxmyjhgl_xlsx,
                                               sheet_name='劳动项目',
                                               cell_num='A2')
        re_xmmc_value = str(hq_xmmc_value + '.*')
        xmmc_opts = Select(self.driver.find_element_by_xpath(self.xmmc_select)).options
        for xmmc_opt in xmmc_opts:
            if re.findall(re_xmmc_value, xmmc_opt.text, re.S):
                self.select_box(self.xmmc_select, xmmc_opt.text)
                print '选择   项目名称：%s' %xmmc_opt.text
        # 取前面加的   合同名称
        print self.htmc_value
        self.select_box(self.htmc_select, self.htmc_value)
        print "选择   合同名称：%s" %self.htmc_value
        # 取前面加的   产品型号
        self.select_box(self.cpxh_select, self.cpxh_value)
        print "选择   产品型号：%s" %self.cpxh_value
        self.click(self.jhsl_input)
        # 取前面加的   完成单位
        self.select_box(self.scdw_select, self.scdw_value)
        print "选择   完成单位：%s" %self.scdw_value
        self.input_text(self.jhnr_textarea, self.jhnr_value)
        print "输入   计划内容：%s" %self.jhnr_value
        self.input_text(self.bz_textarea, self.bz_value)
        print "输入   备注：%s" %self.bz_value
        self.click(self.save_btn)
        # print "点击   保存  按钮"
'''




def main():
    cwd = os.path.abspath('..')
    print (cwd)

if __name__ == '__main__':
    main()