def func(n):
    if n // 10 == 0:
        return n
    else:
        return n%10 * func(n//10)
print(func(1234))