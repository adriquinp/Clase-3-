opc =True
while opc:
    x=int(raw_input("Ingrese un n�mero: "))
    if x==1:
        print str(x) + " es Lunes"

    elif x==2:
        print str(x) + " es Martes"

    elif x==3:
        print str(x) + " es Mi�rcoles"
    elif x==4:
        print str(x) + "es Jueves"
    else:
        print str(x) + " NO es un d�a"
    ent= raw_input("Desea ingresar de nuevo: (s-n)")
    if ent == "s":
        opc= True
    else:
        opc= False

