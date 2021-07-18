s = float(input("Mời bạn nhập giá trị: "))
print("Bạn nhập: ", s)
print(type(s))

def StrToBool(s):
    return s.lower() in ("true", "t", "yes", "1")
x = input("Mời bạn nhập True/False: ")
x = StrToBool(x)
print(x)