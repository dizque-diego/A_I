# Sistema Inteligente de Ruteo - Metro de Medellin
# Materia: Inteligencia Artificial
#
# Este archivo es el punto de entrada del sistema.
# Integra la base de conocimiento (grafo.py), las reglas logicas (reglas.py)
# y los algoritmos de busqueda (busquedas.py) para encontrar la mejor ruta
# entre dos estaciones del metro de Medellin.
#
# El sistema implementa 3 algoritmos:
#   - BFS  : Ruta con menos estaciones
#   - DFS  : Primera ruta posible encontrada
#   - A*   : Ruta de menor tiempo (RECOMENDADA)

from grafo import grafo_transporte, obtener_estaciones
from reglas import (
    estacion_valida,
    conexion_directa,
    puede_desplazarse,
    costo_desplazamiento,
    lineas_estacion,
    permite_transf,
)
from busquedas import busqueda_anchura, busqueda_profundidad, busqueda_astar


# ─────────────────────────────────────────────
# FUNCIONES DE PRESENTACION
# ─────────────────────────────────────────────

def mostrar_encabezado():
    print("=" * 60)
    print("   SISTEMA INTELIGENTE DE RUTEO — METRO DE MEDELLIN")
    print("   Lineas: A | B | Metrocable K")
    print("=" * 60)

def mostrar_estaciones():
    estaciones = obtener_estaciones()
    print("\nEstaciones disponibles:")
    print("-" * 60)
    for i, est in enumerate(estaciones):
        lineas = lineas_estacion(est)
        transf = " [TRANSFERENCIA]" if permite_transf(est) else ""
        print(f"  {est:<22} {' | '.join(lineas)}{transf}")
    print("-" * 60)

def mostrar_ruta(nombre_algoritmo, ruta, costo):
    if ruta:
        print(f"\n  [{nombre_algoritmo}]")
        print(f"  Ruta: {' → '.join(ruta)}")
        print(f"  Estaciones recorridas: {len(ruta)}")
        print(f"  Tiempo estimado: {costo} minutos")
    else:
        print(f"\n  [{nombre_algoritmo}] No se encontro ruta.")

def mostrar_comparacion(ruta_bfs, costo_bfs, ruta_dfs, costo_dfs, ruta_astar, costo_astar):
    print("\n" + "=" * 60)
    print("  COMPARACION DE ALGORITMOS")
    print("=" * 60)
    mostrar_ruta("BFS  — Menos estaciones",    ruta_bfs,   costo_bfs)
    mostrar_ruta("DFS  — Primera ruta posible", ruta_dfs,   costo_dfs)
    mostrar_ruta("A*   — Menor tiempo (OPTIMA)",ruta_astar, costo_astar)
    print("\n" + "=" * 60)

    # Determinar y resaltar la mejor ruta
    if ruta_astar:
        print("  ★ RUTA RECOMENDADA (A*):")
        print(f"  {' → '.join(ruta_astar)}")
        print(f"  Tiempo total: {costo_astar} minutos")
    print("=" * 60)


# ─────────────────────────────────────────────
# PRUEBAS INICIALES DE REGLAS LOGICAS
# (conservadas del trabajo original de Diego)
# ─────────────────────────────────────────────

def prueba_estacion(estacion):
    print(f"\nEstacion consultada: {estacion}")
    print(f"  ¿Existe en el sistema?      {estacion_valida(estacion)}")
    print(f"  Lineas disponibles:         {lineas_estacion(estacion)}")
    print(f"  ¿Permite transferencia?     {permite_transf(estacion)}")

def prueba_conexion(origen, destino):
    print(f"\nConexion: {origen} → {destino}")
    print(f"  ¿Conexion directa?          {conexion_directa(origen, destino)}")
    print(f"  ¿Puede desplazarse?         {puede_desplazarse(origen, destino)}")
    print(f"  Costo del tramo:            {costo_desplazamiento(origen, destino)} minutos")

def ejecutar_pruebas_reglas():
    print("\n" + "=" * 60)
    print("  PRUEBAS DE REGLAS LOGICAS Y BASE DE CONOCIMIENTO")
    print("=" * 60)
    prueba_estacion("San Antonio")
    prueba_estacion("Acevedo")
    prueba_estacion("Poblado")
    prueba_conexion("San Antonio", "Cisneros")
    prueba_conexion("Acevedo", "Andalucia")
    prueba_conexion("Poblado", "Envigado")
    print()


# ─────────────────────────────────────────────
# FUNCION PRINCIPAL: BUSQUEDA DE RUTA
# ─────────────────────────────────────────────

def buscar_ruta_interactiva():
    mostrar_estaciones()

    print("\nIngrese las estaciones para calcular la ruta optima.")
    print("(Escriba el nombre exactamente como aparece en la lista)\n")

    origen  = input("  Estacion de ORIGEN:  ").strip()
    destino = input("  Estacion de DESTINO: ").strip()

    print()

    # Validar que ambas estaciones existen
    if not estacion_valida(origen):
        print(f"  ERROR: La estacion '{origen}' no existe en el sistema.")
        return

    if not estacion_valida(destino):
        print(f"  ERROR: La estacion '{destino}' no existe en el sistema.")
        return

    # Caso especial: origen igual a destino
    if origen == destino:
        print(f"  Ya se encuentra en la estacion '{origen}'. No necesita moverse.")
        return

    print(f"  Calculando rutas de '{origen}' a '{destino}'...")

    # Ejecutar los 3 algoritmos
    ruta_bfs,   costo_bfs   = busqueda_anchura(grafo_transporte, origen, destino)
    ruta_dfs,   costo_dfs   = busqueda_profundidad(grafo_transporte, origen, destino)
    ruta_astar, costo_astar = busqueda_astar(grafo_transporte, origen, destino)

    # Mostrar comparacion completa
    mostrar_comparacion(ruta_bfs, costo_bfs, ruta_dfs, costo_dfs, ruta_astar, costo_astar)


# ─────────────────────────────────────────────
# MENU PRINCIPAL
# ─────────────────────────────────────────────

def menu():
    mostrar_encabezado()

    while True:
        print("\n  ¿Que desea hacer?")
        print("  1. Buscar ruta entre dos estaciones")
        print("  2. Ver pruebas de reglas logicas")
        print("  3. Salir")

        opcion = input("\n  Seleccione una opcion (1/2/3): ").strip()

        if opcion == "1":
            buscar_ruta_interactiva()
        elif opcion == "2":
            ejecutar_pruebas_reglas()
        elif opcion == "3":
            print("\n  Hasta luego.\n")
            break
        else:
            print("  Opcion no valida. Intente de nuevo.")


# ─────────────────────────────────────────────
# PUNTO DE ENTRADA
# ─────────────────────────────────────────────

if __name__ == "__main__":
    menu()
