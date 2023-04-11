import os
import re



def load_data():

    # Se abren los tres ficheros del juego y se cargan en listas. 
    # Se lee en formato utf-8 para asegurnos de que los caracteres especiales,
    # como las tildes, se muestras correctamente.

    f_preguntas  = open("preguntas.txt", "r", encoding='utf-8-sig')
    f_opciones = open("opciones.txt", "r", encoding='utf-8-sig')
    f_respuestas = open("respuestas.txt", "r", encoding='utf-8-sig')

    preguntas  = []
    opciones = []
    respuestas = []
    cont_opcs = 0
    conj_opciones = []

    for respuesta in f_respuestas:
        
        respuesta = re.sub('\n', '', respuesta)
        respuestas.append(respuesta)

    for opcion in f_opciones:    
        conj_opciones.append(opcion)    
        if cont_opcs == 3:
            opciones.append(conj_opciones)
            conj_opciones = []
            cont_opcs = 0
        else:
            cont_opcs += 1

    for pregunta in f_preguntas:
        preguntas.append(pregunta)

    return preguntas, opciones, respuestas


conj_opciones = []
user_fails = []
user_answer = []

def show_score(score, user_fails):
    print ('-- Se ha terminado el juego --')
    print (f'Tu puntuación es: {score} /10')
    print (f'Has fallado: {10-score} preguntas')
    print ('Quieres ver las respuestas correctas')


def check_answer(respuestas, user_answer):
    
    anw_index  = 0  
    f_index = 0     # -> Indice de fallos de usuario
    score = 0       # -> Marcador. 
    user_fails = []

    print (respuestas)

    for respuesta in respuestas:

        print (f'respuesta = {respuesta}')
        print (f'user_answer[{anw_index}] = {user_answer[anw_index]}')

        if respuesta == user_answer[anw_index]:
            score += 1            
        else:
            user_fails.append(anw_index)

        anw_index += 1
    
    print (f'La puntuacion es: {score}')



# Cargamos todas las respuesta en la lista de opciones
# Se crea una lista de listas, cada lista interna es un conjunto de 4 respuesta A-D. 
# La quinta linea de cada bloque, es la respuesta correcta. 




# Mostrarmos el test completo. 

def star_game(preguntas, opciones):
    user_answers = [] 
    i = 0
    j = 0   
    
    letras = ['a', 'b', 'c', 'd']    
    
    os.system('cls')
    for pregunta in preguntas:
        
        print (pregunta, end="")
        
        for opcion in opciones[i]:
            print (f'{letras[j]} {opcion}', end="")
            j +=1

        opc = input ("Introduce una opcion [A, B, C, D]: ").lower()

        print (f'opc = {opc}')
        
        if opc in letras:
            user_answers.append(opc)    
            print (f'agrego la letra = {opc}')
            
        
        
        # os.system('cls')
        i +=1
        j = 0
    return user_answers


preguntas, opciones, respuestas = load_data()

# print (f'Preguntas   = {preguntas}')
# print (f'Opciones    = {opciones}')
# print (f'Respuestas  = {respuestas}')

user_answers = star_game(preguntas, opciones)
print (f'user_answers= {user_answers}')
check_answer(respuestas,user_answers)


# show_score (5,user_fails)
