from math import *

x = 5
y = 7
print(pow(x, y))
print(x ** y)
print(sqrt(25))
deg = 30
print("30 =>", radians(deg))
rad = radians(deg)
print(degrees(rad))
print("log10(100) =", log10(100))

print("Mời bạn nhập một góc: ")
goc = float(input())
sinx = sin(radians(goc))
cosx = cos(radians(goc))
tanx = tan(radians(goc))
cotanx = 1 / tanx
print("sin({0}) = {1}".format(goc, sinx))
print("cos({0}) = {1}".format(goc, cosx))
print("tan({0}) = {1}".format(goc, tanx))
print("cotan({0}) = {1}".format(goc, cotanx))
