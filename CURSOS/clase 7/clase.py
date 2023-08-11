#numA = 10
#numB = 12
#prop = (numA == numB) #preguntamos si num a es igual a b 
#print(prop)

#prop = (numA < numB) #aca preguntamos si es mayor o si es menor
#print(prop)




nom = input("bienvenido, ingrese su nombre ")
nomD = input("bienvenido, ingrese segundo nombre ")
ordenAlf = (nom > nomD) #se fija si el primer nombre es alfabeticamente mayor al segundo

if(ordenAlf):
    print("el nombre",nom,"viene despues de ",nomD) #si es que se cumple
    
else:
        print("el nombre",nom,"no viene despues de ",nomD) #si no se cumple
        
        
        
num = int(input("ingrese un numero: "))
numD = int(input("ingrese otro numero: "))
ordenNum = num > numD 
if(ordenNum):
    print("el primero es mayor al segudno")
elif (num < numD):
    print("el segudno es mayor")
else:
    print("los numeros son iguales")
    


