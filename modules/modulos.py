import os
from tabulate import tabulate

#Función para registrar el equipo 
def regitro(liga:list):
    registrar = True
    while (registrar):
        os.system('cls')
        equipo = input('Nombre del equipo : ').upper()
        liga.append([equipo,[]])
        liga.sort()
        registrar = bool(input('Desea registar un nuevo equipo... s(si) o enter(no)'))
    
    

#Funcion Mostrar los equipos registrados. 
def mostrarEquipos(liga: list):
    encabezado = """
    *********************
    * GRAN LIGA BETPLAY *
    *********************
    """
    print(encabezado)
    for i,item in enumerate(liga):
        equipo,datos = item
        print(f'{i+1}.{equipo}')
    os.system('pause')

#Registros de datos de temporada para el equipo seleccionado. 
def reg_Datos(liga: list):
    if (len(liga) <= 0):
        print('No se encuentran datos registrados')
        os.system('pause')
    else:
        registro = True
        while registro:
            encabezado = """
            ******************************************
            * REGISTO DE INFORMACION DE LA TEMPORADA *
            ******************************************
            """
            print(encabezado)
            print('Selccione el equipo al cual agregará los datos de la temporada...')
            for i,item in enumerate(liga):
                equipo,datos = item
                print(f'{i+1}=>{equipo}')
            seleccion = int(input('=>'))
            numero = seleccion - 1
            os.system('cls')
            for i,item in enumerate(liga):
                equipo,datos = item
                if i == numero:
                    numero = equipo
            print(f'Ingresará los datos de temporada para {numero} ')
            pj = int(input('Patidos jugados: '))
            pg = int(input('Partidos ganados: '))
            pp = int(input('Partidos perdidos: '))
            pe = int(input('Partidos empatados: '))
            gf = int(input('Goles a favor: '))
            gc = int(input('Goles en contra:'))
            tp = int(input('Total puntos: '))
            liga[seleccion-1][1].append([pj,pg,pp,pe,gf,gc,tp])
            registro = bool(input('Desea registar un nuevo equipo... s(si) o enter(no)'))
        os.system('pause')

#Tabulación de los datos. 
def datosTemporada(liga : list):
    os.system('cls')
    encabezado = """
    *******************************
    * INFORMACIÓN DE LA TEMPORADA *
    *******************************
    """
    print(encabezado)

# Desempaquetar los datos
    formatear_data = []
    for equipo, dato in liga:
        if dato:
            formatear_data.append([equipo] + dato[0])
        else:
            formatear_data.append([equipo])

    # Tabular los datos
    print(tabulate(formatear_data, headers=['Equipo', 'PJ', 'PG', 'PP', 'PE', 'GF', 'GC', 'TP']))
    os.system('pause')
