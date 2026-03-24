#LIBRERIAS
from clientes import buscarcliente, registrar_cliente #IMPORTAMOS FUNCIONES DE CLIENTES
import datetime
import unicodedata
import reservas
#FUNCION DE LIMPIEZA DE DATOS.
def limpiardatos (nombres, apellidos):
    nombres = nombres.strip().lower()
    apellidos = apellidos.strip().lower()
    nombres = unicodedata.normalize('NFD', nombres)
    apellidos= unicodedata.normalize('NFD', apellidos)
    nombres =''.join(c for c in nombres if unicodedata.category(c) != 'Mn')
    apellidos = ''.join(c for c in apellidos if unicodedata.category(c)!= 'Mn')
    return (nombres, apellidos)

#FUNCION DE VALIDACIÓN DE FECHAS
def validar_fecha (fecha):
    try:
        fecha_funcion = datetime.date.strptime(fecha, '%d/%m/%Y')
        return (fecha_funcion)
    except ValueError:
        return None

#FUNCION PARA VALIDACIÓN DE HORAS.
def validar_hora(hora_inicio, hora_fin):
    try: 
        hora_funcion_1 = datetime.time.strptime(hora_inicio, "%H:%M")
        hora_funcion_2 = datetime.time.strptime(hora_fin,"%H:%M" )
        return(hora_funcion_1, hora_funcion_2) 
    except ValueError:
        return None

#INGRESO DE DATOS
while True:
    nombres = input('Ingresa tus nombre/s (si tienes 2): ')
    apellidos = input('Ingresa tus apellidos: ')
    telefono = input('Ingresa tu numero de telefono: ')
    correo = input('ingresa tu correo: ')

    if nombres != '' and apellidos != '':
        nombres, apellidos = limpiardatos(nombres, apellidos)
        print (nombres, apellidos)
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) <11:
            print('hasta aqui todo bien.')
            break
        else:
            print('Ingresa números únicamente, o verifica que no estes dejando espacios en blanco')
            continue

#FUNCION PARA BUSCAR A CLIENTE (DENTRO DEL MODULO DE CLIENTES)
id_cliente= buscarcliente(nombres, apellidos, telefono, correo)

while True:
    if id_cliente:
        print (f'Bienvenido/a al sistema de reservas ')
        break
    else: 
        crear =input(f'El usuario con el nombre: {nombres} no existe ¿desea crearlo?: ').lower().strip()
        match crear:
            case 'si'|'ci'|'zi'|'s':
                id_cliente= registrar_cliente(nombres, apellidos, telefono, correo)
                break
            case 'no'|'n':
                print('Te agracedemos por usar nuestros sevicios, vuelve pronto 👋')
                break    
            case _:
                print('La opción que elegiste no es válida o no existe valida he intenta de nuevo')
                continue
print(f'Hola {nombres}')

while True:
    Eleccion = input('Menú\n1)Reservar\n2)Checar Reservación\n3)Cancelar reservación\n4)Editar reservación\n5)Salir\nElige una opción:  ')
    match Eleccion:
        case '1':
            pass

        case '2':
            while True:
                a = input('¿Cuentas con el ID de tu reserva?: ')
                match a:
                    case 'si'|'ci'|'zi'|'s'|'sy'|'cy'|'zy':
                        id_reserva = input('Ingresa el ID de tu reserva: ')
                        fecha, hora_inicio, hora_fin, estatus= reservas.checar_reserva_por_id(id_reserva)
                        if id_reserva and estatus == 'activo':
                            print(f'Tienes una reservación con la fecha: {fecha}\nHora de inicio:{hora_inicio}, Hora fin: {hora_fin}')
                            break
                        elif id_reserva and estatus == 'modificado':
                            print (f'Tu reservación ya ha sido modificada\nFecha: {fecha}, Hora de Inicio: {hora_inicio}, hora fin: {hora_fin} ')
                        elif id_reserva and estatus == 'cancelado':
                            print('Tu reservación ha sido cancelada')
                        else:
                            print('No se encontro el id de tu reserva se te redigira a la pestaña principal')
                            continue

                    case 'no':
                        fecha = input('Ingresa la fecha de tu reservación (DD/MM/YYYY): ')
                        hora_inicio = input('Ingresa la hora de inicio de tu reserva (HH:MM)')
                        hora_fin = input('Ingresa la hora de fin de la reserva (HH:MM): ')
                        fecha = validar_fecha(fecha)
                        hora_inicio, hora_fin = validar_hora(hora_inicio, hora_fin)
                        if fecha and hora_inicio and hora_fin:
                            id_reserva, estatus = reservas.checar_reserva(id_cliente, fecha)
                            if id_reserva and estatus == 'Activo':
                                print(f'Tu reserva esta activa, con el numero de reservación: {id_reserva}')
                                break
                            elif id_reserva and estatus == 'modificado':
                                print(f'Esta reserva ya fue modificada, tu Id es: {id_reserva}')
                                break
                            elif id_reserva and estatus == 'cancelado':
                                print('Tu reservación ha sido cancelada')
                                break
                            else:
                                print('No se encontro el id de la reserva, verifica bien las fechas, horas e intenta de nuevo.\nSe te redigira al inicio.')
                                continue
                        else:
                            print('Las fechas u horas que ingresaste no son válidas, verifica el formato sugerido e ingresa de nuevo.\nSe te redigira a la pantalla principal')
                            continue

                    case _:
                        print('La opción que seleccionaste no es válida')
                        continue

        case '3':
            while True:
                b = input('¿Cuentas con el nunmero de reservación?: ')
                match b:
                    case 'si'|'ci'|'zi'|'s'|'sy'|'cy'|'zy':
                        id_reserva = input('Ingresa el numero de tu reservación: ')
                    case 'no':
                        fecha= input('Ingresa la fecha de la reservación (DD/MM/YYYY): ')
                        hora_inicio = input('Ingresa tu hora de inicio de la reservación (HH:MM): ')
                        hora_fin = input('Ingresa la hora de fin de la reserva (HH:MM): ')
                        id_reserva = reservas.checar_reserva(fecha, hora_inicio, hora_fin)
                    case _:
                        print('La opción que elegiste no es válida.')
                        continue

        case '4':
            pass

        case '5':
            print('Gracias por usar nuestros servicios')
            break
        case _:
            print('La opción que elegiste no es válida intenta de nuevo')
            continue