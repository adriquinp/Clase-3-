def conver(x):
    a= x/3600
    b=x%3600/60
    c= (x%3600)%60
return[a, b, c]
def incre (h1,h2):
    c = h1[2]+h2[2]
    if c>59:
        c = c-60
        temp =1
    else:
        temp= 0
    b = h1[1]+h2[1]+temp
    if b>59:
        b = b-60
        temp =1
    else:
        temp= 0
    a = h1[0]+h2[0]+temp

return  [a, b, c]

def a_cadena(valor):
    if valor < 10:
        return "0"+str(valor)
    else:
        return str(valor)
    
def formatear(lista):
    return lista[0]+":"+lista[1]+":"+lista[2]

horas=["00:22:50","15:10:11","12:20:55"]

lista=[h.split(":") for h in horas]
lista2=[[int(y) for y in x] for x in lista]

x=input("Ingrese el número de segundos: ")

print conver(x)

lista3= [incre(y,conver(x)) for y in lista2]
print lista3
