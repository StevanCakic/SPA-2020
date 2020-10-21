def maks_ab(a, b):
    if a > b:
        print(a)
    else:
        print(b)

# maks_ab(3, 5)
# maks_ab(7, 9)



def zbir_parnih_elemenata_liste(lista):
    zbir = 0
    for element in lista:
        if element % 2 == 0:
            zbir = zbir + element
    return zbir

a = [1, 2, 3, 4, 5]
print(zbir_parnih_elemenata_liste(a))