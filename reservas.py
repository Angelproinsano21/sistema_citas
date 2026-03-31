import os
#ruta_reservas = r'D:\Lenguajes de Programación\Curso de Programación con Python\Proyecto Integrador\sistema_citas\data\reserva.txt'
ruta_base = os.path.dirname(__file__)
ruta_reservas= os.path.join(ruta_base, 'data', 'reserva.txt')

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
            return None

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
    nuevas_lineas = []
    encontrado = False
    with open(ruta_reservas, 'r', encoding='utf-8') as reservas:
        for linea in reservas:
            campos = linea.strip().split(';')
            id_archivo = campos[0]
            if id_archivo == id_reserva:
                campos[6] = 'cancelada'
                encontrado = True
            nuevas_lineas.append(';'.join(campos))
    with open(ruta_reservas, 'w', encoding='utf-8') as reservas:
        for linea in nuevas_lineas:
            reservas.write(linea + '\n')
    return encontrado


def cancelar_reserva(id_cliente, fecha):
    nuevas_lineas = []
    encontrado = False
    with open(ruta_reservas, 'r', encoding='utf-8') as reservas:
        for linea in reservas:
            campos = linea.strip().split(';')
            id_archivo = campos[0] 
            id_cliente_archivo = campos[1]
                




            

            

"""id_cliente = input('No. Cliente: ')
fecha = input('Ingresa la fecha de tu reservación (DD/MM/YYYY): ')
hora_inicio = input('Ingresa la hora de inicio de tu reserva (HH:MM): ')
hora_fin = input('Ingresa la hora de fin de la reserva (HH:MM): ')
checar_reserva(id_cliente, fecha, hora_inicio, hora_fin)
"""
