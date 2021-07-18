n = int(input("Nhập n: "))
s = 0
for x in range(1, n+1):
    s = s + x
    if s >= 15:
        break
print("S =", s)
#8 = 1+2+3+5+6+7+8 = 36