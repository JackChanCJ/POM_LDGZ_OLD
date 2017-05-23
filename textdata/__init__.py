# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
import xlrd

reload(sys)
sys.setdefaultencoding("utf-8")


def open_excel(file='file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def excel_table_byname(file='file.xls',colname=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数
    colnames = table.row_values(colname) #某一行数据
    list = []
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list

def main():
    tables = excel_table_byname(file='test.xls')
    for row in tables:
        print row

if __name__=="__main__":
    main()




