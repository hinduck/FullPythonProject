from random import randrange

lst = [
    [4, 2, 10],
    [7, 10, 5],
    [-7, 9, 2]
]
print(lst)

print("*" * 20)
for row in lst:
    for column in row:
        print(column, end='\t')
    print()

print("*" * 20)
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end="\t")
    print()

print("*" * 20)
arr2D = []
rowsize = int(input("Nhập số dòng: "))
columnsize = int(input("Nhập số cột: "))
for i in range(rowsize):
    onerow = []
    for j in range(columnsize):
        onerow.append(randrange(-100, 100))
    arr2D.append(onerow)
print("Ma trận ngẫu nhiên đã nhập: ")
for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        print(arr2D[i][j], end="\t")
    print()