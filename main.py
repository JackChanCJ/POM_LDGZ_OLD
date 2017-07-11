# coding=utf-8
__author__ = 'JACK_CHAN'

import unittest
import sys
from common import HTMLTestRunner
from time import sleep
from testcase.testLoginPage import TestloginPage
from testcase.testCreateLdxm import TestCreateLdxm
from testcase.testCreateLdht import TestCreateLdht

reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # 添加多个测试集
    # tests = ['testLogin1','testLogin2','testLogin3']
    # testunit.addTest(tests)

    # 测试登陆
    # testunit.addTest(TestloginPage('testLogin'))
    # sleep(8)

    # 测试新增劳动项目
    # testunit.addTest(TestCreateLdxm('testCreateLdxm'))
    # sleep(8)

    # 测试新增劳动合同
    testunit.addTest(TestCreateLdht('testCreateLdht'))
    sleep(8)

    # 定义报告输出路径
    htmlPath = u"page_demo_Report.html"
    fp = file(htmlPath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"劳改登录测试",
                                           description=u"系统测试")
    runner.run(testunit)
    fp.close()
