
EDAD_MAX = 18
edad = 15

def test():
    edad = 22
    print("hola git!" + str(edad))

#test()

def prueba_variable():
     print (edad)

# prueba_variable()

def cuenta_regresiva():
    for cuenta in range(11, 0, -1):
        print(cuenta)
    print('Listo!')

# cuenta_regresiva()

def cuenta_pegresiva_dos():
    contador = 10
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    while contador > 0: 
        print(numeros[contador])
        contador -= 1
    print('Listo!')

# cuenta_pegresiva_dos()

def numeros_pares():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for numero in numeros:
        if numero%2 == 0:
            print("número: ", numero, " es par")
        else:
            print("número " + str(numero) + "es impar")

# numeros_pares()

def numeros_pares_dos():
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for numero in numeros:
        if numero == 0:
            print("número: ", numero, " es par")
        elif numero%2 == 0: 
            print("número: ", numero, " es par")
        else:
            print("número " + str(numero) + " es impar")

numeros_pares_dos()

def sumar(numero_uno, numero_dos):
    resultado = numero_uno + numero_dos
    return resultado
# print(sumar(10, 22))



