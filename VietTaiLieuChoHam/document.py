def UocChungLonNhat(a, b):
    """Hàm này dùng để tìm uớc số chung lớn nhất
    VD: a = 9, b = 6 thì UCLN = 3"""
    min = a if a < b else b
    for i in range(min, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1

uoc = UocChungLonNhat(25, 15)
print(uoc)