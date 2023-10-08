import numpy as np
import time
import barcos_variables as var

# INICIALIZAR TABLERO JUGADOR
def init_tablero_mio(fill):
    var.tablero_mio = np.full((10,10),' ')
    print(var.tablero_mio)

# INICIALIZAR TABLERO MAQUINA (OCULTO PARA EL JUGADOR)
def init_tablero_maquina(fill):
    var.tablero_maquina = np.full((10,10),' ')

# INICIALIZAR TABLERO VISIBLE (BASADO EN TABLERO MAQUINA)
def init_tablero_visible(fill):
    var.tablero_visible = np.full((10,10),'?')
    print(var.tablero_visible)

# GENERAR BARCO SIMPLE --> FUNCIONA PARA EL JUGADOR (MANUAL) Y PARA LA MAQUINA (ALEATORIO)
def generar_barco_simple (tablero,eslora,tablero_auto=True):
    if tablero_auto:
        orientacion = np.random.choice(['N','S','E','W'])
    
    else:
        orientacion = input('Introduce uno de estos: N, S, E, W')

    if orientacion == 'E':
        
        while True:
            if tablero_auto:
                barco_x = np.random.randint(0,10)
                barco_y = np.random.randint(0,10)

            else:
                barco_x = int(input('Introduce una coordenada X entre 0 y 9 inclusive'))
                barco_y = int(input('Introduce una coordenada Y entre 0 y 9 inclusive'))

            if barco_y <= (10-eslora) and all(hueco != 'O' for hueco in tablero[barco_x , barco_y : barco_y + eslora]):
                tablero[barco_x , barco_y : barco_y + eslora] = 'O'
                break
    
    elif orientacion == 'W':

        while True:
            if tablero_auto:
                barco_x = np.random.randint(0,10)
                barco_y = np.random.randint(0,10)

            else:
                barco_x = int(input('Introduce una coordenada X entre 0 y 9 inclusive'))
                barco_y = int(input('Introduce una coordenada Y entre 0 y 9 inclusive'))
            
            if barco_y >= (eslora-1) and all(hueco != 'O' for hueco in tablero[barco_x, barco_y - eslora : barco_y]):
                tablero[barco_x, barco_y - eslora : barco_y] = 'O'
                break

    elif orientacion == 'N':
        
        while True:
            if tablero_auto:
                barco_x = np.random.randint(0,10)
                barco_y = np.random.randint(0,10)

            else:
                barco_x = int(input('Introduce una coordenada X entre 0 y 9 inclusive'))
                barco_y = int(input('Introduce una coordenada Y entre 0 y 9 inclusive'))
            
            if barco_x >= (eslora-1) and all(hueco != 'O' for hueco in tablero[barco_x - eslora : barco_x, barco_y]):
                tablero[barco_x - eslora : barco_x, barco_y] = 'O'
                break
        
    elif orientacion == 'S':

        while True:
            if tablero_auto:
                barco_x = np.random.randint(0,10)
                barco_y = np.random.randint(0,10)

            else:
                barco_x = int(input('Introduce una coordenada X entre 0 y 9 inclusive'))
                barco_y = int(input('Introduce una coordenada Y entre 0 y 9 inclusive'))

            if barco_x <= (10-eslora) and all(hueco != 'O' for hueco in tablero[barco_x : barco_x + eslora, barco_y]):
                tablero[barco_x : barco_x + eslora, barco_y] = 'O'
                break
    
# GENERAR TODOS LOS BARCOS DEL JUGADOR. TENIENDO EN CUENTA LA CANTIDAD DE BARCOS QUE HAY DE CADA TIPO. PIDE COORDENADAS
def generar_todos_los_barcos_mios():
    cantidad_barcos_4_eslora = 1
    cantidad_barcos_3_eslora = 2
    cantidad_barcos_2_eslora = 3
    cantidad_barcos_1_eslora = 4
    
    for _ in range(cantidad_barcos_4_eslora):
        print('Introduce las coordenadas de tu barco de 4 de eslora')
        generar_barco_simple(var.tablero_mio,4,tablero_auto=False)
        print(var.tablero_mio)

    for _ in range(cantidad_barcos_3_eslora):
        print('Introduce las coordenadas de tu barco de 3 de eslora')
        generar_barco_simple(var.tablero_mio,3,tablero_auto=False)
        print(var.tablero_mio)

    for _ in range(cantidad_barcos_2_eslora):
        print('Introduce las coordenadas de tu barco de 2 de eslora')
        generar_barco_simple(var.tablero_mio,2,tablero_auto=False)
        print(var.tablero_mio)

    for _ in range(cantidad_barcos_1_eslora):
        print('Introduce las coordenadas de tu barco de 1 de eslora')
        generar_barco_simple(var.tablero_mio,1,tablero_auto=False)
        print(var.tablero_mio)

