lst = [113, 20, 30, 40, 25, 16, 27, 40]
print(lst)
lst.remove(40)
print(lst)
lst.remove(20)
print(lst)
del lst[0]
print(lst)
del lst[1:4]
print(lst)

lst = [15, 10, 20, 18]
print(lst)
del lst[1], lst[2]
# xoá lst[1] trước:
# [15, 20, 10]
# xoá lst[2]:
# [15, 20]
print(lst)