import re

f_preguntas  = open("preguntas.txt", "r", encoding='utf-8-sig')
f_opciones = open("opciones.txt", "r", encoding='utf-8-sig')
f_respuestas = open("respuestas.txt", "r", encoding='utf-8-sig')

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


preguntas, opciones, respuestas = load_data()

n_pregunta = 0

# print (opciones)
# print ('---->')
# print (opciones[0])
# print (opciones[0][3])
# ord_resp = (ord (respuestas[0]) - 96) - 1
# print ('--->')
# print (opciones[0][ord_resp])



for pregunta in range (0, len(preguntas)):
    ord_resp = (ord (respuestas[pregunta]) - 96) - 1
    print (f'La respuestas correcta es: {opciones[pregunta][ord_resp]}', end="")
