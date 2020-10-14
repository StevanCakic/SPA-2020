def iter_1():
    for i in range(1, 51):
        print(i)

def rec_1(n):
    if n <= 50:
        print(n)
        rec_1(n+1)

def rec_2(n):
    # 1, 1, 2, 3, 5, 8, 13, 21, 34 
    if n <= 1:
        return n
    return rec_2(n-1) + rec_2(n-2)

print(rec_2(4))