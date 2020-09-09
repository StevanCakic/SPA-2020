from stack_ex import Stack

def to_binary(num):
    s = Stack()
    while num > 0:
        reminder = num % 2
        s.push(reminder)
        num = num // 2
    
    bin_num = ""
    while not s.is_empty():
        bin_num = bin_num + str(s.pop())
    return bin_num
print(to_binary(7))