# GENERAR TODOS LOS BARCOS DEL JUGADOR
def generar_todos_los_barcos_maquina():
    cantidad_barcos_4_eslora = 1
    cantidad_barcos_3_eslora = 2
    cantidad_barcos_2_eslora = 3
    cantidad_barcos_1_eslora = 4
    
    for _ in range(cantidad_barcos_4_eslora):
        generar_barco_simple(var.tablero_maquina,4,tablero_auto=True)

    for _ in range(cantidad_barcos_3_eslora):
        generar_barco_simple(var.tablero_maquina,3,tablero_auto=False)

    for _ in range(cantidad_barcos_2_eslora):
        generar_barco_simple(var.tablero_maquina,2,tablero_auto=False)

    for _ in range(cantidad_barcos_1_eslora):
        generar_barco_simple(var.tablero_maquina,1,tablero_auto=False)

    print(var.tablero_maquina)

# FUNCION PARA DISPARAR. FUNCIONA PARA EL JUGADOR Y PARA LA MAQUINA
def disparar (tablero_mio,tablero_maquina,tablero_visible):

    turno_jugador = True
    contador_turnos_jugador = 0
    contador_turnos_maquina = 0

    while True:

        if turno_jugador == True:
            contador_turnos_jugador = contador_turnos_jugador +1
            if 'O' in tablero_maquina:
                disparo_mio_x = int(input('Introduce la coordenada X de tu disparo: [0,9]'))
                disparo_mio_y = int(input('Introduce la coordenada Y de tu disparo: [0,9]'))
                print(f'el turno actual del jugador es {contador_turnos_jugador}')
                
                if tablero_maquina[disparo_mio_x, disparo_mio_y] == "O":
                    tablero_maquina[disparo_mio_x, disparo_mio_y] = "X"
                    tablero_visible[disparo_mio_x, disparo_mio_y] = 'X'
                    print('EL JUGADOR LO HA TOCADO!')
                    print('TABLERO VISIBLE')
                    print(tablero_visible)
                    print('\n')
                    time.sleep(1)
                    
                    turno_jugador = True
                
                elif tablero_maquina[disparo_mio_x, disparo_mio_y] == "X":
                    print("Disparo previamente realizado por el jugador!")
                    print('TABLERO VISIBLE')
                    print(tablero_visible)
                    print('\n')
                    time.sleep(1)

                    turno_jugador = True

                elif tablero_maquina[disparo_mio_x, disparo_mio_y] == "-":
                    print("Disparo previamente realizado por el jugador!")
                    print('TABLERO VISIBLE')
                    print(tablero_visible)
                    print('\n')
                    time.sleep(1)
                    
                    turno_jugador = True

                elif tablero_maquina[disparo_mio_x, disparo_mio_y] == " ":
                    tablero_maquina[disparo_mio_x, disparo_mio_y] = "-"
                    tablero_visible[disparo_mio_x, disparo_mio_y] = '-'
                    print("EL JUGADOR HA DISPARADO AL AGUA!")
                    print('TABLERO VISIBLE')
                    print(tablero_visible)
                    print('\n')
                    time.sleep(1)
                    turno_jugador = False
                    continue

            else:
                print('HAS PERDIDO! MENUDO LOSER')
                break

        if turno_jugador == False:
            contador_turnos_maquina = contador_turnos_maquina +1
            if 'O' in tablero_mio:
                disparo_maquina_x = np.random.randint(0,10)
                disparo_maquina_y = np.random.randint(0,10)
                print(f'el turno actual de la máquina es {contador_turnos_maquina}')

                if tablero_mio[disparo_maquina_x, disparo_maquina_y] == "O":
                    tablero_mio[disparo_maquina_x, disparo_maquina_y] = "X"
                    print("LA MÁQUINA LO HA TOCADO!")
                    print('TABLERO DEL JUGADOR')
                    print(tablero_mio)
                    print('\n')
                    time.sleep(1)
                    turno_jugador = False

                elif tablero_mio[disparo_maquina_x, disparo_maquina_y] == " ":
                    tablero_mio[disparo_maquina_x, disparo_maquina_y] = "-"
                    print("LA MÁQUINA HA DISPARADO AL AGUA!")
                    print('TABLERO DEL JUGADOR')
                    print(tablero_mio)
                    print('\n')
                    time.sleep(1)
                    turno_jugador = True
                    
                elif tablero_mio[disparo_maquina_x, disparo_maquina_y] == "X":
                    print("Disparo previamente realizado por la máquina!")
                    print('TABLERO DEL JUGADOR')
                    print(tablero_mio)
                    print('\n')
                    time.sleep(1)
                    turno_jugador = False

                elif tablero_mio[disparo_maquina_x, disparo_maquina_y] == "-":
                    print("Disparo previamente realizado por la máquina!")
                    print('TABLERO DEL JUGADOR')
                    print(tablero_mio)
                    print('\n')
                    time.sleep(1)
                    turno_jugador = False

            else:
                print('FELICIDADES! HAS GANADO!!!!!!!')
                break