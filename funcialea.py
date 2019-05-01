
import random


def aleatorios(a):
    ale=[]
    for i in range(0,a):
        ale.append(random.randint(2,100))
    return ale
    

def repver(ale):
    for i in range(2*len(ale)):
        i=input("Ingrese un numero:")
        if i in ale:
            return "Lo encontraste"
    return "Perdiste"
    
        
