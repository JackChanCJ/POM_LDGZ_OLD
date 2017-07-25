# coding=utf-8
__author__ = 'JACK_CHAN'

import sys, openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook


reload(sys)
sys.setdefaultencoding("utf-8")

def read_excel_by_cellname(filename,
                            sheet_name,
                            cell_num):
    wb = load_workbook(filename)
    ws = wb.get_sheet_by_name(sheet_name)
    value = ws[cell_num].value
    return value

def write_excel_by_cellname(w_value,
                            filename,
                            sheet_index,
                            cell_num):
    wb = load_workbook(filename)
    wb._active_sheet_index = sheet_index
    ws = wb.active
    ws[cell_num] = w_value
    wb.save(filename)
    return wb

