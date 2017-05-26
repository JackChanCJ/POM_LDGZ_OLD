# coding=utf-8
__author__ = 'JACK_CHAN'

import sys
from openpyxl import Workbook
from openpyxl import load_workbook

reload(sys)
sys.setdefaultencoding("utf-8")

def excel_table_by_cellname(
        filename,
        sheet_name,
        cell_value
        ):
    wb = load_workbook(filename)
    ws = wb.get_sheet_by_name(sheet_name)
    value = ws[cell_value].value
    return value



