import xlrd

class Excel2List:
    """读Excel转为二维数组"""
    def __init__(self,path,tab_index):
        """
        :param path: excel路径
        :param tab_index: 标签下标 0开始
        """
        self.data=xlrd.open_workbook(path)
        self.sheet=self.data.sheet_by_index(tab_index)
        self.rows=self.sheet.nrows
        self.cols=self.sheet.ncols

    def getResult(self):
        result=[]
        for i in range(self.rows):
            temp=[]
            for j in range(self.cols):
                temp.append(self.sheet.cell(i,j).value)
            result.append(temp)
        return result


