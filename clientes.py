import os 
ruta_base = os.path.dirname(__file__)
ruta_clientes= os.path.join(ruta_base, 'data', 'clientes.txt')

#FUNCION PARA BUSCAR CLIENTES
def buscarcliente(nombres, apellidos, telefono,correo):
    with open(ruta_clientes, 'r', encoding='utf-8') as base_clientes:
        for linea in base_clientes:
            linea = linea.strip().split(';')
            id_archivo = linea[0]
            nombres_archivo = linea[1]
            apellidos_archivo = linea[2]
            telefono_archivo= linea[3]
            correo_archivo = linea[4]   
            if nombres == nombres_archivo and apellidos == apellidos_archivo and telefono == telefono_archivo and correo == correo_archivo:
                return(id_archivo) 
        return None
        
#FUNCION PARA REGISTRAR CLIENTE NUEVO 
def registrar_cliente(nombres, apellidos, telefono,correo):
    with open (ruta_clientes, 'r') as base:
        for indice, lineas in enumerate(base):
            pass
    id = f'CL{indice+1}'
    with open (ruta_clientes, 'a', encoding='utf-8') as base:
        base.write(f'{id};{nombres};{apellidos};{telefono};{correo}\n')
    return(id)
