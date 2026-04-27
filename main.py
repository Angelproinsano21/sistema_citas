#LIBRERIAS
#from clientes import buscarcliente, registrar_cliente #IMPORTAMOS FUNCIONES DE CLIENTES
import reservas
import utils
import menus



def main():
    print (f'Bienvenido al sistema de reservas.\n1) Iniciar Sesión\n2) Crear cuenta')
    while True:
        Eleccion = input('Elige una opción: ')
        match Eleccion:
            case '1':
                id_cliente = menus.pedir_datos_inicio(id_cliente=None)
                break
            case '2':
                id_cliente = menus.pedir_datos_registro(id_cliente=None)
                break
            case _:
                print('Opción inválida intenta de nuevo.')
                continue

    while True:
        pass

main()