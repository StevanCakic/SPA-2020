# Prvi zadatak
def first_50(n = 1):
    if n > 50:
        return
    else:
        print(n)
        return first_50(n + 1)

# ovo je samo kao dodatak, generalizovan prethodni primjer u slucaju da se od vas trazi
# da rekurzivno stampate prvih n prirodnih brojeva
def first_n(n):
    if n == 0:
        return 0
    else:
        # idete skroz do kraja rekurzije
        a = first_n(n-1)
        if a == None:
            a = 0
        x = n + a
        print(x)

# Drugi zadatak
# Za ovaj primjer probajte da nacrtate rekurzivno drvo!
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Treci zadatak 
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

# Cetvrti zadatak 
def print_list(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        print(lista[0])
        return print_list(lista[1:])

# Peti zadatak, pretpostaviti da je broj prirodan (cio broj koji je veci od 0) 
def br_cifara(n):
    if n == 0:
        return 0
    else:
        return 1 + br_cifara(n//10)

# Sesti zadatak, ovo je tip zadataka kada u rekurzivnoj funkciji zelite da mijenjate neku varijablu
# ali da se ne bi vracala na inicijalnu vrijednost, definisete je van rekurzivne funkcije
def max_liste(lista):
    max = 0
    def pom_max_liste(lista):
        nonlocal max
        if len(lista) == 0:
            return max
        else:
            if lista[0] > max:
                max = lista[0]
            return pom_max_liste(lista[1:])
    return pom_max_liste(lista)

# Sedmi zadatak, prvi nacin

def to_binary(n):
    if n < 0:
        return 'Mora biti pozitivan broj'
    elif n == 0:
        return '0'
    else:
        return to_binary(n//2) + str(n % 2)

# Sedmi zadatak, drugi nacin
def to_binary_new(n):
    if n == 0:
        return 0
    else:
        return (n % 2 + 10 * to_binary_new(int(n // 2))) 

# Osmi zadatak 
def ispalindrome(word):
    if len(word) < 2: # ako string ima manje od dva karaktera sigurno je palindrom
        return True 
    if word[0] != word[-1]: # ako se prvi i poslenji karakter ne poklapaju, string sigurno nije palindrom
        return False
    return ispalindrome(word[1:-1]) # pozovi rekurziju bez prvog i poslenjeg karaktera

# Deveti zadatak
def get_first_capital(word):
    if word == "":
        return
    elif word[0].isupper():
        return word[0]
    else:
        return get_first_capital(word[1:])

def x_n(x, n):
    if n == 0:
        return 1
    else:
        return x * x_n(x, n - 1)

first_50()
first_n(50)
print(fib(7))
print(fact(5))
print(print_list([1,2,3,4]))
print(br_cifara(1234))
print(max_liste([1,2,1,4,7,3]))
print(to_binary(10))
print(to_binary_new(10))
print(ispalindrome("abba"))
print(get_first_capital("adadaCadadD"))
print(x_n(2, 3))