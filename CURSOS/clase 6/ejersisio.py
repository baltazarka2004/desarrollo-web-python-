#vamos a crear una tupla principal , 
# la cual contenga 3 elementos los cuales 
# a su vez seran 3 tuplas que contendran cada uno 
# 3 listas que contendran 2 numeros, estos numeros se pueden repetir
# pero a al hora de imprimirlo en pantalla queremos 
# que no se muestren repetidos
lista1 = [1, 3]
lista2 = [5, 7]
lista3 = [1,3]
lista4 = [7,7]
lista5 = [9,2]
lista6 = [2,2]
lista7 = [4,2]
lista8 = [4,7]
lista9 = [1,3]
tupla1 = (lista1, lista2, lista3)
tupla2 = (lista4, lista5, lista6)
tupla3 =  (lista7, lista8, lista9)
p_tupla = (tupla1, tupla2, tupla3)


sinrepetidos1 = set(tupla1 [0])
sinrepetidos1u = list(sinrepetidos1)
sinrepetidos2 = set(tupla1 [1])
sinrepetidos2d = list(sinrepetidos2)
sinrepetidos3 = set(tupla1 [2])
sinrepetidos3t= list(sinrepetidos3)
t_sinrepe = (sinrepetidos1u, sinrepetidos2d, sinrepetidos3t)
tupla1 = t_sinrepe

sinrepetidos1 = set(tupla2 [0])
sinrepetidos1u = list(sinrepetidos1)
sinrepetidos2 = set(tupla2 [1])
sinrepetidos2d = list(sinrepetidos2)
sinrepetidos3 = set(tupla2 [2])
sinrepetidos3t = list(sinrepetidos3)
t_sinrepe = (sinrepetidos1u, sinrepetidos2d, sinrepetidos3t)
tupla2 = t_sinrepe

sinrepetidos1 = set(tupla3 [0])
sinrepetidos1u = list(sinrepetidos1)
sinrepetidos2 = set(tupla3 [1])
sinrepetidos2d = list(sinrepetidos2)
sinrepetidos3 = set(tupla3 [2])
sinrepetidos3t = list(sinrepetidos3)
t_sinrepe = (sinrepetidos1u, sinrepetidos2d, sinrepetidos3t)
tupla3 = t_sinrepe




print("tupla original: ", p_tupla)
p_tupla = (tupla1, tupla2, tupla3)
print("nueva tupla sin repetidos en una misma lista", p_tupla)
