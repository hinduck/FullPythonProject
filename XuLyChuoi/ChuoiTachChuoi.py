s = "sv007;Nguyễn Thị Tẹt;1/1/1990"
arr = s.split(";")
print(len(arr))
for x in arr:
    print(x)


s = """Obama
        hahaha
        ali333"""
arr1 = s.splitlines()
for line in arr1:
    print(line, "a-->", line.count("a"))


s = """sv001;Nguyễn Thị Hạnh;1/1/1990
sv002;Trần Văn Phúc;2/2/1995
sv003;Hồ Văn An;2/3/1998
sv004;Phạm Thị Lành;4/4/1994
sv005;Phạm Hồ Đồ
"""
arrSV = s.splitlines()
for line in arrSV:
    arrInfo = line.split(";")
    if len(arrInfo) == 3:
        print(arrInfo)

s2 = "#"
s2 = s2.join(arr)
print(s2)

a = "Obama"
b = "Kim Jong Un"
c = a + b
print(c)