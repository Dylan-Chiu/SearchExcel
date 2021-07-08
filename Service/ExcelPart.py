import xlrd
import xlwt

from entity.cell import cell


def findCellInExcel(path, key):
    result = []
    workbook = xlrd.open_workbook(path)
    sheetNum = workbook.nsheets
    for sheetId in range(0, sheetNum):
        sheet = workbook.sheet_by_index(sheetId)
        rowsNum = sheet.nrows
        for rowId in range(0, rowsNum):
            row = sheet.row(rowId)
            for colId in range(0, len(row)):
                cellStr = str(row[colId])
                TcellStr = cellStr.replace(" ", "")
                if (TcellStr.find(key) > 0):
                    result.append(cell(path, cellStr, sheetId, rowId, colId))
    return result

if __name__ == '__main__':
    res = findCellInExcel('E:\实践委员综测加分证明.xlsx', '邱泉')
    for i in res:
        print(i)
