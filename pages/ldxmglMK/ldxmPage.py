#  coding=utf-8
__author__ = 'JACK_CHAN'

import sys
import textdata
from pages.basePage import Page
from time import sleep
from openpyxl import Workbook
from openpyxl import load_workbook


reload(sys)
sys.setdefaultencoding("utf-8")

class LdxmPage(Page):
    mkmc = u"劳动项目与计划管理"
    ymmc = u"劳动项目"
    xm_btn = u"//a[text()='新增项目']"              # 新增项目    按钮
    ht_btn = u"//a[text()='新增合同']"              # 新增合同    按钮

    # 劳动项目
    # 生产单位信息
    filename = u"D:\\Test\\POM_LDGZ_OLD\\textdata\\劳动项目与计划管理.xlsx"
    xmlx_selection_box = u"//select[@id='xmlx']"                   # 项目类型   下拉选择框
    xmlx = textdata.excel_table_by_cellname(
            filename,
            u'劳动项目',
            u'B2'
    )
    xmmc_selection_box = u"//select[@id='selectXmmc']"             # 项目名称   下拉选择框
    xmmc = textdata.excel_table_by_cellname(
            filename,
            u'劳动项目',
            u'C2'
    )
    dwmc_input = u"//input[@name='lgXmXmzr.xmscdwmc']"             # 单位名称   文本输入框
    dwmc = textdata.excel_table_by_cellname(
            filename,
            u'劳动项目',
            u'D2'
    )
    xmfzr_input = u"//input[@name='lgXmXmzr.xmfzr']"               # 项目负责人   文本输入框
    xmfzr = textdata.excel_table_by_cellname(
            filename,
            u'劳动项目',
            u'E2'
    )
    xmfzrlxdh_input = u"//input[@name='lgXmXmzr.xmfzrlxdh']"       # 项目负责人联系电话   文本输入框
    xmfzrlxdh = textdata.excel_table_by_cellname(
            filename,
            u'劳动项目',
            u'F2'
    )

    # 客户单位信息
    hzfdwmc_input = u"//input[@name='lgXmXmzr.khdwmc']"            # 合作方单位名称   文本输入框
    hzfdwmc = textdata.excel_table_by_cellname(
            filename,
            u'客户信息',
            u'A2'
    )
    fzr_input = u"//input[@name='lgXmXmzr.khfzr']"                 # 负责人   文本输入框
    fzr = textdata.excel_table_by_cellname(
            filename,
            u'客户信息',
            u'B2'
    )
    dz_input = u"//input[@name='lgXmXmzr.khdz']"                   # 地址   文本输入框
    dz = textdata.excel_table_by_cellname(
            filename,
            u'客户信息',
            u'C2'
    )
    yyzzzch_input = u"//input[@name='lgXmXmzr.yyzzzch']"           # 营业执照注册号   文本输入框
    yyzzzch = textdata.excel_table_by_cellname(
            filename,
            u'客户信息',
            u'D2'
    )
    khlxdh_input = u"//input[@name='lgXmXmzr.khfzrlxdh']"          # 客户联系电话   文本输入框
    khlxdh = textdata.excel_table_by_cellname(
            filename,
            u'客户信息',
            u'E2'
    )
    czhm_input = u"//input[@name='lgXmXmzr.czhm']"                 # 传真号码   文本输入框
    czhm = textdata.excel_table_by_cellname(
            filename,
            u'客户信息',
            u'F2'
    )
    zczj_input = u"//input[@name='lgXmXmzr.zczj']"                 # 注册资金   文本输入框
    zczj = textdata.excel_table_by_cellname(
            filename,
            u'客户信息',
            u'G2'
    )

    # 合同信息
    cpxh_input = u"//input[@name='lgXmHtmx.kh']"                   # 产品型号   文本输入框
    cpxh = textdata.excel_table_by_cellname(
            filename,
            u'合同信息',
            u'A2'
    )
    sl_input = u"//input[@name='lgXmHtmx.sl']"                     # 数量   文本输入框
    sl = textdata.excel_table_by_cellname(
            filename,
            u'合同信息',
            u'B2'
    )
    dj_input = u"//input[@name='lgXmHtmx.dj']"                     # 单价   文本输入框
    dj = textdata.excel_table_by_cellname(
            filename,
            u'合同信息',
            u'C2'
    )
    zje_input = u"//input[@name='lgXmHtgl.je']"                    # 总金额   文本输入框
    zje = textdata.excel_table_by_cellname(
            filename,
            u'合同信息',
            u'D2'
    )
    scdw_selection_box = u"//select[@id='bm']"                     # 生产单位   下拉选择框
    scdw = textdata.excel_table_by_cellname(
            filename,
            u'合同信息',
            u'E2'
    )
    khfs_selection_box = u"//select[@id='khfs']"                   # 考核方式   下拉选择框
    khfs = textdata.excel_table_by_cellname(
            filename,
            u'合同信息',
            u'F2'
    )
    # htbh_input = u"//input[@name='lgXmHtgl.htbh']"               # 合同编号   文本输入框
    wcrq_input = u"//input[@name='lgXmHtgl.wcrq']"                 # 完成日期   文本输入框
    wcrq = textdata.excel_table_by_cellname(
            filename,
            u'合同信息',
            u'H2'
    )
    fktj_input = u"//input[@name='lgXmXmzr.fktj']"                 # 付款条件   文本输入框
    fktj = textdata.excel_table_by_cellname(
            filename,
            u'合同信息',
            u'I2'
    )
    tbr_input = u"//input[@name='lgXmXmzr.tbr']"                   # 填报人   文本输入框
    tbr = textdata.excel_table_by_cellname(
            filename,
            u'合同信息',
            u'J2'
    )
    tbrlxdh_input = u"//input[@name='lgXmXmzr.tbrlxdh']"           # 填报人联系电话   文本输入框
    tbrlxdh = textdata.excel_table_by_cellname(
            filename,
            u'合同信息',
            u'K2'
    )
    htfj_input = u"//input[@id='fileHTFJ']"                        # 合同附件   文本输入框
    htfj = textdata.excel_table_by_cellname(
            filename,
            u'合同信息',
            u'L2'
    )

    # 项目基本资料
    trldlrs_input = u"//input[@name='lgXmXmzr.xmrs']"              # 投入劳动力人数   文本输入框
    trldlrs = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'A2'
    )
    xmtze_input = u"//input[@name='lgXmXmzr.xmje']"                # 项目投资额   文本输入框
    trldlrs = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'B2'
    )
    sbs_input = u"//input[@name='lgXmXmzr.sbs']"                   # 设备台（套）   文本输入框
    sbs = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'C2'
    )
    qyzysb_input = u"//input[@name='lgXmXmzr.zysbs']"              # 企业自有设备   文本输入框
    qyzysb = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'D2'
    )
    khtrsb_input = u"//input[@name='lgXmXmzr.khtrsbs']"            # 客户投入设备   文本输入框
    khtrsb = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'E2'
    )
    xmnsr_input = u"//input[@name='lgXmXmzr.yqnsr']"               # 项目年收入   文本输入框
    xmnsr = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'F2'
    )
    yrjsr_input = u"//input[@name='lgXmXmzr.yqrjysr']"             # 月人均收入   文本输入框
    yrjsr = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'G2'
    )
    sdfzcb_input = u"//input[@name='lgXmXmzr.sdfzcb']"             # 水电、房租成本费用   文本输入框
    sdfzcb = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'H2'
    )
    lr_input = u"//input[@name='lgXmXmzr.lr']"                     # 利润   文本输入框
    lr = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'I2'
    )
    fxdj_selection_box = u"//select[@id='fxdj']"                   # 风险等级    下拉选择框
    fxdj = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'J2'
    )
    fxpgfj_input = u"//input[@id='fileFJ']"                        # 风险评估附件    文本输入框
    fxpgfj = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'K2'
    )
    xmpg_textarea = u"//textarea[@name='lgXmXmzr.xmpg']"           # 项目评估    文本区域
    xmpg = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'L2'
    )
    pgry_textarea = u"//textarea[@name='lgXmXmzr.pgr']"            # 评估人员    文本区域
    pgry = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'M2'
    )
    bz_textarea = u"//textarea[@name='lgXmXmzr.bz']"               # 备注    文本区域
    bz = textdata.excel_table_by_cellname(
            filename,
            u'项目基本资料',
            u'N2'
    )

    # 劳动项目详情页按钮
    bc_btn = u"//input[@value='保 存']"                # 保存    按钮
    qx_btn = u"//input[@value='取 消 ']"               # 取消    按钮

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

    def write_xm(self,
                 xmlx, xmmc, dwmc, xmfzr, xmfzrlxdh,
                 hzfdwmc, fzr, dz, yyzzzch, khlxdh, czhm, zczj,
                 cpxh, sl, dj, zje, scdw, khfs, wcrq, fktj, tbr, tbrlxdh, htfj,

                 trldlrs, xmtze, sbs, qyzysb, khtrsb, xmnsr,
                 yrjsr, sdfzcb, lr, fxdj, fxpgfj, xmpg, pgry, bz
                 ):

        #  生产单位信息
        print u"填写 劳动项目各字段"
        print u"选择 项目类型：", xmlx
        self.select_box(self.xmlx_selection_box, xmlx)
        print u"选择 项目名称：", xmmc
        self.select_box(self.xmmc_selection_box, xmmc)
        print u"输入 单位名称: ", dwmc
        self.input_text(self.dwmc_input, dwmc)
        print u"输入 项目负责人: ", dwmc
        self.input_text(self.xmfzr_input, xmfzr)
        print u"输入 项目负责人联系电话: ", xmfzrlxdh
        self.input_text(self.xmfzrlxdh_input, xmfzrlxdh)

        #  客户单位信息
        print u"输入 合作方单位名称: ", hzfdwmc
        self.input_text(self.hzfdwmc_input, hzfdwmc)
        print u"输入 负责人: ", fzr
        self.input_text(self.dz_input, dz)
        print u"输入 地址: ", dz
        self.input_text(self.fzr_input, fzr)
        print u"输入 营业执照注册号: ", yyzzzch
        self.input_text(self.yyzzzch_input, yyzzzch)
        print u"输入 客户联系电话: ", khlxdh
        self.input_text(self.khlxdh_input, khlxdh)
        print u"输入 传真号: ", czhm
        self.input_text(self.czhm_input, czhm)
        print u"输入 注册资金: ", zczj
        self.input_text(self.zczj_input, zczj)

        #  合同信息
        print u"输入 产品型号: ", cpxh
        self.input_text(self.cpxh_input, cpxh)
        print u"输入 数量: ", sl
        self.input_text(self.sl_input, sl)
        print u"输入 单价: ", dj
        self.input_text(self.dj_input, dj)
        print u"输入 总金额: ", zje
        self.input_text(self.zje_input, zje)
        print u"输入 生产单位: ", scdw
        self.select_box(self.scdw_selection_box, scdw)
        print u"输入 考核方式: ", khfs
        self.select_box(self.khfs_selection_box, khfs)
        print u"输入 完成日期: ", wcrq
        self.input_text(self.wcrq_input, wcrq)
        print u"输入 付款条件: ", fktj
        self.input_text(self.fktj_input, fktj)
        print u"输入 填报人: ", tbr
        self.input_text(self.tbr_input, tbr)
        print u"输入 填报人联系电话: ", tbrlxdh
        self.input_text(self.tbrlxdh_input, tbrlxdh)
        print u"输入 合同附件: ", htfj
        self.input_text(self.htfj_input, htfj)

        #  项目基本资料
        print u"输入 投入劳动力人数: ", trldlrs
        self.input_text(self.trldlrs_input, trldlrs)
        print u"输入 项目投资额: ", xmtze
        self.input_text(self.xmtze_input, xmtze)
        print u"输入 设备台（套）: ", sbs
        self.input_text(self.sbs_input, sbs)
        print u"输入 企业自有设备: ", qyzysb
        self.input_text(self.qyzysb_input, qyzysb)
        print u"输入 客户投入设备: ", khtrsb
        self.input_text(self.khtrsb_input, khtrsb)
        print u"输入 项目年收入: ", xmnsr
        self.input_text(self.xmnsr_input, xmnsr)
        print u"输入 月人均收入: ", yrjsr
        self.input_text(self.yrjsr_input, yrjsr)
        print u"输入 利润: ", lr
        self.input_text(self.sdfzcb_input, sdfzcb)
        print u"输入 水电、房租成本费用: ", sdfzcb
        self.input_text(self.lr_input, lr)
        print u"输入 风险等级: ", fxdj
        self.select_box(self.fxdj_selection_box, fxdj)
        print u"输入 风险评估附件: ", fxpgfj
        self.input_text(self.fxpgfj_input, fxpgfj)
        print u"输入 项目评估: ", xmpg
        self.input_text(self.xmpg_textarea, xmpg)
        print u"输入 评估人员: ", pgry
        self.input_text(self.pgry_textarea, pgry)
        print u"输入 备注: ", bz
        self.input_text(self.bz_textarea, bz)

        # 新增项目页面按钮
        print u"点击 保存 按钮: "
        self.click(self.bc_btn)
        print u"保存后，等待5秒！"
        sleep(5)

    def click_create_ht_btn(self):
        print u"点击 新增劳动合同,跳转至劳动合同页面"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("right_mainFrame")
        self.click(self.ht_btn)




