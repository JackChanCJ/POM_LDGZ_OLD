# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
from pages.basePage import Page

reload(sys)
sys.setdefaultencoding("utf-8")

class LdxmPage(Page):
    mkmc = u"劳动项目与计划管理"
    ymmc = u"劳动项目"
    xm_btn = u"//a[text()='新增项目']"
    ht_btn = u"//a[text()='新增合同']"

    def __init__(self, driver, base_url=u"http://192.168.10.201:7001"):
        Page.__init__(self, driver, base_url)

    def enter_ldxm_page(self):
        print u"进入 劳动项目与计划管理-->劳动项目 页面"
        self.enter_page(self, self.mkmc, self.ymmc)

    def click_create_xm_btn(self):
        print u"点击 新增劳动项目，跳转至劳动项目页面"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        self.click(self.xm_btn)

    def write_xm(self):
        print u"填写 劳动项目各字段"

    def click_create_ht_btn(self):
        print u"点击 新增劳动合同,跳转至劳动合同页面"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        self.click(self.ht_btn)




