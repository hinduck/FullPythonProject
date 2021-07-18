lst = [12, 0, 25, 16]
print(lst)
"""lst.reverse()
print(lst)"""
for i in range(len(lst)-1, -1, -1):
    print(lst[i], end="\t")


print()
print("*" * 20)
lst = [8, 0, 2, 100, 20]
print(lst)
lst2 = reversed(lst)
for item in lst2:
    print(item, end=' ')
print()
print(lst)


lst = ["Obama", 'hahaha', "ali333", """Kim Jong Un
Putin
Donald Trump
"""]
print(lst)
lst.reverse()
print(lst)