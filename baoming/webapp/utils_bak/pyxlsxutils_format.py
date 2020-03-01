import pandas as pd
import datetime
# 使用前提导入以下两个库
import xlrd
import xlutils.copy
import platform

system_type = platform.system()
if 'indows' in system_type:
    filepath = "D:/PycharmProjects/lelingzdy/baoming/webapp/utils/fujian04_excel.xlsx"
    # data = pd.read_excel("D:/PycharmProjects/lelingzdy/baoming/webapp/utils/fujian04_excel.xlsx",
    #                      sheet_name='培训人员花名册')
else:
    filepath = "/data/python3_space/lelingzdy/baoming/webapp/utils/fujian04_excel.xlsx"
    # data = pd.read_excel("'/data/python3_space/lelingzdy/baoming/webapp/utils/fujian04_excel.xlsx",
    #                      sheet_name='培训人员花名册')
original_data = pd.read_excel(filepath, encoding='utf-8')
# rb打开该excel，formatting_info=True表示打开excel时并保存原有的格式
rb = xlrd.open_workbook(filepath, formatting_info=True)
# 创建一个可写入的副本
wb = xlutils.copy.copy(rb)


def set_out_cell(outSheet, col, row, value):
    """ Change cell value without changing formatting. """

    def _getOutCell(outSheet, colIndex, rowIndex):
        """ HACK: Extract the internal xlwt cell representation. """
        row = outSheet._Worksheet__rows.get(rowIndex)
        if not row: return None

        cell = row._Row__cells.get(colIndex)
        return cell

    # HACK to retain cell style.
    previousCell = _getOutCell(outSheet, col, row)
    # END HACK, PART I

    outSheet.write(row, col, value)

    # HACK, PART II
    if previousCell:
        newCell = _getOutCell(outSheet, col, row)
        if newCell:
            newCell.xf_idx = previousCell.xf_idx


# 判断需要写入的行是哪一行
for row in range(0, len(original_data)):
    if row > 5:
        outSheet = wb.get_sheet(0)
        set_out_cell(outSheet, 0, row, "a")
        set_out_cell(outSheet, 1, row, "a")
        set_out_cell(outSheet, 2, row, "a")
        set_out_cell(outSheet, 3, row, "a")
        set_out_cell(outSheet, 4, row, "a")
        set_out_cell(outSheet, 5, row, "a")
        set_out_cell(outSheet, 6, row, "a")
        set_out_cell(outSheet, 7, row, "a")
        set_out_cell(outSheet, 8, row, "a")
        set_out_cell(outSheet, 9, row, "a")
        set_out_cell(outSheet, 10, row, "a")
        set_out_cell(outSheet, 11, row, "a")
        set_out_cell(outSheet, 12, row, "a")
        set_out_cell(outSheet, 13, row, "a")
wb.save('output3.xlsx')
print('finish')
