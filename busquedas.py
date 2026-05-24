# Este archivo implementa los algoritmos de busqueda para encontrar rutas
# dentro del sistema de transporte Metro de Medellin.
#
# Se implementan 3 estrategias:
#
# 1. Busqueda en Anchura (BFS - Breadth First Search)
#    Explora todas las estaciones a distancia 1, luego a distancia 2, etc.
#    Garantiza encontrar la ruta con MENOS TRANSBORDOS (estaciones).
#    No considera los tiempos de viaje entre estaciones.
#
# 2. Busqueda en Profundidad (DFS - Depth First Search)
#    Explora cada camino hasta el final antes de probar otro.
#    Encuentra UNA ruta posible, no necesariamente la optima.
#    Util para verificar si existe conexion entre dos estaciones.
#
# 3. Busqueda A* (A-Estrella)
#    Combina el costo real acumulado con una heuristica de estimacion.
#    Garantiza encontrar la ruta de MENOR TIEMPO (costo minimo).
#    Es el algoritmo recomendado para este sistema.

from collections import deque
import heapq
from heuristica import heuristica_posicion


# ─────────────────────────────────────────────
# ALGORITMO 1: BUSQUEDA EN ANCHURA (BFS)
# ─────────────────────────────────────────────

def busqueda_anchura(grafo, origen, destino):
    """
    Encuentra la ruta con menor numero de estaciones entre origen y destino.

    Parametros:
        grafo   : diccionario del grafo de transporte {estacion: [(vecino, costo)]}
        origen  : nombre de la estacion de partida
        destino : nombre de la estacion de llegada

    Retorna:
        (ruta, costo_total) si existe camino, o (None, None) si no existe.
    """

    # Cola FIFO: cada elemento es (estacion_actual, camino_recorrido)
    cola = deque()
    cola.append((origen, [origen]))

    # Conjunto de estaciones ya visitadas para no repetir
    visitados = set()
    visitados.add(origen)

    while cola:
        estacion_actual, camino = cola.popleft()

        # Regla: SI llegamos al destino → retornar la ruta encontrada
        if estacion_actual == destino:
            costo_total = calcular_costo_ruta(grafo, camino)
            return camino, costo_total

        # Explorar cada vecino de la estacion actual
        for vecino, _ in grafo.get(estacion_actual, []):
            # Regla: SI el vecino no ha sido visitado → agregarlo a la cola
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = camino + [vecino]
                cola.append((vecino, nuevo_camino))

    # Si la cola se vacio sin encontrar el destino → no hay ruta
    return None, None


# ─────────────────────────────────────────────
# ALGORITMO 2: BUSQUEDA EN PROFUNDIDAD (DFS)
# ─────────────────────────────────────────────

def busqueda_profundidad(grafo, origen, destino):
    """
    Encuentra una ruta posible entre origen y destino explorando en profundidad.

    Parametros:
        grafo   : diccionario del grafo de transporte
        origen  : nombre de la estacion de partida
        destino : nombre de la estacion de llegada

    Retorna:
        (ruta, costo_total) si existe camino, o (None, None) si no existe.
    """

    # Pila LIFO: cada elemento es (estacion_actual, camino_recorrido)
    pila = [(origen, [origen])]

    # Conjunto de estaciones ya visitadas
    visitados = set()
    visitados.add(origen)

    while pila:
        estacion_actual, camino = pila.pop()

        # Regla: SI llegamos al destino → retornar la ruta encontrada
        if estacion_actual == destino:
            costo_total = calcular_costo_ruta(grafo, camino)
            return camino, costo_total

        # Explorar cada vecino (en orden inverso para mantener orden natural)
        for vecino, _ in reversed(grafo.get(estacion_actual, [])):
            # Regla: SI el vecino no ha sido visitado → agregar a la pila
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = camino + [vecino]
                pila.append((vecino, nuevo_camino))

    # Si la pila se vacio sin encontrar el destino → no hay ruta
    return None, None


# ─────────────────────────────────────────────
# ALGORITMO 3: BUSQUEDA A* (A-ESTRELLA)
# ─────────────────────────────────────────────

def busqueda_astar(grafo, origen, destino):
    """
    Encuentra la ruta de MENOR COSTO (tiempo) entre origen y destino.

    Usa una cola de prioridad ordenada por f(n) = g(n) + h(n), donde:
        g(n) = costo real acumulado desde el origen hasta n
        h(n) = estimacion heuristica del costo restante hasta el destino

    Parametros:
        grafo   : diccionario del grafo de transporte
        origen  : nombre de la estacion de partida
        destino : nombre de la estacion de llegada

    Retorna:
        (ruta, costo_total) si existe camino, o (None, None) si no existe.
    """

    # Cola de prioridad: (f_total, g_real, estacion_actual, camino)
    h_inicial = heuristica_posicion(origen, destino)
    cola = [(h_inicial, 0, origen, [origen])]

    # Diccionario para registrar el menor costo conocido a cada estacion
    costo_minimo = {origen: 0}

    while cola:
        f_total, g_real, estacion_actual, camino = heapq.heappop(cola)

        # Regla: SI llegamos al destino → esta es la ruta optima
        if estacion_actual == destino:
            return camino, g_real

        # Explorar cada vecino de la estacion actual
        for vecino, costo_arista in grafo.get(estacion_actual, []):
            nuevo_g = g_real + costo_arista

            # Regla: SI encontramos un camino mas corto al vecino → actualizar
            if vecino not in costo_minimo or nuevo_g < costo_minimo[vecino]:
                costo_minimo[vecino] = nuevo_g
                h = heuristica_posicion(vecino, destino)
                nuevo_f = nuevo_g + h
                nuevo_camino = camino + [vecino]
                heapq.heappush(cola, (nuevo_f, nuevo_g, vecino, nuevo_camino))

    # Si la cola se vacio → no existe ruta
    return None, None


# ─────────────────────────────────────────────
# FUNCION AUXILIAR: CALCULAR COSTO DE UNA RUTA
# ─────────────────────────────────────────────

def calcular_costo_ruta(grafo, ruta):
    """
    Calcula el costo total (en minutos) de recorrer una ruta dada.

    Parametros:
        grafo : diccionario del grafo de transporte
        ruta  : lista de estaciones en orden de recorrido

    Retorna:
        costo total en minutos (entero), o 0 si la ruta tiene 1 sola estacion.
    """
    costo_total = 0

    for i in range(len(ruta) - 1):
        origen_tramo  = ruta[i]
        destino_tramo = ruta[i + 1]

        # Buscar el costo de este tramo en el grafo
        costo_tramo = None
        for vecino, costo in grafo.get(origen_tramo, []):
            if vecino == destino_tramo:
                costo_tramo = costo
                break

        # Regla: SI el tramo existe en el grafo → sumar su costo
        if costo_tramo is not None:
            costo_total += costo_tramo

    return costo_total
    
