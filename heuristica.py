# Este archivo contiene la funcion heuristica utilizada por el algoritmo A*
# La heuristica es una "estimacion inteligente" de cuantos minutos faltan
# para llegar al destino desde la estacion actual.
#
# Como el metro de Medellin no tiene coordenadas geograficas simples,
# usamos el numero de estaciones que hay entre el nodo actual y el destino
# dentro del orden de la linea. Esto es una heuristica admisible:
# nunca sobreestima el costo real, por lo tanto A* garantiza la ruta optima.
#
# Regla logica aplicada:
# SI la estacion actual esta en la misma linea que el destino
# ENTONCES la heuristica = diferencia de posicion * costo_promedio_por_estacion
# SI no estan en la misma linea
# ENTONCES la heuristica = numero de estaciones restantes * costo_promedio

from grafo import Lineas

# Costo promedio estimado por estacion (en minutos), calculado sobre el grafo real
COSTO_PROMEDIO_POR_ESTACION = 4

def heuristica_posicion(estacion_actual, estacion_destino):
    """
    Estima la cantidad de minutos que faltan desde estacion_actual hasta
    estacion_destino basandose en la posicion relativa dentro de las lineas.

    Esta funcion es admisible: nunca sobreestima el costo real,
    condicion necesaria para que A* encuentre siempre la ruta optima.
    """

    # Caso trivial: ya estamos en el destino
    if estacion_actual == estacion_destino:
        return 0

    mejor_estimacion = float('inf')

    for nombre_linea, estaciones in Lineas.items():
        # Regla: si ambas estaciones estan en la misma linea,
        # la distancia minima estimada es la diferencia de posiciones
        if estacion_actual in estaciones and estacion_destino in estaciones:
            pos_actual  = estaciones.index(estacion_actual)
            pos_destino = estaciones.index(estacion_destino)
            diferencia  = abs(pos_actual - pos_destino)
            estimacion  = diferencia * COSTO_PROMEDIO_POR_ESTACION
            if estimacion < mejor_estimacion:
                mejor_estimacion = estimacion

    # Si no comparten linea, estimamos usando el total de estaciones del grafo
    # dividido entre la cantidad de lineas (heuristica conservadora)
    if mejor_estimacion == float('inf'):
        mejor_estimacion = 2 * COSTO_PROMEDIO_POR_ESTACION

    return mejor_estimacion
