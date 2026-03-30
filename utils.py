import unicodedata
import datetime

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