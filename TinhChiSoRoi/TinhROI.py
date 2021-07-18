def ROI(dt, cp):
    return (dt - cp) / cp


def Hint(roi):
    if roi >= 0.75:
        return "Nên đầu tư"
    else:
        return "Không đầu tư"


print("Chương trình tính ROI")
dt = int(input("Nhập doanh thu: "))
cp = int(input("Nhập chi phí: "))
roi = ROI(dt, cp)
print("ROI =", roi)
print("==>", Hint(roi))
