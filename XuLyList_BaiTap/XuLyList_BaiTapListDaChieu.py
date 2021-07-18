from random import randrange


def AddMatrix(row, column):
    d = []
    for i in range(row):
        onerow = []
        for j in range(column):
            onerow.append(randrange(-100, 100))
        d.append(onerow)
    print()
    return d


def ExportMatrix(d):
    for r in d:
        for c in r:
            print(c, end='\t')
        print()


def ExportRow(Row):
    Dong = d[Row]
    return Dong


def ExportList(Dong):
    for c in Dong:
        print(c, end="\t")


def ExportColumn(Column):
    Cot = []
    for i in range(len(d)):
        Cot.append(d[i][Column])
    return Cot


def FindMax(d):
    max = d[0][0]
    for i in range(len(d)):
        for j in range(len(d[i])):
            if max < d[i][j]:
                max = d[i][j]
    return max


row = int(input("Nhập số dòng: "))
column = int(input("Nhập số cột: "))
d = AddMatrix(row, column)
ExportMatrix(d)
print()
Row = int(input("Mời bạn nhập dòng muốn xuất: "))
ExportList(ExportRow(Row))
print()
Column = int(input("Mời bạn nhập cột muốn xuất: "))
ExportList(ExportColumn(Column))
print()
max = FindMax(d)
print("Số lớn nhất của ma trận là:", max)