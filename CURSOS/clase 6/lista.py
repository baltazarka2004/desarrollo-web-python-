primeralista = []
slista = [18, "balty" , 67.2, "mitas", primeralista]

slista[2] = 12

pares = [i*2 for i in range(101)]

usuarios = []
usuarios.append("lucas")
usuarios.append("lucas")
usuarios.append("balty")
usuarios.append("mati")

print(usuarios)
print("lucas aparece:",usuarios.count("lucas"))


otralista = ["maty", "balty", 32]

usuarios.extend(otralista)
print(usuarios)

usuarios.remove("balty")#remueve el primer valor identico que se cruza y solo el primero, 
# si lo quiero borrar mas veces debo de ponero mas veces
print(usuarios)

texto = "algo de texto"

texto = texto.split(" ")
print(texto)

