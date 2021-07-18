from math import *

"""print("Câu 2: ")
xA, yA = eval(input("Nhập toạ độ điểm A: "))
xB, yB = eval(input("Nhập toạ độ điểm B: "))
x = xB - xA
y = yB - yA
length = sqrt(pow(x, 2) + pow(y, 2))
print("|AB| = dAB = ", length)

print("-" * 24)
print("Câu 3: ")
a = float(input("Nhập số thực a: "))
x = float(input("Nhập số thực x: "))
result = log(x) / log(a)
print("log{0}({1}) = {2}".format(a, x, result))
"""
print("-" * 24)
print("Câu 4:")
n = int(input("Nhập số dấu căn lồng nhau: "))
while n < 1:
    print("Số dấu căn phải lớn hơn hoặc bằng 1!")
    exit()
else:
    s = sqrt(float(2))
    for i in range(2, n + 1):
        s = sqrt(2 + s)
print("S =", s)