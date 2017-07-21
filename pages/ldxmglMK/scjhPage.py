# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
from time import sleep
from pages.basePage import Page
from textdata import read_excel_by_cellname
from textdata import write_excel_by_cellname


reload(sys)
sys.setdefaultencoding("utf-8")

class ScjhPage(Page):
    sub_menu = u'劳动项目'
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
    jhzr_input = u"//input[@id='jhzr']"
    cpxh_select = u"//select[@id='kh']"
    jhsl_input = u"//input[@id='jhscsl']"
    scdw_select = u"//select[@id='scdw']"
    jyhsje_input = u"//input[@id='jyhsje']"
    zrwcsl_input = u"//input[@id='zrwcsl']"
    jhnr_textarea = u"//textarea[@id='jhnr']"
    bz_textarea = u"//textarea[@id='bz']"
    btn_save = u"//input[@'保存']"
    btn_cancel = u"//input[@'取消']"




    def __init__(self, driver):
        Page.__init__(self, driver)

    def enter_scjh_page(self):
        self.enter_sub_menu(self.sub_menu, self.mkmc)
        print u"进入  %s-->%s  页面" %(self.sub_menu, self.mkmc)

    # 进入计划制定页面
    def enter_jhzd_page(self):
        print u"点击 %s按钮，跳转至计划制定页面" %self.mkmc
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        self.click(self.jhzd_btn)

    # 新增计划
    def add_jh(self):
        self.click(self.add_jh_btn)
        sleep(3)
        self.

