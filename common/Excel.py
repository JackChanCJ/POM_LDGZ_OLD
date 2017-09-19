# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
from time import sleep
from pages.basePage import Page
from openpyxl import load_workbook

reload(sys)
sys.setdefaultencoding("utf-8")


class Excel():
    """
        filename  excel文件绝对路径
        sheetname 表名
    """
    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def __str__(self):
        return self.filename

    def get_cell_value(self, columnname, which_row=2):
        self.columnname = columnname
        wb = load_workbook(self.filename)
        ws = wb[self.sheetname]
        rows = ws.rows
        cols = ws.columns
        row_value = []
        col_value = []
        for i in cols:
            row_value.append(i[0].value)
        # print "取出第一行所有的列名：%s" %row_value
        if columnname in row_value:
            col_index = row_value.index(columnname)
            for i in rows:
                col_value.append(i[col_index].value)
                # print "根据列名得到索引，根据索引值获取当前列所有行的值：%s" %col_value
        else:
            print "columnname参数不在excel中，请重新赋值。"
        return col_value[which_row]


def main():
    # filename = u'D:\\Test\\POM_LDGZ_OLD\\textdata\\登录管理.xlsx'
    filename = u"D:\\01____WorkStation\PYTHON\\POM_LDGZ_OLD\\textdata\\登录管理.xlsx"
    e = Excel(filename, '登录')
    print e
    print e.get_cell_value('username')

if __name__ == '__main__':
    main()
