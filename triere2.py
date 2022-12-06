n1=input('Dati primul numar:')
n2=input('Dati al doilea numar:')

equal1=True
equal2=True

for i in n1:
    if i not in n2:
        equal1=False
        break
for i in n2:
    if i not in n1:
        equal2=False
        break
if(equal2 and equal1):
    print("Numerele sunt prietenoase")
else:
    print("Numerele nu sunt prietenoase")
