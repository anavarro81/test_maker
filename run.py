import os

f_preguntas  = open("preguntas.txt", "r", encoding='utf-8-sig')
f_opciones = open("opciones.txt", "r", encoding='utf-8-sig')

	 
	
# preguntas.close

preguntas  = []
opciones = []
respuestas = []
conj_opciones = []

# Cargamos todas las pregutnas en la lista de preguntas
for pregunta in f_preguntas:    
    preguntas.append(pregunta)


# Cargamos todas las respuesta en la lista de opciones
# Se crea una lista de listas, cada lista interna es un conjunto de 4 respuesta A-D. 
# La quinta linea de cada bloque, es la respuesta correcta. 

cont_opcs = 0

for opcion in f_opciones:
    
    conj_opciones.append(opcion)
    
    if cont_opcs == 3:
        opciones.append(conj_opciones)
        conj_opciones = []
        cont_opcs = 0
    else:
        cont_opcs += 1
    
i = 0
j = 0
letras = ['A', 'B', 'C', 'D']


# Mostrarmos el test completo. 
for pregunta in preguntas:
    
    print (pregunta, end="")
    
    for opcion in opciones[i]:
        print (f'{letras[j]} {opcion}', end="")
        j +=1

    opc = input ("Introduce una opcion [A, B, C, D]").lower()
    print (f'La opcion elegida es: {opc}')
    os.system('cls')
    i +=1
    j = 0


# print (opciones)
    



    

# print (preguntas)
# print (opciones)
# print ("---------")
# print (respuestas)

# for respuesta in opciones:
#      print (respuesta, end="")


