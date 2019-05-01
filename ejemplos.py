lista1 =[[25,34,128],[256,77,99],[365,4,128]]
lista3 =[sum(lista1[0]),sum(lista1[1]),sum(lista1[2])]
print lista3
lista2=[]
for j in lista1:
    lista2.extend(j)

print sum(lista2)
lista2.sort()
lista2.reverse()
print lista2
x=input("Ingrese un número:")
divisores=[]
for i in lista2:
    if i%x==0:
        divisores.append(i)
print divisores

lista1 =[[25,34,128],[256,77,99],[365,4,128]]
print [sum(x) for x in lista1]
x=input("Ingrese un número:")

multiplos=[]
[multiplos.extend(i) for i in [[z for z in y if z % x == 0] for y in lista1]]
   
print multiplos
print lista2[1+1:]



print lista4
