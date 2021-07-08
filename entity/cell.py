class cell:
    def __init__(self, fileName, context, sheetId, rowId, colId):
        self.fileName = fileName
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
