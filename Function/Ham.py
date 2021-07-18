def ptb1(a, b):
    if a == 0 and b == 0:
        return "Vô số nghiệm"
    elif a == 0 and b != 0:
        return "Vô nghiệm"
    else:
        return "Nghiệm x = {0}".format(-b/a)

def XuatDuLieu(data):
    print(data)

kq1 = ptb1(0, 0)
print(kq1)
kq2 = ptb1(0, 1)
print(kq2)
kq3 = ptb1(6, 7)
print(kq3)

kq4 = ptb1(3, 7)
p = XuatDuLieu(kq4)
print(p)