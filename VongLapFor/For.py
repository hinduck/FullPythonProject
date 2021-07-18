n = int(input("Nhập n: "))
s = 0
if n % 2 == 0:
    for x in range (2, n + 1, 2):
        s = s + x
elif n % 2 != 0:
    for x in range (1, n + 1, 2):
        s = s + x
print("Tổng S =", s)
#8 = 2+4+6+8 = 20
#7 = 1+3+5+7 = 16