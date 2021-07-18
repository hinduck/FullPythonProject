def CheckDoiXung(s):
    flag = True
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            flag = False
            break
    return flag


def main():
    s = input("Nhập một chuỗi bất kỳ: ")
    if CheckDoiXung(s):
        print("Chuỗi đối xứng!")
    else:
        print("Chuỗi không đối xứng")


while True:
    main()
    check = input("Bạn có muốn tiếp tục? (Yes/No): ")
    if check == "No" or check == "no":
        break
print("CẢM ƠN")
