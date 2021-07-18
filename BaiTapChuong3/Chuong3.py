print("Câu 1:", )
x = 3
y = 5
z = 7
a = bool
a = True if x == 3 else False
print("Kết quả câu a là:", a)

b = bool
b = True if x < y else False
print("Kết quả câu b là:", b)

c = bool
c = True if x >= y else False
print("Kết quả câu c là:", c)

d = bool
d = True if x <= y else False
print("Kết quả câu d là:", d)

e = bool
e = True if x != y - 2 else False
print("Kết quả câu e là:", e)

f = bool
f = True if x < 10 else False
print("Kết quả câu f là:", f)

g = bool
g = True if x >= 0 and x < 10 else False
print("Kết quả câu g là:", g)

h = bool
h = True if x < 0 and x < 10 else False
print("Kết quả câu h là:", h)

i = bool
i = True if x >= 0 and x < 2 else False
print("Kết quả câu i là:", i)

j = bool
j = True if x < 0 or x < 10 else False
print("Kết quả câu j là:", j)

k = bool
k = True if x > 0 or x < 10 else False
print("Kết quả câu k là:", k)

l = bool
l = True if x < 0 or x > 10 else False
print("Kết quả câu l là:", l)

print("-" * 24, )
print("Câu 2:")
print("a) ", end='')
i = 3
j = 5
k = 7
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =", i, "j =", j, "k =", k)

print("b) ", end='')
i = 3
j = 7
k = 5
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =", i, "j =", j, "k =", k)

print("c) ", end='')
i = 5
j = 3
k = 7
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =", i, "j =", j, "k =", k)

print("d) ", end='')
i = 5
j = 7
k = 3
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =", i, "j =", j, "k =", k)

print("e) ", end='')
i = 7
j = 3
k = 5
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =", i, "j =", j, "k =", k)

print("f) ", end='')
i = 7
j = 5
k = 3
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =", i, "j =", j, "k =", k)

print("-"*24,)
print("Câu 3:")
n=int(input("Nhập một số n: "))
hangchuc = n//10
hangdonvi = n%10
while n<100:
    if n==1:
        print("Một")
        break
    if n==11:
        print("Mười một")
        break
    if n==5:
        print("Năm")
        break
    if hangchuc==1: print("Mười ", end='')
    if hangchuc==2: print("Hai mươi ", end='')
    if hangchuc==3: print("Ba mươi ", end='')
    if hangchuc==4: print("Bốn mươi ",end='')
    if hangchuc==5: print("Năm mươi ", end='')
    if hangchuc==6: print("Sáu mươi ", end='')
    if hangchuc==7: print("Bảy mươi ", end='')
    if hangchuc==8: print("Tám mươi ", end='')
    if hangchuc==9: print("Chín mươi ", end='')
    if hangdonvi==1: print("mốt")
    if hangdonvi==2: print("hai")
    if hangdonvi==3: print("ba")
    if hangdonvi==4: print("bốn")
    if hangdonvi==5: print("lăm")
    if hangdonvi==6: print("sáu")
    if hangdonvi==7: print("bảy")
    if hangdonvi==8: print("tám")
    if hangdonvi==9: print("chín")
    break
else:
    print("Số vừa nhập không hợp lệ")

print("-" * 24)
print("Câu 4:")
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

if month in (1, 3, 5, 7, 8, 10):
    if day == 31:
        day = 1
        month += 1
    else:
        day += 1

elif month == 12:
    if day == 31:
        day = 1
        month = 1
        year += 1
    else:
        day += 1

elif month in (4, 6, 9, 11):
    if day == 30:
        day = 1
        month += 1
    else:
        day += 1

elif month == 2 and day == 28:
    if year % 4 != 0:
        day = 1
        month += 1
    else:
        day += 1

elif month == 2 and (year % 4 == 0):
    if day == 29:
        day = 1
        month += 1
    else:
        day += 1

if (month in (1, 3, 5, 7, 8, 10, 12) and day > 31) or (month in (4, 6, 9, 11) and day > 30) or (
        month == 2 and day > 29 and year % 4 == 0) or (month == 2 and day > 28 and year % 4 != 0):
    print("Ngày tháng năm vừa nhập không hợp lệ!")
else:
    print("Ngày tiếp theo là: Ngày", day, "tháng", month, "năm", year)

print("-"*24)
print("Câu 5:")
a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
operate=input("Nhập một phép toán: ")
if operate == "+":
    print("Kết quả phép cộng trên là:", a + b)
elif operate == "-":
    print("Kết quả phép trừ trên là:", a - b)
elif operate == "*":
    print("Kết quả phép nhân trên là:", a * b)
elif operate == "/":
    print("Kết quả phép chia trên là:", a / b)
else:
    print("Phép toán vừa nhập không hợp lệ!")


print("-" * 24)
print("Câu 6:")
thang = int(input("Nhập vào một tháng: "))
if thang in (1, 2, 3):
    print("Tháng", thang, "thuộc quý I")
elif thang in (4, 5, 6):
    print("Tháng", thang, "thuộc quý II")
elif thang in (7, 8, 9):
    print("Tháng", thang, "thuộc quý III")
elif thang in (10, 11, 12):
    print("Tháng", thang, "thuộc quý IV")
else:
    print("Tháng vừa nhập không hợp lệ")
