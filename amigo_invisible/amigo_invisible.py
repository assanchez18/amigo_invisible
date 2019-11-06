import time
import random

time.sleep(1)
print("Introduce un nombre: ")
nombre = input()
lista_nombres = []
lista_nombres2 = []
i = 0
#Introducimos todos los nombres
while nombre != "":
    lista_nombres.append(nombre)
    lista_nombres2.append(nombre)
    i += 1
    print("Introduce otro nombre: ")
    nombre = input()

#Comprobamos que están todos en la lista
print(lista_nombres)


time.sleep(1)
while i != 0:
    numero_random = random.randint(0,i-1)
    if i != 1:
        numero_random_envio = random.randint(0,i-1)
        while numero_random == numero_random_envio:
            numero_random_envio = random.randint(0,i-1)
    else:
        numero_random_envio = 0
    persona = lista_nombres[numero_random]
    persona2 = lista_nombres2[numero_random_envio]
    if persona != persona2:
        lista_nombres.pop(numero_random)
        lista_nombres2.pop(numero_random_envio)
        #Creamos fichero para cada persona
        archivo = open("path to save file " + str(persona2) + ".txt", "w")
        archivo.write(persona +  '\n')
        time.sleep(1)
        archivo.close()
        i -= 1
        print("He introducido a " + str(persona2) )