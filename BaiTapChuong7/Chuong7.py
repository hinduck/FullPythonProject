"""def Check(s):
    count_upper = 0
    count_lower = 0
    count_number = 0
    count_space = 0
    count_alnum = 0
    count_vowel = 0
    count_consunant = 0
    arr = s
    for x in arr:
        if x.isupper():
            count_upper += 1
        if x.islower():
            count_lower += 1
        if x.isdigit():
            count_number += 1
        if x.isspace():
            count_space += 1
        if x.isalnum():
            count_alnum += 1
        if x == "A" or x == "E" or x == "I" or x == "O" or x == "U" or x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            count_vowel += 1
        else:
            count_consunant += 1

    print("Câu 2:")
    print("Số ký tự trong chuỗi =", len(s))
    print("Số chữ cái IN HOA =", count_upper)
    print("Số chữ cái IN THƯỜNG =", count_lower)
    print("Số chữ số =", count_number)
    print("Số khoảng trắng =", count_space)
    print("Số ký tự đặc biệt =", count_alnum)
    print("Số ký tự NGUYÊN ÂM =", count_vowel)
    print("Số ký tự PHỤ ÂM =", count_consunant)


s = input("Nhập vào một chuỗi: ")
Check(s)


def NegativeNumberInString(str):
    count_minusnumber = 0
    arr1 = str.split()
    for x in arr1:
            if x == "-":
                print(x, x+1)

str = input("Mời bạn nhập chuỗi: ")
print("Số ký tự trong chuỗi =", len(str))
print("Các số nguyên âm trong chuỗi là :")
NegativeNumberInString(str)
"""

def ToiUuChuoi(s):
    s2 = s
    s2 = s2.strip()
    arr = s2.split(" ")
    s2 = ""
    for x in arr:
        word = x
        if len(word.strip()) != 0:
            s2 = s2 + word + " "
    return s2.strip().title()

print("Câu 4:")
s = input("Nhập một chuỗi: ")
print(s, "=>", len(s))
s = ToiUuChuoi(s)
print(s, "=>", len(s))
