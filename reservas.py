import os
ruta_base = os.path.dirname(__file__)
ruta_reservas= os.path.join(ruta_base, 'data', 'reserva.txt')

def buscarDisponibilidad(id_mesa, fecha, hora):
    pass

def nueva_reserva (id_reserva,id_cliente, id_mesa, fecha, hora_incio, hora_fin):
    pass

def modificar_reserva(Id_reserva):
    with open (ruta_reservas, 'r', encoding='utf=8') as reservas: 
        for lineas in reservas:
            lineas = lineas.strip().split(';')
            idReservaArchivo = lineas [0]
        
def buscar_Reservacion (id_cliente, fecha):
    with open (ruta_reservas, 'r', encoding='utf-8') as reservas:
        encontrado = False
        for buscar in reservas:
            buscar = buscar.strip().split(';')
            id_reserva_arch = buscar[0]
            id_cliente_arch = [1]
            fecha_arch = [3]
            if id_cliente == id_cliente_arch and fecha == fecha_arch:
                encontrado = True
                break
        if encontrado == True:
            return id_reserva_arch
        if not encontrado:
            return None
        
def validar_id (id_reserva):
    with open (ruta_reservas, 'r', encoding='utf-8') as reservas:
        encontrado = False
        for buscar in reservas:
            buscar = buscar.strip().split(';')
            id_reserva_ar = buscar[0]
            if id_reserva == id_reserva_ar:
                encontrado = True
                break
        if encontrado == True:
            return id_reserva

def checar_reserva(id_reserva):
    with open(ruta_reservas, 'r', encoding='utf-8') as reservas:
        for buscar in reservas:
            buscar = buscar.strip().split(';')
            id_reserva_archivo = buscar [0]
            fecha_archivo = buscar[3]
            hora_inicio_archivo = buscar[4]
            hora_fin_archivo = buscar[5]
            estatus_archivo = buscar[6]
            if id_reserva == id_reserva_archivo:
                return fecha_archivo, hora_inicio_archivo, hora_fin_archivo, estatus_archivo
        else:
            return(None)                
        
def cancelar_reserva(id_reserva):
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