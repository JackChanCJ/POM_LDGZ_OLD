# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
import re
from time import sleep
from openpyxl import load_workbook
from pages.basePage import Page
from textdata import read_excel_by_cellname
from textdata import write_excel_by_cellname
from selenium.webdriver.support.select import Select


reload(sys)
sys.setdefaultencoding("utf-8")

class ScjhPage(Page):
    filename = u"D:\\Test\\POM_LDGZ_OLD\\textdata\\劳动项目与计划管理.xlsx"
    sub_menu = u'劳动项目与计划管理'
    mkmc = u'监狱劳动生产计划'

    jhzd_btn = u"//a[text()='计划制定']"

    add_jh_btn = u"//a[text()='新增']"
    delete_btn = u"//a[text()='删除']"
    export_btn = u"//a[text()='导出']"
    return_btn = u"//a[text()='返回']"

    jhdh_input = u"//input[@id='jhdh']"
    jhlx_select = u"//select[@id='jhlx']"
    xmmc_select = u"//select[@id='xmbh']"
    jhqr_input = u"//input[@id='jhqr']"
    htmc_select = u"//select[@id='htbh']"
    htmc_value = read_excel_by_cellname(filename=filename,
                                        sheet_name='生产计划',
                                        cell_num='C2')
    jhzr_input = u"//input[@id='jhzr']"
    cpxh_select = u"//select[@id='kh']"
    cpxh_value = read_excel_by_cellname(filename=filename,
                                        sheet_name='生产计划',
                                        cell_num='A2')
    jhsl_input = u"//input[@id='jhscsl']"
    scdw_select = u"//select[@id='scdw']"
    scdw_value = read_excel_by_cellname(filename=filename,
                                        sheet_name='生产计划',
                                        cell_num='G2')
    jyhsje_input = u"//input[@id='jyhsje']"
    zrwcsl_input = u"//input[@id='zrwcsl']"
    jhnr_textarea = u"//textarea[@id='jhnr']"
    jhnr_value = read_excel_by_cellname(filename=filename,
                                        sheet_name='生产计划',
                                        cell_num='L2')
    bz_textarea = u"//textarea[@id='bz']"
    bz_value = read_excel_by_cellname(filename=filename,
                                        sheet_name='生产计划',
                                        cell_num='M2')
    btn_save = u"//input[@'保存']"
    btn_cancel = u"//input[@'取消']"



    def __init__(self, driver):
        Page.__init__(self, driver)
    # 进入生产计划页面
    def enter_scjh_page(self):
        self.enter_sub_menu(self.sub_menu, self.mkmc)
        print u"进入  %s-->%s  页面" %(self.sub_menu, self.mkmc)

    # 进入计划制定页面
    def enter_jhzd_page(self):
        print u"点击 计划制定 按钮，跳转至计划制定页面"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        self.click(self.jhzd_btn)

    # 新增计划
    def add_jh(self):
        self.click(self.add_jh_btn)
        sleep(3)
        jhdh_value = self.get_input_text(self.jhdh_input, "value")
        write_excel_by_cellname(w_value=jhdh_value,
                                filename=self.filename,
                                sheet_index=6,
                                cell_num='A2')
        print '获取"计划代号"的值：%s，写入excel' %jhdh_value
        # 用唯一的项目编号来匹配项目名称并进行选择
        hq_xmmc_value = read_excel_by_cellname(filename=self.filename,
                                               sheet_name='劳动项目',
                                               cell_num='A2')
        re_xmmc_value = str(hq_xmmc_value + '.*')
        xmmc_eles = self.driver.find_elements_by_xpath(self.xmmc_select)
        for xmmc_ele in xmmc_eles:
            if re.findall(re_xmmc_value, xmmc_ele.text, re.S):
                xmmc_text = unicode(xmmc_ele.text, 'utf-8')
                self.select_box(self.xmmc_select, xmmc_text)
                print '选择  项目名称：%s' %xmmc_text
        # 取前面加的   合同名称
        self.select_box(self.htmc_select, self.htmc_value)
        print "选择   合同名称：%s" %self.htmc_value
        # 取前面加的   产品型号
        self.select_box(self.cpxh_select, self.cpxh_value)
        print "选择   产品型号：%s" %self.cpxh_value
        # 取前面加的   完成单位
        self.select_box(self.scdw_select, self.scdw_value)
        print "选择   完成单位：%s" %self.scdw_value
        self.input_text(self.jhnr_textarea, self.jhnr_value)
        print "输入   计划内容：%s" %self.jhnr_value
        self.input_text(self.bz_textarea, self.bz_value)
        print "输入   备注：%s" %self.bz_value




