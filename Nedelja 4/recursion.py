def suma(array):
    if len(array) == 0:
        return 0
    return array[0] + suma(array[1:]) 
    

niz = [1,2,3,3]
print(suma(niz))