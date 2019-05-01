def suma(a,b):
    return a + b
def resta(a,b):
    return a-b
def producto(a,b):
    return a*b
def division(a,b):
    return a/b

def factorial(a):
    temp=1
    for i in range(1,a):
        temp =temp*(i+1)
    return temp
        
    
def factorial1(a):
    temp=1
    for i in range(1,a):
        temp *= (i+1)
    return temp
                                                              
def fibonacci(a):
    if a==1:
        return 1
    elif a==2:
        return 1
    return fibonacci(a-1)+fibonacci(a-2)

lista=[[1,2,3],[1,2]]
lista2=[sum(i) for i in lista]

print sum(lista2)

def contar_sub(lista):
    if lista==[]:
        return 0
    return len(lista[0])+contar_sub(lista[1:])

def suma_lista(lista):
    if lista==[]:
        return 0
    return lista[0]+suma_lista(lista[1:])

def sumsub_lis(lista):
    if lista==[]:
        return 0
    return sum(lista[0])+sumsub_lis(lista[1:])
