print("eliga una de las siguientes 4 opcione"
      "\n1- detectar el mayor de tres numeros"
      "\n2-horarios"
      "\n3-suma de un numero entre sus cifras"
      "\n4-imprimir una lista con pares e invertida de un numero de 5 cifras")

opcion = int(input("escriba su opcion "))
if(opcion == 1):
    numU = int(input("ingrese su primer numero: "))
    numD = int(input("ingrese su segundo numero: "))
    numT = int(input("ingrese su tercer numero: "))
    if (numU > numD and numU > numD):
        print("el mayor numero es", numU)
    elif (numD > numU and numD >  numT):
        print("el mayor numero es", numD)
    elif (numT > numU and numT > numD):
        print("el mayor numero es", numT)
    else:
        print("los tres son iguales")
elif (opcion == 2):
    hora = int(input("ingrese la hora (formato 23hs): "))
    if (hora >= 6 and hora <= 12):
        print("la hora seleccionada pertenece a la mañana")
    elif (hora >= 13 and hora <= 18):
        print("la hora seleccionada pertenece a la tarde")
    else:
        print("la hora seleccionada pertenece a la noche")

    

elif (opcion == 3):
    num = int(input("ingrese un numero de 3 cifras"))
    cU = num / 100
    resto = num % 100
    cD = resto / 10
    cT = resto % 10
    total = cU + cD + cT
    print("el resultado de la suma de las tres cifras es:",total)
    
elif (opcion == 4): #numero = 10562
    num = str(input("ingrese un numero de 5 cifras"))
    num = list(num) # [1, 0 ,5, 6, 2]
    num[0] = int(num[0]) #para evitar que python detecte los elementos de la lista como str paso uno por uno a int
    num[1] = int(num[1])
    num[2] = int(num[2])
    num[3] = int(num[3])
    num[4] = int(num[4])
    
    listanueva = []
    
    if(num[0] % 2 == 0):
        listanueva.append(num[0])
    if(num[1] % 2 == 0):
        listanueva.append(num[1])
    if(num[2] % 2 == 0):
        listanueva.append(num[2])
    if(num[3] % 2 == 0):
        listanueva.append(num[3])
    if(num[4] % 2 == 0):
        listanueva.append(num[4])
        
    print("esta es la lista con solo los numero pares",listanueva[::-1])
    
        
        
    
    

        
