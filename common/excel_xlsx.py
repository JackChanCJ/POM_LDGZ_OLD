# coding=utf-8
__author__ = 'JACK_CHAN'

from openpyxl import load_workbook


class Excel(object):
    """
        filename  excel文件绝对路径
        sheetname 表名
    """
    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def __str__(self):
        return self.filename

    def get_cell_value(self, columnname, which_row=1):
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

    def write_by_cell(self, columnname, which_row=1):
        self.columnname = columnname
        wb = load_workbook(self.filename)
        ws = wb[self.sheetname]

        pass


class read_xlsx(object):
    def __int__(self, filename):
        self.filename = filename

    def retrieveNoOfRows(self):
        wb = load_workbook(self.filename)
        ws = wb.get_sheet_names




        # 检索 .xlsx 文件 sheets的行数

        # 检索 .xlsx 文件 sheets的列数

        # 读取测试套件和测试用例的 SuiteToRun and CaseToRun 标志








def main():
    # filename = u'D:\\Test\\POM_LDGZ_OLD\\textdata\\登录管理.xlsx'
    filename = u"D:\\01____WorkStation\PYTHON\\POM_LDGZ_OLD\\textdata\\登录管理.xlsx"
    e = Excel(filename, '登录')
    print e

if __name__ == '__main__':
    main()


