import math

try:
    r=float(input("Nhập bán kính hình tròn: "))
    cv=2*math.pi*r
    dt=r**2*math.pi
    print("Chu vi là: ",cv)
    print("Diện tích là: ",dt)
except:
    print("Có lỗi!")