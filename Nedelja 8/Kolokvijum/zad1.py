lista = [{"ime":"Marko", "prezime":"Markovic"}, {"ime":"Ivan", "prezime":"Ivanovic"}]
for element in lista:
    print(element["ime"])

# Neka Ulazna R -> R

def poslednje_veliko_slovo(string):
    lista_velikih_slova = []
    for karakter in string:
        if karakter.isupper():
            lista_velikih_slova.append(karakter)
    return lista_velikih_slova[-1]

def poslednje_veliko_slovo_rec(string):
    if len(string) == 0:
        return False
    elif string[-1].isupper():
        print(string[-1])
    else:
        poslednje_veliko_slovo_rec(string[:-1])
    