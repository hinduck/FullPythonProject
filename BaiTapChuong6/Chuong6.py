"""def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s


def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s


def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s


print("Câu 1:")


# Trường hợp 1:
def main():
    print("Câu a:")
    global val
    val = 5
    print(sum1(5))
    print(sum2())
    print(sum3())


main()


# Trường hợp 2:
def main():
    print("Câu b:")
    global val
    val = 5
    print(sum1(5))
    print(sum3())
    print(sum2())


main()


# Trường hợp 3:
def main():
    print("Câu c:")
    global val
    val = 5
    print(sum2())
    print(sum1(5))
    print(sum3())


main()

print("Câu 2:")
def oscillate(n=-3, m=5):
    dic = {}
    for i in n:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return max(dic), dic[max(dic)]

for n in oscillate():
    print(n, end=" ")
print()
"""

print("CÂU 4: ")


def UocSo(n):
    """Hàm tính tổng ước số không kể chính nó.
    VD: Số 12 có tổng ước số là: 1+2+3+4+6=16"""
    TongUoc = 0
    for i in range(1, n):
        if n % i == 0:
            TongUoc += i
    return TongUoc


def PerfectNumber(n):
    """Hàm kiểm tra số hoàn thiện (số hoàn thiện là số có tổng các ước số của nó (không kể nó) thì bằng chính nó.
    VD: Số 6 có các ước số là 1, 2, 3 và 6 = 1+2+3 ==> 6 là số hoàn thiện"""
    if UocSo(n) == n:
        return print(n, "là số hoàn thiện")
    else:
        return print(n, "không phải là số hoàn thiện")


def AbundantNumber(n):
    """Hàm kiểm tra số thịnh vượng (số thịnh vượng là số có tổng các ước số của nó (không kể nó) thì lớn hơn nó
    VD: Số 12 có các ước số 1, 2, 3, 6 và 12 < 1+2+3+6 ==> 12 là số thịnh vượng"""
    if UocSo(n) > n:
        return print(n, "là số thịnh vượng")
    else:
        return print(n, "không phải là số thịnh vượng")


n = int(input("Nhập số nguyên dương n: "))
m = UocSo(n)
print("Tổng ước số của {0} là: {1}".format(n, m))
PerfectNumber(n)
AbundantNumber(n)
