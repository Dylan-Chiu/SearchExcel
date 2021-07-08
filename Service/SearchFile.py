import os
from Service.ExcelPart import findCellInExcel

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
        cellList = findCellInExcel(file, key)
        result.extend(cellList)
    return result

if __name__ == '__main__':
    result = findAllCellInAllExcel('E:\Chrome下载内容', '邱泉')
    for i in result:
        print(i)
