opc =True
while opc:
    x=input("Ingrese su edad")
    if  15<=x and x<= 20:
        print "Eres un anciano"

    elif 20<x and x<35:
        print "Eres un adulto contemporaneo"
    elif  x>=35:
        print "Eres muy joven"
    else:
        print "No es una edad válida"
    ent= raw_input("Desea ingresar otra edad: (s-n) ")
    if ent == "s":
        opc= True
    else:
        opc= False
