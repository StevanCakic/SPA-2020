"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))
"""

# comment code with instance creation i stack_ex.py file
from stack_ex import Stack

def is_match(p1, p2):
    return (p1 == "(" and p2 == ")") or (p1 == "[" and p2 == "]") or (p1 == "{" and p2 == "}")

def is_parentesis_balanced(str):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(str) and is_balanced:
        parethesis = str[index]
        if parethesis in "{[(":
            s.push(parethesis)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, parethesis):
                    is_balanced = False
        index = index + 1
    return s.is_empty() and is_balanced

print(is_parentesis_balanced("([])"))
# prosiriti zadataka da radi sa brojevima