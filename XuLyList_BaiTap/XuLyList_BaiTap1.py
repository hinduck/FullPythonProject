from random import randrange

print("Chương trình xử lý list")
n = int(input("Nhập số phần tử: "))
lst = [0] * n
for i in range(n):
    lst[i] = randrange(-100, 100)
print("List ngẫu nhiên là: ", )
print(lst)
print()

val = int(input("Mời bạn nhập thêm số: "))
lst.append(val)
print(lst)
print()

k = int(input("Bạn muốn đếm số lần xuất hiện của số nào? "))
dem = lst.count(k)
print("Số", k, "xuất hiện", dem, "lần trong list")
print()

def CheckPrime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count == 2

demnguyento = 0
tongnguyento = 0
for x in lst:
    if CheckPrime(x):
        demnguyento += 1
        tongnguyento += x
print("Có", demnguyento, "số nguyên tố trong list")
print("Tổng các số nguyên tố =", tongnguyento)
print()

lst.sort()
print("List sau khi Sort: ")
print(lst)
print()

del lst
print("List sau khi xoá: ")
print(lst)