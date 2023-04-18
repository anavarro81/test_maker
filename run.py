import os
import re
import random 


user_fails = []
user_answer = []

def cargar_bote_preguntas():

    # Se abren los tres ficheros del juego y se cargan en listas. 
    # Se lee en formato utf-8 para asegurnos de que los caracteres especiales,
    # como las tildes, se muestras correctamente.

    f_bote_preguntas = open("bote_preguntas.txt", "r", encoding='utf-8-sig')

    preguntas  = []
    opciones = []
    respuestas = []

    for lin in f_bote_preguntas:        
        
        if lin[0] == 'P':
            preguntas.append(lin[3:])
        elif lin[0] == 'O':
            opciones_pregunta = (lin[3:].split(';'))
            print (f'opciones_pregunta = {opciones_pregunta}')
            opciones.append(opciones_pregunta)
        else:
            respuestas.append(lin[3:])

    return preguntas, opciones, respuestas

def gen_num_preg(tot_preg, n_preguntas):
    return random.sample(range(tot_preg), n_preguntas)

# def gen_sel_preguntas(lista_preguntas, preguntas):

#         sel_preguntas )
#     for pregunta in lista_preguntas:
#         preguntas = 

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

def star_game(lista_preguntas, preguntas, opciones):
    user_answers = [] 
    i = 0
    j = 0   
    
    letras = ['a', 'b', 'c', 'd']   

    print  (lista_preguntas)
    
    os.system('cls')
    for pregunta in lista_preguntas:
        
        print (preguntas[pregunta])
        
        for opcion in opciones[pregunta]:
            # print (f'{letras[j]} {opcion}', end="")
            print (f'\t {opcion}')
            j +=1

        opc = input ("Introduce una opcion [a, b, c, d]: ").lower()

        print (f'opc = {opc}')
        
        if opc in letras:
            user_answers.append(opc)    
        
        os.system('cls')
        i +=1
        
    return user_answers

def mostrar_marcador(score, preguntas):
    
    os.system('cls')
    print ('El juego ha terminado')
    print (f'score = {score}')
    
    score = score / len(preguntas) * 100
    print (f'Has obtenido una puntacion de {score}%')

# A partir de un bote de preugntas, genera tres listas una preguntas, otra para sus opciones y otra para respuesta. 
preguntas, opciones, respuestas = cargar_bote_preguntas()

print (opciones)


# Genera una lista de números de 5 numeros aleatorios, del 0 al 9. 
# Seran las preguntas generadas al azar
lista_preguntas = gen_num_preg(10,5)

# preguntas = gen_sel_preguntas(lista_preguntas, preguntas)

print (lista_preguntas)


    

user_answers = star_game(lista_preguntas, preguntas, opciones)
# print (f'user_answers= {user_answers}')
# user_fails, score = check_answer(respuestas,user_answers)
# mostrar_respuesta(user_fails, preguntas, opciones, respuestas, user_answers)
# mostrar_marcador(score, preguntas)

