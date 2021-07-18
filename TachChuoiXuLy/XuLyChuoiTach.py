def CheckPrime(i):
    dem = 0
    for x in range(1, i + 1):
        if i % x == 0:
            dem += 1
    return dem == 2


s = "5;7;8;-2;8;11;-13;9;10"
arr = s.split(";")
sochan = 0
soam = 0
songuyento = 0
sum = 0
for i in arr:
    print(i)
    number = int(i)
    if number % 2 == 0:
        sochan += 1
    if number < 0:
        soam += 1
    if CheckPrime(number):
        songuyento += 1
    sum += number
print("Số chẵn =", sochan)
print("Số âm =", soam)
print("Số nguyên tố =", songuyento)
print("Trung bình =", sum / len(arr))
