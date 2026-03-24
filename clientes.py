import os 


#ruta_clientes = r'D:\Lenguajes de Programación\Curso de Programación con Python\Proyecto Integrador\sistema_citas\data\clientes.txt'
ruta_clientes = os.path.abspath('clientes.txt')

print(ruta_clientes)

"""def buscarcliente(nombres, apellidos, telefono,correo):
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
        
def registrar_cliente(nombres, apellidos, telefono,correo):
    with open (ruta_clientes, 'r') as base:
        for indice, lineas in enumerate(base):
            pass
    id = f'CL{indice+1}'
    with open (ruta_clientes, 'a', encoding='utf-8') as base:
        base.write(f'{id};{nombres};{apellidos};{telefono};{correo}\n')
    return(id)"""
