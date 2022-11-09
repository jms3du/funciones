MENU = '''
    MENÚ PRINCIPAL: 
    a. Conocer el mayor
    b. Conocer el menor
    c. Obtener la suma de todos los números
    d. Obtener la media
    e. Sustituir el valor de un elemento por otro número introducido por teclado
    f. Mostrar todos los números
    g. Salir
''' 
lista_numeros = [2, 3, 4]
lista_num_2 = [3, 7, 11]


def suma_numeros(lista):
    suma = 0
    for i in range(len(lista)):
        suma+= lista[i]
    return suma






assert(suma_numeros(lista_numeros)==9)
assert(suma_numeros(lista_num_2)==21)
assert(suma_numeros([0, 9 , 27, 14, 35])==85)






def sustituir_valor(lista_para_sustituir, elemento_buscar, elemento_sustituto):
    
    for i in range(len(lista_para_sustituir)):
        if elemento_buscar == lista_para_sustituir[i]:
            lista_para_sustituir[i]=elemento_sustituto
    
    return lista_para_sustituir


def programa_principal():
    print(MENU)
    opcion = input("Introduce una opción: ")
    
    while opcion!='g':
        if opcion=="a":
            pass
        elif opcion == 'c':
            print(suma_numeros(lista_numeros))
        elif opcion == 'e':
            ns = int(input("Introduce el número a sustituir: "))
            sustituto = int(input("Introduce el sustituto: "))
            print(sustituir_valor(lista_numeros, ns, sustituto))
        
        
        opcion = input("Introduce una opción: ")
    
        
#programa_principal()




print(sustituir_valor(["hola", "hola", "buenas"], "hola", "adiós"))




