while True:
    x = int(input("Nhập vào một số: "))
    print(x, "là số chẵn" if x % 2 == 0 else "là số lẻ")
    ask = input("Tiếp không bạn?: ")
    if ask == "no" or ask == "không" or ask == "n" or ask == "k":
        break;
print("BYE!")