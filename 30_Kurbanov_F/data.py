# import openpyxl
# import parse
# from main import *


class Data:

    def __init__(self, data):
        self.book = openpyxl.load_workbook('data')
        self.sheet = self.book.active # активный лист


if __name__ == '__main__':
    cl1 = Data('1-kurs.xlsx')