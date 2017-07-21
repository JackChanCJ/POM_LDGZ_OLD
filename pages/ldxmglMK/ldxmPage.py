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
    sub_menu = u"劳动项目"
    mkmc = u"劳动项目与计划管理"
    add_xm_btn = u"//a[text()='新增项目']"              # 新增项目    按钮
    add_ht_btn = u"//a[text()='新增合同']"              # 新增合同    按钮

    # 劳动项目
    # 生产单位信息
    filename = u"D:\\Test\\POM_LDGZ_OLD\\textdata\\劳动项目与计划管理.xlsx"

    xmbh_input = u"//input[@name='lgXmXmzr.xmbh']"          # 项目编号   文本框获取

    xmlx_select_box = u"//select[@id='xmlx']"                   # 项目类型   下拉选择框
    xmlx = textdata.read_excel_by_cellname(
            filename,
            u'劳动项目',
            u'B2'
            )
    xmmc_select_box = u"//select[@id='selectXmmc']"             # 项目名称   下拉选择框
    xmmc = textdata.read_excel_by_cellname(
            filename,
            u'劳动项目',
            u'C2'
            )
    dwmc_input = u"//input[@name='lgXmXmzr.xmscdwmc']"             # 单位名称   文本输入框
    dwmc = textdata.read_excel_by_cellname(
            filename,
            u'劳动项目',
            u'D2'
            )
    xmfzr_input = u"//input[@name='lgXmXmzr.xmfzr']"               # 项目负责人   文本输入框
    xmfzr = textdata.read_excel_by_cellname(
            filename,
            u'劳动项目',
            u'E2'
    )
    xmfzrlxdh_input = u"//input[@name='lgXmXmzr.xmfzrlxdh']"       # 项目负责人联系电话   文本输入框
    xmfzrlxdh = textdata.read_excel_by_cellname(
            filename,
            u'劳动项目',
            u'F2'
    )

    # 客户单位信息
    hzfdwmc_input = u"//input[@name='lgXmXmzr.khdwmc']"            # 合作方单位名称   文本输入框
    hzfdwmc = textdata.read_excel_by_cellname(
            filename,
            u'客户信息',
            u'A2'
    )
    fzr_input = u"//input[@name='lgXmXmzr.khfzr']"                 # 负责人   文本输入框
    fzr = textdata.read_excel_by_cellname(
            filename,
            u'客户信息',
            u'B2'
    )
    dz_input = u"//input[@name='lgXmXmzr.khdz']"                   # 地址   文本输入框
    dz = textdata.read_excel_by_cellname(
            filename,
            u'客户信息',
            u'C2'
    )
    yyzzzch_input = u"//input[@name='lgXmXmzr.yyzzzch']"           # 营业执照注册号   文本输入框
    yyzzzch = textdata.read_excel_by_cellname(
            filename,
            u'客户信息',
            u'D2'
    )
    khlxdh_input = u"//input[@name='lgXmXmzr.khfzrlxdh']"          # 客户联系电话   文本输入框
    khlxdh = textdata.read_excel_by_cellname(
            filename,
            u'客户信息',
            u'E2'
    )
    czhm_input = u"//input[@name='lgXmXmzr.czh']"                 # 传真号码   文本输入框
    czhm = textdata.read_excel_by_cellname(
            filename,
            u'客户信息',
            u'F2'
    )
    zczj_input = u"//input[@name='lgXmXmzr.zczj']"                 # 注册资金   文本输入框
    zczj = textdata.read_excel_by_cellname(
            filename,
            u'客户信息',
            u'G2'
    )

    # 合同信息
    cpxh_input = u"//input[@name='lgXmHtmx.kh']"                   # 产品型号   文本输入框
    cpxh = textdata.read_excel_by_cellname(
            filename,
            u'合同信息',
            u'A2'
    )
    sl_input = u"//input[@name='lgXmHtmx.sl']"                     # 数量   文本输入框
    sl = textdata.read_excel_by_cellname(
            filename,
            u'合同信息',
            u'B2'
    )
    dj_input = u"//input[@name='lgXmHtmx.dj']"                     # 单价   文本输入框
    dj = textdata.read_excel_by_cellname(
            filename,
            u'合同信息',
            u'C2'
    )
    zje_input = u"//input[@name='lgXmHtgl.je']"                    # 总金额   文本输入框
    zje = textdata.read_excel_by_cellname(
            filename,
            u'合同信息',
            u'D2'
    )
    scdw_select_box = u"//select[@id='bm']"                        # 生产单位   下拉选择框
    scdw = textdata.read_excel_by_cellname(
            filename,
            u'合同信息',
            u'E2'
    )
    khfs_select_box = u"//select[@id='khfs']"                      # 考核方式   下拉选择框
    khfs = textdata.read_excel_by_cellname(
            filename,
            u'合同信息',
            u'F2'
    )
    # htbh_input = u"//input[@name='lgXmHtgl.htbh']"               # 合同编号   文本输入框
    wcrq_input = u"//input[@name='lgXmHtgl.wcrq']"                 # 完成日期   文本输入框
    wcrq = textdata.read_excel_by_cellname(
            filename,
            u'合同信息',
            u'H2'
    )
    fktj_input = u"//input[@name='lgXmXmzr.fktj']"                 # 付款条件   文本输入框
    fktj = textdata.read_excel_by_cellname(
            filename,
            u'合同信息',
            u'I2'
    )
    tbr_input = u"//input[@name='lgXmXmzr.tbr']"                   # 填报人   文本输入框
    tbr = textdata.read_excel_by_cellname(
            filename,
            u'合同信息',
            u'J2'
    )
    tbrlxdh_input = u"//input[@name='lgXmXmzr.tbrlxdh']"           # 填报人联系电话   文本输入框
    tbrlxdh = textdata.read_excel_by_cellname(
            filename,
            u'合同信息',
            u'K2'
    )
    htfj_input = u"//input[@id='fileHTFJ']"                        # 合同附件   文本输入框
    htfj = textdata.read_excel_by_cellname(
            filename,
            u'合同信息',
            u'L2'
    )

    # 项目基本资料
    trldlrs_input = u"//input[@name='lgXmXmzr.xmrs']"              # 投入劳动力人数   文本输入框
    trldlrs = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'A2'
    )
    xmtze_input = u"//input[@name='lgXmXmzr.xmje']"                # 项目投资额   文本输入框
    xmtze = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'B2'
    )
    sbs_input = u"//input[@name='lgXmXmzr.sbs']"                   # 设备台（套）   文本输入框
    sbs = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'C2'
    )
    qyzysb_input = u"//input[@name='lgXmXmzr.zysbs']"              # 企业自有设备   文本输入框
    qyzysb = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'D2'
    )
    khtrsb_input = u"//input[@name='lgXmXmzr.khtrsbs']"            # 客户投入设备   文本输入框
    khtrsb = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'E2'
    )
    xmnsr_input = u"//input[@name='lgXmXmzr.yqnsr']"               # 项目年收入   文本输入框
    xmnsr = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'F2'
    )
    yrjsr_input = u"//input[@name='lgXmXmzr.yqrjysr']"             # 月人均收入   文本输入框
    yrjsr = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'G2'
    )
    sdfzcb_input = u"//input[@name='lgXmXmzr.sdfzcb']"             # 水电、房租成本费用   文本输入框
    sdfzcb = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'H2'
    )
    lr_input = u"//input[@name='lgXmXmzr.lr']"                     # 利润   文本输入框
    lr = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'I2'
    )
    fxdj_select_box = u"//select[@id='fxdj']"                   # 风险等级    下拉选择框
    fxdj = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'J2'
    )
    fxpgfj_input = u"//input[@id='fileFJ']"                        # 风险评估附件    文本输入框
    fxpgfj = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'K2'
    )
    xmpg_textarea = u"//textarea[@name='lgXmXmzr.xmpg']"           # 项目评估    文本区域
    xmpg = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'L2'
    )
    pgry_textarea = u"//textarea[@name='lgXmXmzr.pgr']"            # 评估人员    文本区域
    pgry = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'M2'
    )
    bz_textarea = u"//textarea[@name='lgXmXmzr.bz']"               # 备注    文本区域
    bz = textdata.read_excel_by_cellname(
            filename,
            u'项目基本资料',
            u'N2'
    )

    # 劳动项目详情页按钮
    bc_btn = u"//input[@value='保 存']"                # 保存    按钮
    qx_btn = u"//input[@value='取 消 ']"               # 取消    按钮

    def __init__(self, driver):
        Page.__init__(self, driver)

    def enter_ldxm_page(self):
        self.enter_sub_menu(self.sub_menu, self.mkmc)
        print u"进入  %s-->%s  页面" %(self.sub_menu, self.mkmc)

    def click_create_xm_btn(self):
        print u"点击 新增劳动项目按钮，跳转至劳动项目页面"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        self.click(self.add_xm_btn)

    def create_xm(self):
        # xmlx, xmmc, dwmc, xmfzr, xmfzrlxdh,                                     # 劳动项目
        # hzfdwmc, fzr, dz, yyzzzch, khlxdh, czhm, zczj,                          # 客户信息
        # cpxh, sl, dj, zje, scdw, khfs, wcrq, fktj, tbr, tbrlxdh, htfj,          # 合同信息
        #
        # trldlrs, xmtze, sbs, qyzysb, khtrsb, xmnsr,                             # 项目基本资料
        # yrjsr, sdfzcb, lr, fxdj, fxpgfj, xmpg, pgry, bz

        # 生产单位信息
        print u"填写 劳动项目各字段"
        # 获取劳动项目页面中项目编号的值并填写入excle中
        xmbh_value = self.get_input_text(self.xmbh_input, attribute = "value")
        print u"获取的项目编号的值: ", xmbh_value
        textdata.write_excel_by_cellname(w_value= xmbh_value,
                                         filename = self.filename,
                                         sheet_index = 0,
                                         cell_num = 'A2'
                                         )
        textdata.write_excel_by_cellname(w_value= xmbh_value,
                                         filename = self.filename,
                                         sheet_index = 4,
                                         cell_num = 'A2'
                                         )
        print u"选择 项目类型：", self.xmlx
        self.select_box(self.xmlx_select_box, self.xmlx)
        print u"选择 项目名称：", self.xmmc
        self.select_box(self.xmmc_select_box, self.xmmc)
        print u"输入 单位名称: ", self.dwmc
        self.input_text(self.dwmc_input, self.dwmc)
        print u"输入 项目负责人: ", self.xmfzr
        self.input_text(self.xmfzr_input, self.xmfzr)
        print u"输入 项目负责人联系电话: ", self.xmfzrlxdh
        self.input_text(self.xmfzrlxdh_input, self.xmfzrlxdh)

        #  客户信息
        print u"输入 合作方单位名称: ", self.hzfdwmc
        self.input_text(self.hzfdwmc_input, self.hzfdwmc)
        print u"输入 负责人: ", self.fzr
        self.input_text(self.fzr_input, self.fzr)
        print u"输入 地址: ", self.dz
        self.input_text(self.dz_input, self.dz)
        print u"输入 营业执照注册号: ", self.yyzzzch
        self.input_text(self.yyzzzch_input, self.yyzzzch)
        print u"输入 客户联系电话: ", self.khlxdh
        self.input_text(self.khlxdh_input, self.khlxdh)
        print u"输入 传真号: ", self.czhm
        self.input_text(self.czhm_input, self.czhm)
        print u"输入 注册资金: ", self.zczj
        self.input_text(self.zczj_input, self.zczj)

        #  合同信息
        print u"输入 产品型号: ", self.cpxh
        self.input_text(self.cpxh_input, self.cpxh)
        print u"输入 数量: ", self.sl
        self.input_text(self.sl_input, self.sl)
        print u"输入 单价: ", self.dj
        self.input_text(self.dj_input, self.dj)
        print u"输入 总金额: ", self.zje
        self.input_text(self.zje_input, self.zje)
        print u"输入 生产单位: ", self.scdw
        self.select_box(self.scdw_select_box, self.scdw)
        print u"输入 考核方式: ", self.khfs
        self.select_box(self.khfs_select_box, self.khfs)
        print u"输入 完成日期: ", self.wcrq
        self.input_text(self.wcrq_input, self.wcrq)
        self.driver.find_element_by_xpath(self.wcrq_input).send_keys(Keys.ESCAPE)
        print u"输入 付款条件: ", self.fktj
        self.input_text(self.fktj_input, self.fktj)
        print u"输入 填报人: ", self.tbr
        self.input_text(self.tbr_input, self.tbr)
        print u"输入 填报人联系电话: ", self.tbrlxdh
        self.input_text(self.tbrlxdh_input, self.tbrlxdh)
        print u"输入 合同附件: ", self.htfj
        self.input_text(self.htfj_input, self.htfj)

        #  项目基本资料
        print u"输入 投入劳动力人数: ", self.trldlrs
        self.input_text(self.trldlrs_input, self.trldlrs)
        print u"输入 项目投资额: ", self.xmtze
        self.input_text(self.xmtze_input, self.xmtze)
        print u"输入 设备台（套）: ", self.sbs
        self.input_text(self.sbs_input, self.sbs)
        print u"输入 企业自有设备: ", self.qyzysb
        self.input_text(self.qyzysb_input, self.qyzysb)
        print u"输入 客户投入设备: ", self.khtrsb
        self.input_text(self.khtrsb_input, self.khtrsb)
        print u"输入 项目年收入: ", self.xmnsr
        self.input_text(self.xmnsr_input, self.xmnsr)
        print u"输入 月人均收入: ", self.yrjsr
        self.input_text(self.yrjsr_input, self.yrjsr)
        print u"输入 利润: ", self.lr
        self.input_text(self.sdfzcb_input, self.sdfzcb)
        print u"输入 水电、房租成本费用: ", self.sdfzcb
        self.input_text(self.lr_input, self.lr)
        print u"输入 风险等级: ", self.fxdj
        self.select_box(self.fxdj_select_box, self.fxdj)
        print u"输入 风险评估附件: ", self.fxpgfj
        self.input_text(self.fxpgfj_input, self.fxpgfj)
        print u"输入 项目评估: ", self.xmpg
        self.input_text(self.xmpg_textarea, self.xmpg)
        print u"输入 评估人员: ", self.pgry
        self.input_text(self.pgry_textarea, self.pgry)
        print u"输入 备注: ", self.bz
        self.input_text(self.bz_textarea, self.bz)
        # 新增项目页面按钮
        print u"点击 '保存' 按钮"
        self.click(self.bc_btn)
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
        self.click(self.add_ht_btn)

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