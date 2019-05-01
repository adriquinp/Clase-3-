def saludar(nombre, hora):
    return nombre*hora
    
nombres= [("Juan",10),("María",15), ("Ana",3), ("Miguel",12)]
for n,h in nombres:
    saludar(n,h)


lista = [saludar(n,h) for n,h in nombres if n[0]=="M"]

print lista
