import os
import modules.modulos as fun
ligaBetplay = []
op = 0
    
if __name__ == '__main__':
    title= """
    ***************************************
    * LIGA DE FUTBOL COLOMBIANO - BETPLAY *
    ***************************************
    """
    menuP = '1.Registrar equipos\n2.Mostrar equipos participantes\n3.Registrar resultados de la liga\n4.Resultados\n5.Salir'
    while op < 5:
        print(title)
        print(menuP)   
        op = int (input('=>'))
        os.system('cls')
        match op: 
            case 1:
                fun.regitro(ligaBetplay)
            case 2:
                fun.mostrarEquipos(ligaBetplay)
            case 3:
                fun.reg_Datos(ligaBetplay)
            case 4:
                fun.datosTemporada(ligaBetplay)
            case 5:
                print('Un gusto servirle... Vuelva pronto...')
                os.system('pause')
            case _:
                print('Opcion inválida...')
                op = 0
                os.system('pause')
                os.system('cls')
        