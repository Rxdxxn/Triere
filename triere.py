#Se consideră numerele naturale din mulţimea {m, …, n}.
#Elaboraţi un program care determină pentru cîte numere q din această mulţime vor avea numarul x in structura.


n = int(input('Introduceti limita maxima pentru interval:'))
m=int(input('Introduceti limita minima pentru interval:'))
x=int(input('Introduceti cifra corespunzatoare:'))
k=0
nm=list(range(m,n))

def Num(a,b):
    for i in b:
        if i not in b:
            return False
        else:
            return True

def da(a,b):
    for i in a:
        if i in b:
            return k+1


print('Conditia se satisface pentru',da(nm,x),'numere!')