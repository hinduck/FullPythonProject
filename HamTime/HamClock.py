from time import clock

start = clock()
print("Mời bạn nhập một giá trị: ")
x = input()
print("Bạn nhập x =", x)
end = clock()
duration = end - start
print("duration =", duration)