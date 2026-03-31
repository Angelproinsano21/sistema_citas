#LIBRERIAS
from clientes import buscarcliente, registrar_cliente #IMPORTAMOS FUNCIONES DE CLIENTES
import reservas
from utils import limpiardatos, validar_fecha, validar_hora 

#FUNCION PARA INGRESO DE DATOS
def pedir_datos():
    while True:
        nombres = input('Ingresa tus nombre/s (si tienes 2): ')
        apellidos = input('Ingresa tus apellidos: ')
        telefono = input('Ingresa tu numero de telefono: ')
        correo = input('ingresa tu correo: ')

        if nombres != '' and apellidos != '':
            nombres, apellidos = limpiardatos(nombres, apellidos)

            if telefono.isdigit() and len(telefono) > 0 and len(telefono) <11:
                print('hasta aqui todo bien.')
                break

            else:
                print('Ingresa números únicamente, o verifica que no estes dejando espacios en blanco')
                continue
def main():
    #INGRESO DE DATOS
    nombres, apellidos, telefono, correo = pedir_datos ()

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
            case '1': #CREAR LA RESERVACION
                fecha = input('Ingresa la fecha que quieres reservar (DD/MM/YYYY): ')
                pass

            case '2': #CHECAR LA RESERVACION
                while True:
                    a = input('¿Cuentas con el ID de tu reserva?: ')
                    match a:
                        case 'si'|'ci'|'zi'|'s'|'sy'|'cy'|'zy':
                            id_reserva = input('Ingresa el ID de tu reserva: ')
                            fecha, hora_inicio, hora_fin, estatus= reservas.checar_reserva_por_id(id_reserva)
                            if id_reserva and estatus == 'activo':
                                print(f'Tienes una reservación con la fecha: {fecha}\nHora de inicio:{hora_inicio}, Hora fin: {hora_fin}, Con estatus: {estatus}')
                                break
                            elif id_reserva and estatus == 'modificado':
                                print (f'Tu reservación ya ha sido modificada\nDATOS DE LA RESERVACIÓN:\nFecha: {fecha}, Hora de Inicio: {hora_inicio}, hora fin: {hora_fin} ')
                                break
                            elif id_reserva and estatus == 'cancelado':
                                print('Tu reservación ha sido cancelada')
                                break
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

            case '3': #CANCELAR RESERVACION 
                seguir= True
                while seguir: #Variable bandera para asegurar que todo esta bien 
                    b = input('¿Cuentas con el nunmero de reservación?: ')
                    match b:
                        case 'si'|'ci'|'zi'|'s'|'sy'|'cy'|'zy':
                            id_reserva = input('Ingresa el numero de tu reservación: ') 
                            encontrado = reservas.cancelar_reserva(id_reserva)
                            if encontrado == True:
                                print(f'La reservación con ID: {id_reserva}, ha sido cancelada con éxito ')
                            else:
                                print('No se encontro la reserva')

                        case 'no':
                            while True:
                                fecha= input('Ingresa la fecha de la reservación (DD/MM/YYYY): ')
                                fecha = validar_fecha(fecha)

                                hora_inicio = input('Ingresa tu hora de inicio de la reservación (HH:MM): ')
                                hora_fin = input('Ingresa la hora de fin de la reserva (HH:MM): ')

                                hora_inicio, hora_fin = validar_hora(hora_inicio, hora_fin)

                                id_reserva = reservas.checar_reserva(fecha, hora_inicio, hora_fin)
                                encontrado = reservas.cancelar_reserva(id_reserva)

                                if fecha != None and hora_inicio != None and hora_fin != None:
                                    if encontrado == True:
                                        print(f'La reservación con ID: {id_reserva}, ha sido cancelada con éxito, se te redigira a la pagina de inicio, gracias')
                                        seguir = False
                                        break
                                    else:
                                        print('No se encontro la reserva')
                                        continue

                                else: 
                                    print('Los datos ingresados para la consulta de la reserva no son válidos, intenta de nuevo.')
                                    continue
            
            
            case '4': #EDITAR LA RESERVACION
                pass

            case '5': #SALIR
                print('Gracias por usar nuestros servicios')
                break
            case _: #SI NO FUNCIONA NINGUNA
                print('La opción que elegiste no es válida intenta de nuevo')
                continue