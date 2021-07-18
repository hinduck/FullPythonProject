def handle(f, x):
    return f(x)


kq1 = handle(lambda x: x ** 2, 9)
print(kq1)
kq2 = handle(lambda x: x % 2 == 0, 4)
print(kq2)


def SoChan(x):
    return x % 2 == 0


kq3 = handle(SoChan, 4)
print(kq3)
kq4 = handle(SoChan, 5)
print(kq4)
kq5 = handle(lambda x: SoChan(x), 7)
print(kq5)
