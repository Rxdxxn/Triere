#Se consideră numerele naturale din mulţimea {m, …, n}.
#Elaboraţi un program care determină pentru cîte numere q din această mulţime vor avea numarul x in structura.
#Sa se afiseze numerele determinate.

m = int(input('Introduceti limita inferioara: '))
n = int(input('Introduceti limita superioara: '))
x = int(input('Introduceti cifra cautata: '))
lst = []
rez = []

for i in range(m,n+1):
    lst.append(i)

def verificareSolutie(k):
    while k != 0:
        if k%10 == x:
            return True
        k //= 10
        return False

def adaugareSolutie(k):
    global rez
    rez.append(k)

for i in lst:
    if verificareSolutie(i):
        adaugareSolutie(i)

print(f'Elementele care contin {x} sunt {len(rez)} \n{rez}')
