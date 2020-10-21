
def MaxElem(lista):
    i = 0
    current_max = -9999

    def maxElemPom(lista):
        nonlocal i, current_max
        if i < len(lista):
            if current_max < lista[i]:
                current_max = lista[i]
            i = i + 1
            maxElemPom(lista)
        return current_max
    return maxElemPom(lista)

print(MaxElem([1,2,1,3,4]))
