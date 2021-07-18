def Fibonacci(n):
    if n <= 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def ListFibonacci(n):
    for i in range(1, n + 1):
        print(Fibonacci(i), end="\t")


n = int(input("Nhập n: "))
print(Fibonacci(n))
ListFibonacci(n)
