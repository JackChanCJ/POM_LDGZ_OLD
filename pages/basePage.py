# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
import random
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver

reload(sys)
sys.setdefaultencoding("utf-8")

# Page基类
class Page(object):
    """
        所有的page都应该继承该类
        所有的操作最少需停留一秒
    """
    def __init__(self, driver, base_url=u"http://localhost:7001"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        self.driver.maximize_window()

    def input_text(self, loc, text):
        self.driver.find_element_by_xpath(loc).send_keys(text)
        sleep(1)

    def choose_xt(self, loc):
        self.driver.find_element_by_xpath(loc).click()
        sleep(1)

    def click(self, loc):
        self.driver.find_element_by_xpath(loc).click()
        sleep(1)

    # driver.title不需要括号
    def get_title(self):
        self.driver.title
        sleep(1)

    def enter_sub_menu(self, sub_menu, mkmc):
        # 从子菜单进入各模块
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame("menuFrame")
        mk_loc = "//span[text()='%s']" % sub_menu
        ym_loc = "//span[@sjmc='%s' and text()='%s']" %(sub_menu, mkmc)
        self.driver.find_element_by_xpath(mk_loc).click()
        sleep(1)
        self.driver.find_element_by_xpath(ym_loc).click()
        sleep(1)

    def random_select_box(self, loc):
        # 随机选择下拉框元素 c_ele下拉框元素
        c_ele = self.driver.find_element_by_xpath(loc)
        c_ele.click()
        sleep(1)
        ret = Select(c_ele).options
        srand = random.Random().choice(ret)
        Select(c_ele).select_by_value(srand.get_attribute("value"))
        c_ele.send_keys(Keys.ESCAPE)
        sleep(1)

    def select_box(self, loc, text):
        s_ele = self.driver.find_element_by_xpath(loc)
        s_ele.click()
        Select(s_ele).select_by_visible_text(text)
        s_ele.send_keys(Keys.ESCAPE)
        sleep(1)

    def get_input_text(self, loc, attribute):
        # 获取文本框的值
        attribute_value = self.driver.find_element_by_xpath(loc).get_attribute(attribute)
        return attribute_value
