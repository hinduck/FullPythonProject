"""print("Câu 1:")
a = 0
while a < 100:
    print("*", end='')
print()

print("Câu 2:")
a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print("*", end='')
        b += 1
    print()
a += 1


print("Câu 4:")
for a in range(20, 100, 5):
    print("*", end='')
print()

print("-" * 24)
print("Câu 6:")
for i in range(1, 5):
    for j in range(1, 5):
        if i == 1 or j == 1 or i == 4 or j == 4:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

print("-" * 24)
for i in range(1, 5, 1):
    for j in range(1, 5, 1):
        if j > 4 - i:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

print("-" * 24)
n=int(input("Nhập chiều cao: "))
for i in range(1, n + 1, 1):
    for j in range(1, n + 1, 1):
        m = 8 // 2
        if i == j or i == m  or (j == 1 and i <= m) or (j == n and i >= m and i <= n):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
"""

print("-" * 24)
print("Câu 7: ")
x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
s = 0
for i in range(1, n + 1):
    tu = x ** (2 * i + 1)
    mau = 1
    for j in range(1, i + 1):
        mau *= (2 * j + 1)
    s += tu / mau
print("S({0},{1}) = {2}".format(x, n, s))
