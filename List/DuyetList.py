from random import randrange

n = int(input("Mời bạn nhập số phần tử: "))
lst = [0] * n
for i in range(n):
    lst[i] = randrange(-100, 100)
print(lst)
print("Duyệt theo Collection")
for x in lst:
    print(x, end=' ')
print("\nDuyệt theo Index")
for i in range(len(lst)):
    print("Vị trí thứ", i, "có giá trị =", lst[i])
print("\nDuyệt ngược danh sách")
for i in range(len(lst)-1, -1, -1):
    print(lst[i], end=' ')
