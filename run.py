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


def check_answer(respuestas, user_answer):
    
    anw_index  = 0  
    f_index = 0     # -> Indice de fallos de usuario
    score = 0       # -> Marcador. 
    user_fails = []

    

    for respuesta in respuestas:

        if respuesta == user_answer[anw_index]:
            score += 1 
            print (f'score = ´{score}')           
        else:
            user_fails.append(anw_index)

        anw_index += 1

    return user_fails, score


def mostrar_respuesta(user_fails, preguntas, opciones, respuestas, user_answers):
    
    os.system('cls')
    print ('--- Preguntas Falladas / Respuestas Correctas --- ')
    
    
    marcar_opc = "[X]"
    desmar_opc = "[ ]"

    
    # for n_fallo in user_fails:
    for n_fallo in user_fails:

        ord_res = (ord (respuestas[n_fallo]) - 96) - 1
        ord_res_user = (ord (user_answers[n_fallo]) - 96) - 1
        
        
        print (preguntas[n_fallo], end="")

        n_opcion = 0

        for opcion in opciones[n_fallo]:
            # print (opcion, end="")
            opcion_marcada = desmar_opc
            
            

            if n_opcion == ord_res_user:
                opcion_marcada = marcar_opc
            
            print (f'{opcion_marcada} {opcion}', end="")
            n_opcion += 1
    
        print (f'La opcion correcta es: {opciones[n_fallo][ord_res]}')

    if len(user_fails) == 0:
        print ('¡Enhorabuena! Has respondiendo correctamente a todas las pregutnas')
    else:
        print (f'Ha fallado {len(user_fails)} preguntas de {len(preguntas)}')

    input ('Pulsa una tecla para continuar...')

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
        
        # os.system('cls')
        i +=1
        j = 0
    return user_answers

def mostrar_marcador(score, preguntas):
    
    os.system('cls')
    print ('El juego ha terminado')
    print (f'score = {score}')
    
    score = score / len(preguntas) * 100
    print (f'Has obtenido una puntacion de {score}%')

preguntas, opciones, respuestas = load_data()

user_answers = star_game(preguntas, opciones)
print (f'user_answers= {user_answers}')
user_fails, score = check_answer(respuestas,user_answers)
mostrar_respuesta(user_fails, preguntas, opciones, respuestas, user_answers)
mostrar_marcador(score, preguntas)

