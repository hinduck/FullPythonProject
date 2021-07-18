s = "C:/music/bolero/longme.mp4"
if s.endswith(".mp3"):
    print("Bài hát này có định dạng mp3")
else:
    print("Bài hát này không phải định dạng mp3")
s2 = "***OBAMA###"
print(s2.startswith("$"))


def LocSoDienThoai(dauso):
    dsArr = ["0937811400", "097235085", "0903308665", "0982523902", "0947135721", "0930259522"]
    for phone in dsArr:
        if (phone.startswith(dauso)):
            return phone
        return "<empty>"


dauso = input("Mời bạn nhập đầu số: ")
phone = LocSoDienThoai(dauso)
print(phone)


def LocToanBoSoPhone(dauso):
    dsArr = ["0937811400", "097235085", "0903308665", "0982523902", "0907135721", "0930259522"]
    dsFound = []
    for phone in dsArr:
        if (phone.startswith(dauso)):
            dsFound.append(phone)
        return dsFound


phone = input("Nhập đầu số: ")
dsFound = LocToanBoSoPhone(dauso)
print(dsFound)
