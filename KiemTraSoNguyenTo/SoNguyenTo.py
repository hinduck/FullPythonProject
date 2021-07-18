while True:
    n = int(input("Nhập một số nguyên dương: "))
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n, "là số nguyên tố")
    else:
        print(n, "không là số nguyên tố")
    ask = input("Bạn có muốn tiếp tục (Yes/No)?: ")
    if ask == "No" or ask == "no":
        break
print("THANKS!")