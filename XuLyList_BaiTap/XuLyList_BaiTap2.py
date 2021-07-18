from random import randrange

lst = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    lst.append(randrange(0, 100))
print("List sau khi tạo ngẫu nhiên là: ")
print(lst)
print()

k = int(input("Nhập số để xoá: "))
while lst.count(k) > 0:
    lst.remove(k)
print("List sau khi xoá: ")
print(lst)
print()


def CheckDoiXung(lst):
    for i in range(len(lst)):
        if (lst[i] != lst[len(lst) - i - 1]):
            return False
    return True


check = CheckDoiXung(lst)
if check == True:
    print("List đối xứng")
else:
    print("List không đối xứng")
