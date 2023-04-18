f_bote_preguntas = open("bote_preguntas.txt", "r", encoding='utf-8-sig')
fichero_final = open ('fichero_final.txt', 'w')

    # Se crea un prefijo para identificar las lineas del fichero en funcion de su contenido:
    # P(Preguntas) | O(Opciones) | R(Respuestas)
    
PREP_PRGTA = 'P: '
PREP_OPCNS = 'O: '
PREP_RPSTA = 'R: '
cont_linea = 1
    
# Se define la posicion inicial (línea dentro del fichero) de la primera pregunta, opcion y respuesta. 
pos_prgta   = 1
pos_opcin   = 2
pos_rpsta   = 3

final = []

for lin in f_bote_preguntas:    
    
    prefijo = ""        

    if  cont_linea == pos_prgta:
        prefijo = PREP_PRGTA
        pos_prgta += 3
    elif cont_linea == pos_opcin:
        prefijo = PREP_OPCNS
        pos_opcin += 3
    else:
        prefijo = PREP_RPSTA
        pos_rpsta += 3

    lin = prefijo + lin
    
    final.append(lin)
    fichero_final.write(lin)
    cont_linea = cont_linea + 1

# for lin in final:
#     print (lin)



