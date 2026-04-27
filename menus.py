from clientes import buscarcliente, registrar_cliente, verificar
import reservas
import utils

#FUNCION PARA INICIO DE SESION
def pedir_datos_inicio(id_cliente):
    contador = 0
    while contador < 3: #VALIDAMOS QUE NO SE QUEDE EN BUCLE
        correo = input('Ingresa tu correo: ')
        password = input ('Ingres tu password: ')
        id_cliente = buscarcliente(correo, password)

        if id_cliente:
                return id_cliente
        contador +=1
        print(f'Datos incorrectos, intentos restantes: {3-contador}')
        
    print('Haz agotado todos los intentos') 
    selection = input('El cliente no existe, ¿deseas crearlo?(S/N):').lower().strip() 
    if selection == 's':
            return pedir_datos_registro()
    else:
        print('Volviendo al inicio.')
        return None

#FUNCION PARA REGISTRO 
def pedir_datos_registro(id_cliente):
    while True:
        nombres = input('Ingresa tus nombre/s (si tienes 2): ')
        apellidos = input('Ingresa tus apellidos: ')
        
        if nombres != '' and apellidos != '':
            nombres, apellidos = utils.limpiardatos(nombres, apellidos)
        else:
            print('Los nombres y apellidos no pueden estar vacios intenta de nuevo')
            continue

        telefono = input('Ingresa tu numero de telefono: ')
        correo = input('ingresa tu correo: ')

        if telefono.isdigit() and len(telefono) > 0 and len(telefono) <11: 
            pass
        else:
            print('Ingresa números únicamente, o verifica que no estes dejando espacios en blanco')
            continue
            
        password = input('Ingresa una contraseña que contenga al menos 8 carateres: ')
        p_confirm = input('Ingresa de nuevo la contraseña: ')
        if password == p_confirm:
            print('Contraseña correcta.')
            break
        else:
            print('Las contraseñas no coinciden verifica e intenta de nuevo')
            continue
    id_cliente = verificar(nombres, apellidos, telefono, correo)

    if id_cliente:
        print ('Este cliente ya existe, dirigiendo a la pagina de inicio de sesión')
        id_cliente = pedir_datos_inicio(id_cliente)
        return id_cliente
        
    elif id_cliente == None:
        id_cliente = registrar_cliente (nombres, apellidos, telefono, correo, password)
        return id_cliente

#FUNCION PARA MANEJAR ÚNICAMENTE ID'S DE RESERVAS.
def datos_reserva(id_cliente, fecha):
    while True:
        fecha = input('ingresa la fecha de tu reservación(DD/MM/AAAA): ')
        fecha = validar_fecha(fecha)
        if fecha:
            id_reserva = reservas.buscar_Reservacion(id_cliente, fecha)
            return id_reserva
        else:
            print('No existen datos de reversa con esa fecha.')
            return None