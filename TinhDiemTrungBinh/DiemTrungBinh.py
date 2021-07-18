print("Chương trình tính điểm trung bình")
toan, ly, hoa = eval(input("Nhập điểm toán, lý, hoá: "))
print("Điểm toán =", toan)
print("Điểm lý =", ly)
print("Điểm hoá =", hoa)
dtb = (toan + ly + hoa) / 3
print("Điểm trung bình =", dtb)
print("Điểm làm tròn =", round(dtb, 2))