# Este Archivo contendrá las reglas logicas para consultar la base de conocimiento del sistema de transporte
# Estas reglas permiten validar si:
# Una estacion existe
# Si dos estaciones tienen conexion directa
# Si es posible despalzarse directamente entre dos estaciones
# Si la estacion permite transferencias entre una linea y otra 
from grafo import (
    existe_estacion,
    obtener_conexiones,
    obtener_costo,
    obtener_lin_estacion,
    es_esta_trans
)

#   Una estacion es valida si existe dentro de una base de conocimiento
def estacion_valida(estacion):
    return existe_estacion(estacion)

#   Existe una conexion directa entre dos estaciones si el destino aparece dentro de las conexiones disponibles desde el origen
def conexion_directa(origen,destino):
    conexiones = obtener_conexiones(origen)
    for estacion_vecina, costo in conexiones:
        if estacion_vecina == destino:
            return True
    return False

#   El usuario puede desplazarse desde una estacion origen hacia una estacion destino si ambas estaciones son validas y existe una conexion directa entre ellas
def puede_desplazarse(origen,destino):
    return estacion_valida(origen) and estacion_valida(destino) and conexion_directa(origen,destino)


#   Si eciste una conexion directa entre dos estaciones, se puede consultar el costo asociado a su desplazamiento
def costo_desplazamiento(origen,destino):
    if puede_desplazarse(origen, destino):
        return obtener_costo(origen,destino)
    return None

#   Si una estación existe, de puede consultar a que linea pertenece
def lineas_estacion(estacion):
    if estacion_valida (estacion):
        return obtener_lin_estacion(estacion)
    return []

#    Una estacion permite transferencia si está registrada como estacion de trasnferencia dentro de la base de conocimiento
def permite_transf(estacion):
    return estacion_valida(estacion) and es_esta_trans(estacion)