g = 5
def increment():
    global g
    g = 2
    g = g + 1
increment()
print(g)

x = 0
def decrement():
    global x
    x = 2
    x = x - 1
decrement()
print("x =", x)