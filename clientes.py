import os 
ruta_base = os.path.dirname(__file__)
ruta_clientes= os.path.join(ruta_base, 'data', 'clientes.txt')

#FUNCION PARA BUSCAR CLIENTES
def buscarcliente(correo, password):
    with open(ruta_clientes, 'r', encoding='utf-8') as base_clientes:
        for linea in base_clientes:
            linea = linea.strip().split(';')
            id_cliente = linea[0]
            correo_archivo = linea[4]   
            password_archivo = linea[5] 
            if correo == correo_archivo and password == password_archivo:
                return id_cliente
        return None
        
#FUNCION PARA REGISTRAR CLIENTE NUEVO 
def registrar_cliente(nombres, apellidos, telefono,correo, password):
    with open (ruta_clientes, 'r') as base:
        for indice, lineas in enumerate(base):
            pass
    id = f'CL{indice+1}'
    with open (ruta_clientes, 'a', encoding='utf-8') as base:
        base.write(f'{id};{nombres};{apellidos};{telefono};{correo};{password}\n')
    return id

#FUNCION PARA VALIDAR QUE EL CLIENTE NO EXISTA
def verificar (nombres, apellidos, telefono,correo):
    with open (ruta_clientes, 'r') as base:
        for cliente in base:
            cliente = cliente.strip().split(';')
            id_cliente = cliente [0]
            n_archivo = cliente [1]
            a_archivo = cliente [2]
            t_archivo = cliente [3]
            c_archivo = cliente [4]
            if nombres == n_archivo and apellidos == a_archivo and telefono == t_archivo and correo == c_archivo:
                return id_cliente
        return None