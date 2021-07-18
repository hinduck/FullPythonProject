while True:
    print("Nhập một số: ")
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n, "là số nguyên tố")
    else:
        print(n, "không là số nguyên tố")
    print("Tiếp không?(Yes/No)")
    if (input() == "No"):
        exit()
print("BYE!")

