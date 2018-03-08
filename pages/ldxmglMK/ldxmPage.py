#  coding=utf-8
__author__ = 'JACK_CHAN'

import re
import os
import textdata
from pages.basePage import Page
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class LdxmPage(Page):
    cwd = os.getcwd()
    #  祖父级别路径
    cwd = os.path.abspath(os.path.dirname(cwd) + os.path.sep + "..")
    filename = unicode(cwd, 'utf-8') + u"\\textdata\\劳动项目与计划管理.xlsx"

    # 劳动项目与计划管理-->劳动项目页面
    add_xm_xp = u"//a[text()='新增项目']"  # 新增项目    按钮
    add_ht_xp = u"//a[text()='新增合同']"  # 新增合同    按钮

    # 劳动项目详情页按钮
    xmbc_xp = u"//input[@value='保 存']"  # 保存    按钮
    xmqx_xp = u"//input[@value='取 消 ']"  # 取消    按钮

    # 合同备案新增页面按钮
    ht_bc_xp = u"//input[@type='button' and @value='保 存']"  # 保存按钮
    ht_qx_xp = u"//input[@value='保存' and @type='button']"  # 取消按钮

    def __init__(self, driver):
        Page.__init__(self, driver)

    def click_create_xm_btn(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        self.click_btn(self.add_xm_xp)
        print u"点击 新增项目按钮，跳转至项目页面"

    def click_create_ht_btn(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        self.click_btn(self.add_ht_xp)
        print u"点击 新增合同按钮，跳转至合同页面"

    # xmlx, xmmc, dwmc, xmfzr, xmfzrlxdh,                                     # 劳动项目
    # hzfdwmc, fzr, dz, yyzzzch, khlxdh, czhm, zczj,                          # 客户信息
    # cpxh, sl, dj, zje, scdw, khfs, wcrq, fktj, tbr, tbrlxdh, htfj,          # 合同信息
    #
    # trldlrs, xmtze, sbs, qyzysb, khtrsb, xmnsr,                             # 项目基本资料
    # yrjsr, sdfzcb, lr, fxdj, fxpgfj, xmpg, pgry, bz

    def get_xmbh_value(self):
        xmbh_xp = u"//input[name()='bh']"
        xmbh_value = self.get_text_value(xmbh_xp).get_attribute('项目编号')
        print u"获取'项目编号'的值： ", xmbh_value
        return xmbh_value

    def select_xm_xmlx(self, xmlx):
        xmlx_xp = u"//select[@id='xmlx']"  # 项目类型   下拉选择框
        sel = self.select_box(xmlx_xp)
        Select(sel).select_by_visible_text(xmlx)
        print u"选择 项目类型：", xmlx

    def select_xm_xmmc(self, xmmc):
        xmmc_xp = u"//select[@id='selectXmmc']"  # 项目名称   下拉选择框
        sel = self.select_box(xmmc_xp)
        Select(sel).select_by_visible_text(xmmc)
        print u"选择 项目名称：", xmmc

    def input_xm_dwmc(self, dwmc):
        dwmc_xp = u"//input[@name='lgXmXmzr.xmscdwmc']"  # 单位名称   文本输入
        self.input_text(dwmc_xp).send_keys(dwmc)
        print u"输入 单位名称: ", dwmc

    def input_xm_xmfzr(self, xmfzr):
        xmfzr_xp = u"//input[@name='lgXmXmzr.xmfzr']"  # 项目负责人   文本输入框
        self.input_text(xmfzr_xp).send_keys(xmfzr)
        print u"输入 项目负责人: ", xmfzr

    def input_xm_lxdh(self, xmfzrlxdh):
        xmfzrlxdh_xp = u"//input[@name='lgXmXmzr.xmfzrlxdh']"  # 项目负责人联系电话   文本输入框
        self.input_text(xmfzrlxdh_xp).send_keys(xmfzrlxdh)
        print u"输入 项目负责人联系电话: ", xmfzrlxdh

    # 客户单位信息
    def input_xm_hzfdwmc(self, hzfdwmc):
        hzfdwmc_xp = u"//input[@name='lgXmXmzr.khdwmc']"  # 合作方单位名称   文本输入框
        self.input_text(hzfdwmc_xp).send_keys(hzfdwmc)
        print u"输入 合作方单位名称: ", hzfdwmc

    def input_xm_fzr(self, fzr):
        fzr_xp = u"//input[@name='lgXmXmzr.khfzr']"  # 负责人   文本输入框
        self.input_text(fzr_xp).send_keys(fzr)
        print u"输入 负责人: ", fzr

    def input_xm_dz(self, dz):
        dz_xp = u"//input[@name='lgXmXmzr.khdz']"  # 地址   文本输入框
        self.input_text(dz_xp).send_keys(dz)
        print u"输入 地址: ", dz

    def input_xm_yyzzzch(self, yyzzzch):
        yyzzzch_xp = u"//input[@name='lgXmXmzr.yyzzzch']"  # 营业执照注册号   文本输入框
        self.input_text(yyzzzch_xp).send_keys(yyzzzch)
        print u"输入 营业执照注册号: ", yyzzzch

    def input_xm_khfzrlxdh(self, khfzrlxdh):
        khfzrlxdh_xp = u"//input[@name='lgXmXmzr.khfzrlxdh']"  # 客户联系电话   文本输入框
        self.input_text(khfzrlxdh_xp).send_keys(khfzrlxdh)
        print u"输入 客户联系电话: ", khfzrlxdh

    def input_xm_czh(self, czh):
        czh_xp = u"//input[@name='lgXmXmzr.czh']"  # 传真号码   文本输入框
        self.input_text(czh_xp).send_keys(czh)
        print u"输入 传真号: ", czh

    def input_xm_zczj(self, zczj):
        zczj_xp = u"//input[@name='lgXmXmzr.zczj']"  # 注册资金   文本输入框
        self.input_text(zczj_xp).send_keys(zczj)
        print u"输入 注册资金: ", zczj

    # 合同信息
    def input_xm_cpxh(self, cpxh):
        cpxh_xp = u"//input[@name='lgXmHtmx.kh']"  # 产品型号   文本输入框
        self.input_text(cpxh_xp).send_keys(cpxh)
        print u"输入 产品型号: ", cpxh

    def input_xm_sl(self, sl):
        sl_xp = u"//input[@name='lgXmHtmx.sl']"  # 数量   文本输入框
        self.input_text(sl_xp).send_keys(sl)
        print u"输入 数量: ", sl

    def input_xm_dj(self, dj):
        dj_xp = u"//input[@name='lgXmHtmx.dj']"  # 单价   文本输入框
        self.input_text(dj_xp).send_keys(dj)
        print u"输入 单价: ", dj

    def input_xm_zje(self, zje):
        zje_xp = u"//input[@name='lgXmHtgl.je']"  # 总金额   文本输入框
        self.input_text(zje_xp).send_keys(zje)
        print u"输入 总金额: ", zje

    def select_xm_scdw(self, scdw):
        scdw_xp = u"//select[@id='bm']"  # 生产单位   下拉选择框
        sel = self.input_text(scdw_xp)
        Select(sel).select_by_visible_text(scdw)
        print u"选择 生产单位: ", scdw

    def select_xm_khfs(self, khfs):
        khfs_xp = u"//select[@id='khfs']"  # 考核方式   下拉选择框
        sel = self.select_box(khfs_xp)
        Select(sel).select_by_visible_text(khfs)
        print u"选择 考核方式: ", khfs

    def get_htbh_value(self):
        htbh_xp = u"//input[@id='htbh']"
        htbh_value = self.get_text_value(htbh_xp).get_attribute('value')
        print u"获取 '合同编号'的值： ", htbh_value
        return htbh_value

    def input_xm_wcrq(self, wcrq):
        wcrq_xp = u"//input[@name='lgXmHtgl.wcrq']"
        self.input_text(wcrq_xp).send_keys(wcrq)
        print u"输入 完成日期: ", wcrq

    def input_xm_fktj(self, fktj):
        fktj_xp = u"//input[@name='lgXmXmzr.fktj']"
        self.input_text(fktj_xp).send_keys(fktj)
        print u"输入 付款条件: ", fktj

    def input_xm_tbr(self, tbr):
        tbr_xp = u"//input[@name='lgXmXmzr.tbr']"
        self.input_text(tbr_xp).send_keys(tbr)
        print u"输入 填报人: ", tbr

    def input_xm_tbrlxdh(self, tbrlxdh):
        tbrlxdh_xp = u"//input[@name='lgXmXmzr.tbrlxdh']"
        self.input_text(tbrlxdh_xp).send_keys(tbrlxdh)
        print u"输入 填报人联系电话: ", tbrlxdh

    def input_xm_htfj(self, htfj):
        htfj_xp = u"//input[@id='fileHTFJ']"
        self.input_text(htfj_xp).send_keys(htfj)
        print u"输入 合同附件: ", htfj

        # 项目基本资料

    def input_xm_trldlrs(self, trldlrs):
        trldlrs_xp = u"//input[@name='lgXmXmzr.xmrs']"
        self.input_text(trldlrs_xp).send_keys(trldlrs)
        print u"输入 投入劳动力人数: ", trldlrs

    def input_xm_xmtze(self, xmtze):
        xmtze_xp = u"//input[@name='lgXmXmzr.xmje']"
        self.input_text(xmtze_xp).send_keys(xmtze)
        print u"输入 项目投资额: ", xmtze

    def input_xm_sbt(self, sbt):
        sbt_xp = u"//input[@name='lgXmXmzr.sbs']"
        self.input_text(sbt_xp).send_keys(sbt)
        print u"输入 设备台（套）: ", sbt

    def input_xm_qyzysb(self, qyzysb):
        qyzysb_xp = u"//input[@name='lgXmXmzr.zysbs']"
        self.input_text(qyzysb_xp).send_keys(qyzysb)
        print u"输入 企业自有设备: ", qyzysb

    def input_xm_khtrsb(self, khtrsb):
        khtrsb_xp = u"//input[@name='lgXmXmzr.khtrsbs']"
        self.input_text(khtrsb_xp).send_keys(khtrsb)
        print u"输入 客户投入设备: ", khtrsb

    def input_xm_xmnsr(self, xmnsr):
        xmnsr_xp = u"//input[@name='lgXmXmzr.yqnsr']"
        self.input_text(xmnsr_xp).send_keys(xmnsr)
        print u"输入 项目年收入: ", xmnsr

    def input_xm_yrjsr(self, yrjsr):
        yrjsr_xp = u"//input[@name='lgXmXmzr.yqrjysr']"
        self.input_text(yrjsr_xp).send_keys(yrjsr)
        print u"输入 月人均收入: ", yrjsr

    def input_xm_sdfzcb(self, sdfzcb):
        sdfzcb_xp = u"//input[@name='lgXmXmzr.sdfzcb']"  # 水电、房租成本费用   文本输入框
        self.input_text(sdfzcb_xp).send_keys(sdfzcb)
        print u"输入 水电、房租成本费用: ", sdfzcb

    def input_xm_lr(self, lr):
        lr_xp = u"//input[@name='lgXmXmzr.lr']"  # 利润   文本输入框
        self.input_text(lr_xp).send_keys(lr)
        print u"输入 水电、房租成本费用: ", lr

    def select_xm_fxdj(self, fxdj):
        fxdj_xp = u"//select[@id='fxdj']"
        sel = self.select_box(fxdj_xp)
        Select(sel).select_by_visible_text(fxdj)
        print u"选择 风险等级：", fxdj

    def input_xm_fxpgfj(self, fxpgfj):
        fxpgfj_xp = u"//input[@id='fileFJ']"
        self.input_text(fxpgfj_xp).send_keys(fxpgfj)
        print u"输入 风险评估附件: ", fxpgfj

    def input_xm_xmpg(self, xmpg):
        xmpg_xp = u"//textarea[@name='lgXmXmzr.xmpg']"
        self.input_text(xmpg_xp).send_keys(xmpg)
        print u"输入 项目评估: ", xmpg

    def input_xm_pgry(self, pgry):
        pgry_xp = u"//textarea[@name='lgXmXmzr.pgr']"
        self.input_text(pgry_xp).send_keys(pgry)
        print u"输入 评估人员: ", pgry

    def input_xm_bz(self, bz):
        bz_xp = u"//textarea[@name='lgXmXmzr.bz']"
        self.input_text(bz_xp).send_keys(bz)
        print u"输入 备注: ", bz


    """
        劳动项目——合同备案
    """

    def select_ht_xmmc(self, xmmc):
        xmmc_xp = u"//select[@name='lgXmHtgl.xmbh']"
        sel = self.driver.find_element_by_xpath(xmmc_xp)
        Select(sel).select_by_visible_text(xmmc)
        print "选择  项目名称：", xmmc

    def get_ht_htbh(self):
        htbh_xp = u"//input[@name='lgXmHtgl.htbh']"  # 合同编号    文本输入框
        htbh_value = self.input_text(htbh_xp).get_attribute('合同编号')
        print "获取  合同编号：", htbh_value

    def input_ht_htmc(self, htmc):
        htmc_xp = u"//input[@name='lgXmHtgl.htmc']"  # 合同名称    文本输入框
        self.input_text(htmc_xp).send_keys(htmc)
        print "输入  合同名称", htmc

    def input_ht_zje(self, zje):
        htzje_xp = u"//input[@name='lgXmHtgl.je']"  # 合同总金额    文本输入框
        self.input_text(htzje_xp).send_keys(zje)
        print "输入  总金额：", zje

    def input_ht_qdrq(self, qdrq):
        htqdrq_xp = u"//input[@name='lgXmHtgl.qdrq']"  # 合同签订日期    文本输入框
        self.input_text(htqdrq_xp).send_keys(qdrq)
        print "输入  签订日期：", qdrq

    def input_ht_wcrq(self, wcrq):
        htwcrq_xp = u"//input[@name='lgXmHtgl.wcrq']"  # 合同完成日期    文本输入框
        self.input_text(htwcrq_xp).send_keys(wcrq)
        print "输入  完成日期：", wcrq

    def select_ht_scdw(self, scdw):
        htscdw_xp = u"//select[@id='bm']"  # 合同单位    下拉选择框
        sel = self.driver.find_element_by_xpath(htscdw_xp)
        Select(sel).select_by_visible_text(scdw)
        print "选择  生产单位：", scdw

    def select_ht_khfs(self, khfs):
        htkhfs_xp = u"//select[@id='khfs']"  # 合同考核方式    下拉选择框
        sel = self.driver.find_element_by_xpath(htkhfs_xp)
        Select(sel).select_by_visible_text(khfs)
        print "选择  考核方式：", khfs

    def input_ht_khmc(self, khmc):
        khmc_xp = u"//input[@name='lgXmHtgl.khmc']"  # 客户名称        文本输入框
        self.input_text(khmc_xp).send_keys(khmc)
        print "输入  客户名称：", khmc

    def input_ht_htnr(self, htnr):
        htnr_xp = u"//textarea[@name='lgXmHtgl.htnr']"  # 合同内容    文本输入框
        self.input_text(htnr_xp).send_keys(htnr)
        print "输入  合同内容：", htnr

    def input_ht_fj(self, fj):
        fj_xp = u"//input[@name='upload' and @id = 'fileFJ']"  # 附件    文本输入框
        self.input_text(fj_xp).send_keys(fj)
        print "上传  文件路径：", fj

    # 合同--合同明细
    def input_ht_xh(self, xh):
        ssxh_xp = u"//input[@id='cpkh10']"  # 手输型号    文本输入框
        self.input_text(ssxh_xp).send_keys(xh)
        print "输入  型号：", xh

    def input_ht_ks(self, ks):
        ks_xp = u"//input[@name='cpks0']"  # 款式    文本输入框
        self.input_text(ks_xp).send_keys(ks)
        print "输入  款式：", ks

    def input_ht_gg(self, gg):
        gg_xp = u"//input[@name='ggxh0']"  # 规格    文本输入框
        self.input_text(gg_xp).send_keys(gg)
        print "输入  规格：", gg

    def input_ht_pp(self, pp):
        pp_xp = u"//input[@name='ppmc0']"  # 品牌    文本输入框
        self.input_text(pp_xp).send_keys(pp)
        print "输入  品牌：", pp

    def input_ht_sl(self, sl):
        sssl_xp = u"//input[@name='sl0']"  # 数量    文本输入框
        self.input_text(sssl_xp).send_keys(sl)
        print "输入  数量：", sl

    def input_ht_dj(self, dj):
        ssdj_xp = u"//input[@name='dj0']"  # 单价    文本输入框
        self.input_text(ssdj_xp).send_keys(dj)
        print "输入  单价：", dj
