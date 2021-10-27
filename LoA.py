from os import system, name
import random

def clear():

    # para windows
    if name == 'nt':
        _ = system('cls')

    # para mac o linux
    else:
        _ = system('clear')

clear()

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
    clear()

    if valor == 1:
        rango = int(input("Digite el tamano de la lista de emparejamiento que desea: "))
        #rango = random.randrange(1, 10)

        #print(random.random()*8.99)

        while rango > 0:
            numero_random = random.uniform(0.00, 8.99)
            #interfaz = random.random()*8.99
            formato_al_numero = float("{:.2f}".format(numero_random))
            lista.append(formato_al_numero)
            rango -= 1

        ordenada = lista.copy()
        ordenada.sort()
        print(lista)
        input("Lista inicial creada! Presione Enter para volver al menu principal")
        clear()
        
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
        input("Listas ordenadas creadas! Presione Enter para volver al menu principal")
        clear()

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
        clear()

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
                print("El jugador con la mayor division es Jugador #:", cont_two+1)
            cont_two += 1
        input("Presione Enter para volver al menu principal")
        clear()

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
                print("El Jugador con la menor division es Jugador #:", cont+1)
            cont += 1
        input("Presione Enter para volver al menu principal")
        clear()

    elif valor == 7: 
        cont = 0
        valor = 0
        while cont < len(ordenada):
            valor += lista[cont]
            cont += 1
        valor = valor/len(lista)
        print("El promedio de todas las divisionses es de","%.2f" % valor)
        input("Presione Enter para volver al menu principal")
        clear()

    elif valor == 8: 
        if len(hierro) > 0:
            print("0. Hierro")
        else:
            pass
        
        if len(bronce) > 0:
            print("1. Bronce")
        else:
            pass

        if len(plata) > 0:
            print("2. Plata")
        else:
            pass

        if len(oro) > 0:
            print("3. Oro")
        else:
            pass

        if len(platino) > 0:
            print("4. Platino")
        else:
            pass 
        
        if len(diamante) > 0:
            print("5. Diamante")
        else:
            pass

        if len(maestro) > 0:
            print("6. Maestro")
        else:
            pass

        if len(gran_maestro) > 0:
            print("7. Gran Maestro")
        else:
            pass

        if len(retador) > 0:
            print("8. Retador")
        else:
            pass
        
        print("9. Volver al menu anterior")
        opcion = int(input("Digite la division que desea ver el promedio: "))
        clear()
        cont = 0
        bandera2 = True
        valor = 0
        while bandera2: 
            if opcion == 0:
                while cont < len(hierro):
                    valor += hierro[cont]
                    cont += 1
                valor = valor/len(hierro)
                print("El promedio de la division Hierro es de","%.2f" % valor)
                input("Presione Enter para volver al menu principal")
                bandera2 = False
                clear()

            elif opcion == 1:
                while cont < len(bronce):
                    valor += bronce[cont]
                    cont += 1
                valor = valor/len(bronce)
                print("El promedio de la division Bronce es de","%.2f" % valor)
                input("Presione Enter para volver al menu principal")
                bandera2 = False
                clear()

            elif opcion == 2:
                while cont < len(plata):
                    valor += plata[cont]
                    cont += 1
                valor = valor/len(plata)
                print("El promedio de la division Plata es de","%.2f" % valor)
                input("Presione Enter para volver al menu principal")
                bandera2 = False
                clear()

            elif opcion == 3:
                while cont < len(oro):
                    valor += oro[cont]
                    cont += 1
                valor = valor/len(oro)
                print("El promedio de la division Oro es de","%.2f" % valor)
                input("Presione Enter para volver al menu principal")
                bandera2 = False
                clear()

            elif opcion == 4:
                while cont < len(platino):
                    valor += platino[cont]
                    cont += 1
                valor = valor/len(platino)
                print("El promedio de la division Platino es de","%.2f" % valor)
                input("Presione Enter para volver al menu principal")
                bandera2 = False
                clear()

            elif opcion == 5:
                while cont < len(diamante):
                    valor += diamante[cont]
                    cont += 1
                valor = valor/len(diamante)
                print("El promedio de la division Diamante es de","%.2f" % valor)
                input("Presione Enter para volver al menu principal")
                bandera2 = False
                clear()

            elif opcion == 6:
                while cont < len(maestro):
                    valor += maestro[cont]
                    cont += 1
                valor = valor/len(maestro)
                print("El promedio de la division Maestro es de","%.2f" % valor)
                input("Presione Enter para volver al menu principal")
                bandera2 = False
                clear()

            elif opcion == 7:
                while cont < len(gran_maestro):
                    valor += gran_maestro[cont]
                    cont += 1
                valor = valor/len(gran_maestro)
                print("El promedio de la division Gran Maestro es de","%.2f" % valor)
                input("Presione Enter para volver al menu principal")
                bandera2 = False
                clear()

            elif opcion == 8:
                while cont < len(retador):
                    valor += retador[cont]
                    cont += 1
                valor = valor/len(retador)
                print("El promedio de la division Retador es de","%.2f" % valor)
                input("Presione Enter para volver al menu principal")
                bandera2 = False
                clear()
            else: 
                clear()
                bandera2 = False
                
    elif valor == 9:

        valor_bronce = 0
        valor_hierro = 0
        valor_plata = 0
        valor_oro = 0
        valor_platino = 0
        valor_diamante = 0
        valor_maestro = 0
        valor_gran_maestro = 0
        valor_retador = 0

        contador_promedio = 0
        
        if len(hierro) > 0:
            valor = 0
            cont = 0
            while cont < len(hierro):
                puntuacion = str(hierro[cont])
                valor += int(puntuacion.split(".")[1])
                cont += 1
                valor_hierro = valor/len(hierro)
                contador_promedio += 1
        else:
            valor_hierro = 0
        
        if len(bronce) > 0:
            valor = 0
            cont = 0
            while cont < len(bronce):
                puntuacion = str(bronce[cont])
                valor += int(puntuacion.split(".")[1])
                cont += 1
                valor_bronce = valor/len(bronce)
                contador_promedio += 1
        else:
            valor_bronce = 0

        if len(plata) > 0:
            valor = 0
            cont = 0
            while cont < len(plata):
                puntuacion = str(plata[cont])
                valor += int(puntuacion.split(".")[1])
                cont += 1
                valor_plata = valor/len(plata)
                contador_promedio += 1
        else:
            valor_plata = 0

        if len(oro) > 0:
            valor = 0
            cont = 0
            while cont < len(oro):
                puntuacion = str(oro[cont])
                valor += int(puntuacion.split(".")[1])
                cont += 1
                valor_oro = valor/len(oro)
                contador_promedio += 1
        else:
            valor_oro = 0

        if len(platino) > 0:
            valor = 0
            cont = 0
            while cont < len(platino):
                puntuacion = str(platino[cont])
                valor += int(puntuacion.split(".")[1])
                cont += 1
                valor_platino = valor/len(platino)
                contador_promedio += 1
        else:
            valor_platino = 0

        if len(diamante) > 0:
            valor = 0
            cont = 0
            while cont < len(diamante):
                puntuacion = str(diamante[cont])
                valor += int(puntuacion.split(".")[1])
                cont += 1
                valor_diamante = valor/len(diamante)
                contador_promedio += 1
        else:
            valor_diamante = 0
        
        if len(maestro) > 0:
            valor = 0
            cont = 0
            while cont < len(maestro):
                puntuacion = str(maestro[cont])
                valor += int(puntuacion.split(".")[1])
                cont += 1
                valor_maestro = valor/len(maestro)
                contador_promedio += 1
        else:
            valor_maestro = 0

        if len(gran_maestro) > 0:
            valor = 0
            cont = 0
            while cont < len(gran_maestro):
                puntuacion = str(gran_maestro[cont])
                valor += int(puntuacion.split(".")[1])
                cont += 1
                valor_gran_maestro = valor/len(gran_maestro)
                contador_promedio += 1
        else:
            valor_gran_maestro = 0

        if len(retador) > 0:
            valor = 0
            cont = 0
            while cont < len(retador):
                puntuacion = str(retador[cont])
                valor += int(puntuacion.split(".")[1])
                cont += 1
                valor_retador = valor/len(retador)
                contador_promedio += 1
        else:
            valor_retador = 0

        print("El promedio de puntuacion de todas las divisiones es de","%.2f" % ((valor_hierro + valor_bronce + valor_plata + valor_oro + valor_platino + valor_diamante + valor_gran_maestro + valor_retador) / contador_promedio))
        input("Digite la tecla Enter para continuar")
        clear()

    elif valor == 12:
        clear()
        bandera = False
