#bucles
#while()
#while(i > 100):
    #print(i)
   # i += 1

#for i in range(100):
    #print(i)
    
i = 0    
lista = [1, 6, "algo", 70.2]
palabra = ["murcielago", "ofici", "more", "balty"]
LconA = []
palabraBuscada = input("ingrese la palabra que quiere buscar, o ingrese FIN para finalizar la busqueda ")


while(palabraBuscada != "FIN"):
    

    if palabraBuscada not in palabra:
        print("la palabra elegida no esta dentro de la lista")
    else:
        for i in range(len(palabra)):
            if(palabra[i] == palabraBuscada):
                LconA.append(palabra[i])
        print("palabra encontrada: ", LconA)
    palabraBuscada = input("ingrese la palabra que quiere buscar, o ingrese FIN para finalizar la busqueda")
print("busqueda finalizada")
    
    
    
#while (i < len(palabra)):
        #if ("a" in palabra[i]):
         #   LconA.append(palabra[i])
        #i += 1

#print(LconA)

#for i in range(len(lista)):
    #print("accediendo a la lista: ",lista[i])


#for elem in lista:
   # print("imprimiedno for i", elem)
    