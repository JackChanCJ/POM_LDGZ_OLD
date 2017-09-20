#  coding=utf-8
__author__ = 'JACK_CHAN'

import sys
import textdata
import re
from pages.basePage import Page
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


reload(sys)
sys.setdefaultencoding("utf-8")

class LdxmPage(Page):
    sub_menu = u"劳动项目与计划管理"
    sub_page = u"劳动项目"
    filename = u"D:\\Test\\POM_LDGZ_OLD\\textdata\\劳动项目与计划管理.xlsx"
    # filename = u"D:\\01____WorkStation\PYTHON\\POM_LDGZ_OLD\\textdata\\劳动项目与计划管理.xlsx"

    # 劳动项目与计划管理-->劳动项目页面
    add_xm_xp = u"//a[text()='新增项目']"  # 新增项目    按钮
    add_ht_xp = u"//a[text()='新增合同']"  # 新增合同    按钮

    # 劳动项目详情页按钮
    xmbc_xp = u"//input[@value='保 存']"  # 保存    按钮
    xmqx_xp = u"//input[@value='取 消 ']"  # 取消    按钮

    def __init__(self, driver):
        Page.__init__(self, driver)

    def enter_ldxm_sub_page(self):
        self.enter_sub_menu(self.sub_menu, self.sub_page)
        print u"进入  %s-->%s  页面" % (self.sub_menu, self.sub_page)

    def click_create_xm_btn(self):
        print u"点击 新增劳动项目按钮，跳转至劳动项目页面"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        self.click(self.add_xm_btn)

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

    def select_xmlx(self, xmlx):
        xmlx_xp = u"//select[@id='xmlx']"  # 项目类型   下拉选择框
        sel = self.select_box(xmlx_xp)
        Select(sel).select_by_visible_text(xmlx)
        print u"选择 项目类型：", xmlx

    def select_xmmc(self, xmmc):
        xmmc_xp = u"//select[@id='selectXmmc']"  # 项目名称   下拉选择框
        sel = self.select_box(xmmc_xp)
        Select(sel).select_by_visible_text(xmmc)
        print u"选择 项目名称：", xmmc

    def input_dwmc(self, dwmc):
        dwmc_xp = u"//input[@name='lgXmXmzr.xmscdwmc']"  # 单位名称   文本输入
        self.input_text(dwmc_xp).send_keys(dwmc)
        print u"输入 单位名称: ", dwmc

    def input_xmfzr(self, xmfzr):
        xmfzr_xp = u"//input[@name='lgXmXmzr.xmfzr']"  # 项目负责人   文本输入框
        self.input_text(xmfzr_xp).send_keys(xmfzr)
        print u"输入 项目负责人: ", xmfzr

    def input_lxdh(self, xmfzrlxdh):
        xmfzrlxdh_xp = u"//input[@name='lgXmXmzr.xmfzrlxdh']"  # 项目负责人联系电话   文本输入框
        self.input_text(xmfzrlxdh_xp).send_keys(xmfzrlxdh)
        print u"输入 项目负责人联系电话: ", xmfzrlxdh

    # 客户单位信息
    def input_hzfdwmc(self, hzfdwmc):
        hzfdwmc_xp = u"//input[@name='lgXmXmzr.khdwmc']"  # 合作方单位名称   文本输入框
        self.input_text(hzfdwmc_xp).send_keys(hzfdwmc)
        print u"输入 合作方单位名称: ", hzfdwmc

    def input_fzr(self, fzr):
        fzr_xp = u"//input[@name='lgXmXmzr.khfzr']"  # 负责人   文本输入框
        self.input_text(fzr_xp).send_keys(fzr)
        print u"输入 负责人: ", fzr

    def input_dz(self, dz):
        dz_xp = u"//input[@name='lgXmXmzr.khdz']"  # 地址   文本输入框
        self.input_text(dz_xp).send_keys(dz)
        print u"输入 地址: ", dz

    def input_yyzzzch(self, yyzzzch):
        yyzzzch_xp = u"//input[@name='lgXmXmzr.yyzzzch']"  # 营业执照注册号   文本输入框
        self.input_text(yyzzzch_xp).send_keys(yyzzzch)
        print u"输入 营业执照注册号: ", yyzzzch

    def input_khlxdh(self, khlxdh):
        khlxdh_xp = u"//input[@name='lgXmXmzr.khfzrlxdh']"  # 客户联系电话   文本输入框
        self.input_text(khlxdh_xp).send_keys(khlxdh)
        print u"输入 客户联系电话: ", khlxdh

    def input_czhm(self, czhm):
        czhm_xp = u"//input[@name='lgXmXmzr.czh']"  # 传真号码   文本输入框
        self.input_text(czhm_xp).send_keys(czhm)
        print u"输入 传真号: ", czhm

    def input_zczj(self, zczj):
        zczj_xp = u"//input[@name='lgXmXmzr.zczj']"  # 注册资金   文本输入框
        self.input_text(zczj_xp).send_keys(zczj)
        print u"输入 注册资金: ", zczj

    # 合同信息
    def input_cpxh(self, cpxh):
        cpxh_xp = u"//input[@name='lgXmHtmx.kh']"  # 产品型号   文本输入框
        self.input_text(cpxh_xp).send_keys(cpxh)
        print u"输入 产品型号: ", cpxh

    def input_sl(self, sl):
        sl_xp = u"//input[@name='lgXmHtmx.sl']"  # 数量   文本输入框
        self.input_text(sl_xp).send_keys(sl)
        print u"输入 数量: ", sl

    def input_dj(self, dj):
        dj_xp = u"//input[@name='lgXmHtmx.dj']"  # 单价   文本输入框
        self.input_text(dj_xp).send_keys(dj)
        print u"输入 单价: ", dj

    def input_zje(self, zje):
        zje_xp = u"//input[@name='lgXmHtgl.je']"  # 总金额   文本输入框
        self.input_text(zje_xp).send_keys(zje)
        print u"输入 总金额: ", zje

    def select_scdw(self, scdw):
        scdw_xp = u"//select[@id='bm']"  # 生产单位   下拉选择框
        sel = self.input_text(scdw_xp)
        Select(sel).select_by_visible_text(scdw)
        print u"选择 生产单位: ", scdw

    def select_khfs(self, khfs):
        khfs_xp = u"//select[@id='khfs']"  # 考核方式   下拉选择框
        sel = self.select_box(khfs_xp)
        Select(sel).select_by_visible_text(khfs)
        print u"选择 考核方式: ", khfs

    def get_htbh_value(self):
        htbh_xp = u"//input[id()='htbh']"
        htbh_value = self.get_text_value(htbh_xp).get_attribute('合同编号')
        print u"获取'合同编号'的值： ", htbh_value
        return htbh_value

    def input_wcrq(self, wcrq):
        wcrq_xp = u"//input[@name='lgXmHtgl.wcrq']"
        self.input_text(wcrq_xp).send_keys(wcrq)
        print u"输入 完成日期: ", wcrq

    def input_fktj(self, fktj):
        fktj_xp = u"//input[@name='lgXmXmzr.fktj']"
        self.input_text(fktj_xp).send_keys(fktj)
        print u"输入 付款条件: ", fktj

    def input_tbr(self, tbr):
        tbr_xp = u"//input[@name='lgXmXmzr.tbr']"
        self.input_text(tbr_xp).send_keys(tbr)
        print u"输入 填报人: ", tbr

    def input_tbrlxdh(self, tbrlxdh):
        tbrlxdh_xp = u"//input[@name='lgXmXmzr.tbrlxdh']"
        self.input_text(tbrlxdh_xp).send_keys(tbrlxdh)
        print u"输入 填报人联系电话: ", tbrlxdh

    def input_htfj(self, htfj):
        htfj_xp = u"//input[@id='fileHTFJ']"
        self.input_text(htfj_xp).send_keys(htfj)
        print u"输入 合同附件: ", htfj

        # 项目基本资料

    def input_trldlrs(self, trldlrs):
        trldlrs_xp = u"//input[@name='lgXmXmzr.xmrs']"
        self.input_text(trldlrs_xp).send_keys(trldlrs)
        print u"输入 投入劳动力人数: ", trldlrs

    def input_xmtze(self, xmtze):
        xmtze_xp = u"//input[@name='lgXmXmzr.xmje']"
        self.input_text(xmtze_xp).send_keys(xmtze)
        print u"输入 项目投资额: ", xmtze

    def input_sbt(self, sbt):
        sbt_xp = u"//input[@name='lgXmXmzr.sbs']"
        self.input_text(sbt_xp).send_keys(sbt)
        print u"输入 设备台（套）: ", sbt

    def input_qyzysb(self, qyzysb):
        qyzysb_xp = u"//input[@name='lgXmXmzr.zysbs']"
        self.input_text(qyzysb_xp).send_keys(qyzysb)
        print u"输入 企业自有设备: ", qyzysb

    def input_khtrsb(self, khtrsb):
        khtrsb_xp = u"//input[@name='lgXmXmzr.khtrsbs']"
        self.input_text(khtrsb_xp).send_keys(khtrsb)
        print u"输入 客户投入设备: ", khtrsb

    def input_xmnsr(self, xmnsr):
        xmnsr_xp = u"//input[@name='lgXmXmzr.yqnsr']"
        self.input_text(xmnsr_xp).send_keys(xmnsr)
        print u"输入 项目年收入: ", xmnsr

    def input_yrjsr(self, yrjsr):
        yrjsr_xp = u"//input[@name='lgXmXmzr.yqrjysr']"
        self.input_text(yrjsr_xp).send_keys(yrjsr)
        print u"输入 月人均收入: ", yrjsr

    def input_sdfzdfy(self, sdfzcb):
        sdfzcb_xp = u"//input[@name='lgXmXmzr.sdfzcb']"  # 水电、房租成本费用   文本输入框
        self.input_text(sdfzcb_xp).send_keys(sdfzcb)
        print u"输入 水电、房租成本费用: ", sdfzcb

    def input_sdfzcb(self, sdfzcb):
        sdfzcb_xp = u"//input[@name='lgXmXmzr.lr']"  # 水电、房租成本费用   文本输入框
        self.input_text(sdfzcb_xp).send_keys(sdfzcb)
        print u"输入 水电、房租成本费用: ", sdfzcb

    def select_fxdj(self, fxdj):
        fxdj_xp = u"//select[@id='fxdj']"
        sel = self.select_box(fxdj_xp)
        Select(sel).select_by_visible_text(fxdj)
        print u"选择 风险等级：", fxdj

    def input_fxpgfj(self, fxpgfj):
        fxpgfj_xp = u"//input[@id='fileFJ']"
        self.input_text(fxpgfj_xp).send_keys(fxpgfj)
        print u"输入 风险评估附件: ", fxpgfj

    def input_xmpg(self, xmpg):
        xmpg_xp = u"//textarea[@name='lgXmXmzr.xmpg']"
        self.input_text(xmpg_xp).send_keys(xmpg)
        print u"输入 项目评估: ", xmpg

    def input_pgry(self, pgry):
        pgry_xp = u"//textarea[@name='lgXmXmzr.pgr']"
        self.input_text(pgry_xp).send_keys(pgry)
        print u"输入 风险评估附件: ", pgry

    def input_bz(self, bz):
        bz_xp = u"//textarea[@name='lgXmXmzr.bz']"
        self.input_text(bz_xp).send_keys(bz)
        print u"输入 备注: ", bz

    def create_xm(self):
        # xmlx, xmmc, dwmc, xmfzr, xmfzrlxdh,                                     # 劳动项目
        # hzfdwmc, fzr, dz, yyzzzch, khlxdh, czhm, zczj,                          # 客户信息
        # cpxh, sl, dj, zje, scdw, khfs, wcrq, fktj, tbr, tbrlxdh, htfj,          # 合同信息
        #
        # trldlrs, xmtze, sbs, qyzysb, khtrsb, xmnsr,                             # 项目基本资料
        # yrjsr, sdfzcb, lr, fxdj, fxpgfj, xmpg, pgry, bz

        # 生产单位信息
        # 新增项目页面按钮
        print u"点击 '保存' 按钮"
        # self.click(self.bc_btn)
        sleep(3)

    """
        劳动项目——合同备案
    """
    # 合同备案新增页面按钮
    ht_save = u"//input[@type='button' and @value='保 存']"            # 保存按钮
    ht_cancel = u"//input[@value='保存' and @type='button']"          # 取消按钮
    xmbh_select_ele = u"//select[@name='lgXmHtgl.xmbh']/option"     # 合同项目编号    下拉选择框option元素
    xmbh_select_box = u"//select[@name='lgXmHtgl.xmbh']"            # 合同项目编号    下拉选择框
    xmbh = textdata.read_excel_by_cellname(
        filename,
        u"劳动合同",
        u"A2"
        )
    # xmbh = re.search(re_obj, re_xmbh)
    htbh_input = u"//input[@name='lgXmHtgl.htbh']"                 # 合同编号    文本输入框
    htbh = textdata.read_excel_by_cellname(
        filename,
        u"劳动合同",
        u"B2"
        )
    htmc_input = u"//input[@name='lgXmHtgl.htmc']"                  # 合同名称    文本输入框
    htmc = textdata.read_excel_by_cellname(
        filename,
        u"劳动合同",
        u"C2"
        )
    htzje_input = u"//input[@name='lgXmHtgl.je']"                   # 合同总金额    文本输入框
    htzje = textdata.read_excel_by_cellname(
        filename,
        u"劳动合同",
        u"D2"
        )
    htqdrq_input = u"//input[@name='lgXmHtgl.qdrq']"                # 合同签订日期    文本输入框
    htqdrq = textdata.read_excel_by_cellname(
        filename,
        u"劳动合同",
        u"E2"
        )
    htwcrq_input = u"//input[@name='lgXmHtgl.wcrq']"                # 合同完成日期    文本输入框
    htwcrq = textdata.read_excel_by_cellname(
        filename,
        u"劳动合同",
        u"F2"
        )
    htscdw_select_box = u"//select[@id='bm']"                       # 合同单位    下拉选择框
    htscdw = textdata.read_excel_by_cellname(
        filename,
        u"劳动合同",
        u"G2"
        )
    htkhfs_select_box = u"//select[@id='khfs']"                     # 合同考核方式    下拉选择框
    htkhfs = textdata.read_excel_by_cellname(
        filename,
        u"劳动合同",
        u"H2"
        )
    htkhfs_add_btn = u"//input[@id='addScdwBtn']"                   # 合同考核方式    添加按钮

    khmc_input = u"//input[@name='lgXmHtgl.khmc']"                  # 客户名称        文本输入框
    khmc = textdata.read_excel_by_cellname(
        filename,
        u"劳动合同",
        u"I2"
        )
    htnr_textarea = u"//textarea[@name='lgXmHtgl.htnr']"            # 合同内容    文本输入框
    htnr = textdata.read_excel_by_cellname(
        filename,
        u"劳动合同",
        u"J2"
        )
    fj_input = u"//input[@name='upload' and @id = 'fileFJ']"        # 附件    文本输入框
    fj = textdata.read_excel_by_cellname(
        filename,
        u"劳动合同",
        u"K2"
        )

    # 合同明细
    ssxh_input = u"//input[@id='cpkh10']"                         # 手输型号    文本输入框
    ssxh = textdata.read_excel_by_cellname(
        filename,
        u"合同明细",
        u"A2"
        )
    ks_input = u"//input[@name='cpks0']"                            # 款式    文本输入框
    ks = textdata.read_excel_by_cellname(
        filename,
        u"合同明细",
        u"B2"
        )
    gg_input = u"//input[@name='ggxh0']"                            # 规格    文本输入框
    gg = textdata.read_excel_by_cellname(
        filename,
        u"合同明细",
        u"C2"
        )
    pp_input = u"//input[@name='ppmc0']"                            # 品牌    文本输入框
    pp = textdata.read_excel_by_cellname(
        filename,
        u"合同明细",
        u"D2"
        )
    sssl_input = u"//input[@name='sl0']"                          # 数量    文本输入框
    sssl = textdata.read_excel_by_cellname(
        filename,
        u"合同明细",
        u"E2"
        )
    ssdj_input = u"//input[@name='dj0']"                          # 单价    文本输入框
    ssdj = textdata.read_excel_by_cellname(
        filename,
        u"合同明细",
        u"F2"
        )

    def click_create_ht_btn(self):
        print u"点击 新增劳动合同,跳转至劳动合同页面"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        # self.click(self.add_ht_xp)

    def create_ht(self):
        print u"填写 项目合同的各字段"
        xmbhs_ele = self.driver.find_elements_by_xpath(self.xmbh_select_ele)
        for xmbh_ele in xmbhs_ele:
            xmbh_value = xmbh_ele.get_attribute('value')
            if xmbh_value == self.xmbh:
                Select(self.driver.find_element_by_xpath(self.xmbh_select_box))\
                    .select_by_value(self.xmbh)
                print u"选择 合同项目编号: ", xmbh_value
        # 获取合同编号的值，写入excel
        htbh_value = self.driver.find_element_by_xpath(self.htbh_input).get_attribute('value')
        textdata.write_excel_by_cellname(w_value=htbh_value,
                                         filename=self.filename,
                                         sheet_index=4,
                                         cell_num='B2'
                                         )
        print u"填写 合同编号: ", htbh_value

        print u"填写 合同名称: ", self.htmc
        self.input_text(self.htmc_input, self.htmc)
        print u"填写 合同总金额: ", self.htzje
        self.input_text(self.htzje_input, self.htzje)
        print u"填写 合同签订日期: ", self.htqdrq
        self.input_text(self.htqdrq_input, self.htqdrq)
        self.driver.find_element_by_xpath(self.htqdrq_input).send_keys(Keys.ESCAPE)
        print u"填写 合同完成日期: ", self.htwcrq
        self.input_text(self.htwcrq_input, self.htwcrq)
        self.driver.find_element_by_xpath(self.htqdrq_input).send_keys(Keys.ESCAPE)
        print u"选择 合同生产单位: ", self.htscdw
        self.select_box(self.htscdw_select_box, self.htscdw)
        print u"选择 合同考核方式: ", self.htkhfs
        self.select_box(self.htkhfs_select_box, self.htkhfs)
        print u"点击 考核方式“添加”按钮: ", self.htkhfs
        self.click(self.htkhfs_add_btn)
        print u"填写 客户名称: ", self.khmc
        self.input_text(self.khmc_input, self.khmc)
        print u"填写 合同内容: ", self.htnr
        self.input_text(self.htnr_textarea, self.htnr)
        print u"上传 附件: ", self.fj
        self.input_text(self.fj_input, self.fj)
        # 填写项目合同各字段
        print
        print u"填写 项目合同明细的各字段"
        print u"填写 手输型号: ", self.ssxh
        self.input_text(self.ssxh_input, self.ssxh)
        print u"填写 款式: ", self.ks
        self.input_text(self.ks_input, self.ks)
        print u"填写 规格: ", self.gg
        self.input_text(self.gg_input, self.gg)
        print u"填写 品牌: ", self.pp
        self.input_text(self.pp_input, self.pp)
        print u"填写 数量: ", self.sssl
        self.input_text(self.sssl_input, self.sssl)
        print u"填写 单价: ", self.ssdj
        self.input_text(self.ssdj_input, self.ssdj)
        print u"点击 '保存' 按钮"
        self.click(self.ht_save)
        sleep(3)



        # print u"选择 项目名称：", self.xmmc
        # self.select_box(self.xmmc_select_box, self.xmmc)
        # print u"输入 单位名称: ", self.dwmc