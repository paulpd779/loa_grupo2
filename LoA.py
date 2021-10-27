import random

lista = []
ordenada = []
bandera = True

while bandera:
    print("1. Generar lista de emparejamiento.")
    print("2. Ordenar los jugadores en las listas.")
    print("3. Mostrar la lista inicial de jugadores.")
    print("4. Mostrar las listas de cada división luego de ubicar a los jugadores.")
    print("5. El jugador con mayor división y puntuación.")
    print("6. El jugador con menor división y menor puntuación.")
    print("7. El promedio de todas las divisiones en base a cuantos jugadores contiene.")
    print("8. El promedio de puntuación dada una división.")
    print("9. El promedio de puntuación de todas las divisiones.")
    print("10. Cantidad de jugadores por división.")
    print("11. Cantidad de jugadores totales.")
    print("12. Salir del programa.")
    valor = int(input())
    if valor == 1:
        rango = random.randrange(1, 10) #de momento este valor va a quedar en 10 para facilitar la programacion pero en realidad tiene que estar en 1 millon como dijo el profe. "Cree una lista de 1 a 1 millon" 

        while rango > 1:
            numero_random = random.uniform(0.00, 8.99) # se selecciona un numero de 0.00 a 8.99
            formato_al_numero = float("{:.2f}".format(numero_random)) # se le da formato al numero anterior para que queden solo dos decimales. Si saben de una forma mejor de como hacerlo por favor hacer el cambio
            lista.append(formato_al_numero)
            rango -= 1

        ordenada = lista.copy() # se hace una copia real de la lista
        ordenada.sort() #se ordena la lista
        print(lista)
        input("Presione Enter para volver al menu principal")
        
    elif valor == 2:
        hierro = []
        bronce = []
        plata = []
        oro = []
        platino = []
        diamante = []
        maestro = []
        gran_maestro = []
        retador = []

        contar = 0

        while contar < len(ordenada):
            if (ordenada[contar] >= 0.00) and (ordenada[contar] <= 0.99):
                hierro.append(ordenada[contar])
            elif ordenada[contar] >= 1.00 and ordenada[contar] <= 1.99:
                bronce.append(ordenada[contar])
            elif ordenada[contar] >= 2.00 and ordenada[contar] <= 2.99:
                plata.append(ordenada[contar]) 
            elif ordenada[contar] >= 3.00 and ordenada[contar] <= 3.99:
                oro.append(ordenada[contar])
            elif ordenada[contar] >= 4.00 and ordenada[contar] <= 4.99:
                platino.append(ordenada[contar])
            elif ordenada[contar] >= 5.00 and ordenada[contar] <= 5.99:
                diamante.append(ordenada[contar])
            elif ordenada[contar] >= 6.00 and ordenada[contar] <= 6.99:
                maestro.append(ordenada[contar])
            elif ordenada[contar] >= 7.00 and ordenada[contar] <= 7.99:
                gran_maestro.append(ordenada[contar])
            else:
                retador.append(ordenada[contar])
            contar += 1
        print(ordenada)
        input("Listas ordenadas. Presione Enter para volver al menu principal")

    elif valor == 3:
        contador = 0
        jugador = 1
        print(lista)
        while contador < len(lista):
            print( "Jugador # " + str(jugador) + " con rango " + str(lista[contador]))
            contador +=1
            jugador += 1
        input("Presione Enter para volver al menu principal")

    elif valor == 4:
        print("Esta es la lista de hierro: ", hierro)
        print("Esta es la lista de bronce: ", bronce)
        print("Esta es la lista de plata: ", plata)
        print("Esta es la lista de oro: ", oro)
        print("Esta es la lista de platino: ", platino)
        print("Esta es la lista de diamante: ", diamante)
        print("Esta es la lista de maestro: ", maestro)
        print("Esta es la lista de gran maestro: ", gran_maestro)
        print("Esta es la lista de retador: ", retador)
        input("Presione Enter para volver al menu principal")

    elif valor == 5: 
        cont = 0
        valor = 0
        while cont < len(ordenada):
            if lista[cont] > valor:
                valor = lista[cont]
            cont += 1
        print(valor)

        cont_two = 0
        while cont_two < len(lista):
            if valor == lista[cont_two]:
                print("Jugador #:", cont_two+1)
            cont_two += 1
        input("Presione Enter para volver al menu principal")

    elif valor == 6: 
        cont = 0
        valor = 8.99
        while cont < len(ordenada):
            if lista[cont] < valor:
                valor = lista[cont]
            cont += 1
        print(valor)

        cont = 0
        while cont < len(lista):
            if valor == lista[cont]:
                print("Jugador #:", cont+1)
            cont += 1
        input("Presione Enter para volver al menu principal")

    elif valor == 7: 
        cont = 0
        valor = 0
        while cont < len(ordenada):
            valor += lista[cont]
            cont += 1
        valor = valor/len(lista)
        print("%.2f" % valor)
        input("Presione Enter para volver al menu principal")

    elif valor == 8: 
        print("0. Hierro")
        print("1. Bronce")
        print("2. Plata")
        print("3. Oro")
        print("4. Platino")
        print("5. Diamante")
        print("6. Maestro")
        print("7. Gran Maestro")
        print("8. Retador")
        print("9. Volver al menu anterior")
        opcion = int(input("Digite la division que desea ver el promedio"))
        cont = 0
        bandera = True
        valor = 0
        while bandera: 
            if opcion == 0:
                while cont < len(hierro):
                    valor += hierro[cont]
                    cont += 1
                valor = valor/len(hierro)
                print("%.2f" % valor)
                input("Presione Enter para volver al menu principal")

            elif opcion == 1:
                while cont < len(bronce):
                    valor += bronce[cont]
                    cont += 1
                valor = valor/len(bronce)
                print("%.2f" % valor)
                input("Presione Enter para volver al menu principal")

            elif opcion == 2:
                while cont < len(plata):
                    valor += plata[cont]
                    cont += 1
                valor = valor/len(plata)
                print("%.2f" % valor)
                input("Presione Enter para volver al menu principal")

            elif opcion == 3:
                while cont < len(oro):
                    valor += oro[cont]
                    cont += 1
                valor = valor/len(oro)
                print("%.2f" % valor)
                input("Presione Enter para volver al menu principal")

            elif opcion == 4:
                while cont < len(platino):
                    valor += platino[cont]
                    cont += 1
                valor = valor/len(platino)
                print("%.2f" % valor)
                input("Presione Enter para volver al menu principal")

            elif opcion == 5:
                while cont < len(diamante):
                    valor += diamante[cont]
                    cont += 1
                valor = valor/len(diamante)
                print("%.2f" % valor)
                input("Presione Enter para volver al menu principal")

            elif opcion == 6:
                while cont < len(maestro):
                    valor += maestro[cont]
                    cont += 1
                valor = valor/len(maestro)
                print("%.2f" % valor)
                input("Presione Enter para volver al menu principal")

            elif opcion == 7:
                while cont < len(gran_maestro):
                    valor += gran_maestro[cont]
                    cont += 1
                valor = valor/len(gran_maestro)
                print("%.2f" % valor)
                input("Presione Enter para volver al menu principal")

            elif opcion == 8:
                while cont < len(retador):
                    valor += retador[cont]
                    cont += 1
                valor = valor/len(retador)
                print("%.2f" % valor)
                input("Presione Enter para volver al menu principal")
            else: 
                bandera = False

    elif valor == 12:
        bandera = False

    
'''
#lista por comprension / comprenhension list

hierro = [i for i in lista if i>= 0.00 and i <= 0.99]
bronce = [i for i in lista if i>= 1.00 and i <= 1.99]
plata = [i for i in lista if i>= 2.00 and i <= 2.99]
oro = [i for i in lista if i>= 3.00 and i <= 3.99]
platino = [i for i in lista if i>= 4.00 and i <= 4.99]
diamante = [i for i in lista if i>= 5.00 and i <= 5.99]
maestro = [i for i in lista if i>= 6.00 and i <= 6.99]
gran_maestro = [i for i in lista if i>= 7.00 and i <= 7.99]
retador = [i for i in lista if i>= 8.00 and i <= 8.99]
'''



