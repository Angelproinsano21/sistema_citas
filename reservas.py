
ruta_reservas = r'D:\Lenguajes de Programación\Curso de Programación con Python\Proyecto Integrador\sistema_citas\data\reserva.txt'

def buscarDisponibilidad(id_mesa, fecha, hora):
    pass

def nueva_reserva (id_reserva,id_cliente, id_mesa, fecha, hora_incio, hora_fin):
    pass

def modificar_reserva():
    pass

def checar_reserva(id_cliente, fecha):
    with open (ruta_reservas, 'r', encoding='utf-8') as reservas:
        for buscar in reservas:
            buscar = buscar.strip().split(';')
            id_reserva = buscar[0]
            id_cl_archivo = buscar[1]
            fecha_archivo  = buscar[3]
            estatus_archivo = buscar[6]
            if id_cliente == id_cl_archivo and fecha == fecha_archivo:
                return(id_reserva, estatus_archivo)
        else:
            return(None)

def checar_reserva_por_id (id_reserva):
    with open(ruta_reservas, 'r', encoding='utf-8') as reservas:
        for buscar in reservas:
            buscar = buscar.strip().split(';')
            id_reserva_archivo = buscar [0]
            fecha_archivo = buscar[3]
            hora_inicio_archivo = buscar[4]
            hora_fin_archivo = buscar[5]
            estatus_archivo = buscar[6]
            if id_reserva == id_reserva_archivo:
                return(fecha_archivo, hora_inicio_archivo, hora_fin_archivo, estatus_archivo)
        else:
            return(None)                
def cancelar_reserva_por_id(id_reserva):
    with open (ruta_reservas, 'r', encoding='utf-8') as reservas: 
        for lineas in reservas:
            lineas = lineas.strip().split(';')
            id_archivo = lineas[0]
            id_cliente = lineas[1]
            id_mesa = lineas[2]
            fecha = lineas[3]
            hora_inicio = lineas[4]
            hora_fin = lineas[5]
            estatus = lineas[6]
        if id_reserva == id_archivo:
            estatus = 'cancelada'
            with open (ruta_reservas, 'w', encoding='utf-8') as reservas:
                reservas.write(f'{id_archivo};{id_cliente};{id_mesa};{fecha};{hora_inicio};{hora_fin};{estatus}')
                




            

            

"""id_cliente = input('No. Cliente: ')
fecha = input('Ingresa la fecha de tu reservación (DD/MM/YYYY): ')
hora_inicio = input('Ingresa la hora de inicio de tu reserva (HH:MM): ')
hora_fin = input('Ingresa la hora de fin de la reserva (HH:MM): ')
checar_reserva(id_cliente, fecha, hora_inicio, hora_fin)
"""
