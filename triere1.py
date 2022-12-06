n = int(input('Introduceti limita pentru interval:'))
m=int(input('Introduceti suma cifrelor:'))
k=0

def SUMnum(a):
	if a == 0:
		return 0
	return SUMnum(a // 10) + a % 10

for i in range(n):
	if SUMnum(i) == m:
		k+=1

print('Conditia se satisface pentru',k,'numere!')
