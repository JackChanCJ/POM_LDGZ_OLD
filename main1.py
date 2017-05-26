# coding=utf-8
__author__ = 'JACK_CHAN'

import unittest
import sys
from common import HTMLTestRunner
from testcase.testCreateLdxm import TestCreateLdxm
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestCreateLdxm('testCreateLdxm'))
    # 定义报告输出路径
    htmlPath = u"page_demo_Report.html"
    fp = file(htmlPath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"劳改登录测试",
                                           description=u"系统测试")
    runner.run(testunit)
    fp.close()