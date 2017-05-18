# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
import random
from time import sleep
reload(sys)
from selenium.webdriver.support.select import Select

sys.setdefaultencoding("utf-8")

# Page基类
class Page(object):
    # 所有的page都应该集成该类
    def __init__(self, driver, base_url=u"http://localhost:7001"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def input_text(self, loc, text):
        self.driver.find_element_by_xpath(loc).send_keys(text)

    def choose_xt(self, loc):
        self.driver.find_element_by_xpath(loc).click()

    def click(self, loc):
        self.driver.find_element_by_xpath(loc).click()
    # driver.title不需要括号
    def get_title(self):
        self.driver.title

    def enter_page(self, mkmc, ymmc):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("menuFrame")
        # 方法1
        # mk_loc = u"//span[text()='\"+ mkmc +\"']"
        # ym_loc = u"//span[@sjmc='\"+ mkmc +\"' and text()='\"+ ymmc +\"']"
        # self.driver.find_element_by_xpath(mk_loc).click()
        # self.driver.find_element_by_xpath(ym_loc).click()

        # 方法2
        mks = u"//span[@class='folder']"
        mk_elements = self.driver.find_elements_by_xpath(mks)
        for mk_element in mk_elements:
            if mk_element.text == mkmc:
                mk_element.click()
                yms = u"//li[@sjmc='\" + mkmc +\" ']"
                ym_elements = self.driver.find_elements_by_xpath(yms)
                for ym_element in ym_elements:
                    if ym_element.text == ymmc:
                        ym_element.click()

    def random_select_box(self, loc):
        # c_ele下拉框元素
        c_ele = self.driver.find_element_by_xpath(loc)
        c_ele.click()
        sleep(1)
        ret = Select(c_ele).optins
        srand = random.Random().choice(ret)
        Select(c_ele).select_by_value(srand.get_attribute("value"))

    def select_box(self, loc, text):
        self.driver.find_element_by_xpath(loc).click()
        Select(self.driver.find_element_by_xpath(loc)).select_by_visible_text(text)

















