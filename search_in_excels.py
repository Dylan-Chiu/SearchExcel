import os
import xlrd
import sys


class cell:
    def __init__(self, fileName, context, sheetId, rowId, colId):
        self.fileName = fileName.replace("/", '\\')
        self.context = context
        self.sheetId = sheetId
        self.rowId = rowId
        self.colId = colId

    def __str__(self):
        list = []
        list.append(self.fileName)
        list.append(self.context)
        list.append(self.sheetId)
        list.append(self.rowId)
        list.append(self.colId)
        return str(list)

    def getList(self):
        list = []
        list.append(self.fileName)
        list.append(self.context)
        list.append(self.sheetId)
        list.append(self.rowId)
        list.append(self.colId)
        return list


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


def findAllFilesWithSpecifiedSuffix(target_dir, target_suffix):
    find_res = []
    target_suffix_dot = "." + target_suffix
    walk_generator = os.walk(target_dir)
    for root_path, dirs, files in walk_generator:
        if len(files) < 1:
            continue
        for file in files:
            file_name, suffix_name = os.path.splitext(file)
            if suffix_name == target_suffix_dot:
                find_res.append(os.path.join(root_path, file))
    return find_res


def findAllCellInAllExcel(target_dir, key):
    result = []
    files = findAllFilesWithSpecifiedSuffix(target_dir, 'xls')
    file2 = findAllFilesWithSpecifiedSuffix(target_dir, 'xlsx')
    files.extend(file2)
    for file in files:
        cell_list = findCellInExcel(file, key)
        result.extend(cell_list)
    return result

# 运行示例：python search_in_excels.py "/Volumes/Samsung SSD/backup/综测计算/大二" "关键字"
if __name__ == "__main__":
    directory = sys.argv[1]
    key = sys.argv[2]
    print(f'directory: {directory}')
    print(f'key: {key}')
    print('result:')
    result = findAllCellInAllExcel(directory, key)
    for cell in result:
        print(cell.fileName)
