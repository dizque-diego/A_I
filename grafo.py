# Este archivo es la base de conocimiento principal del sistema de transporte
# Cada estación es un nodo
# Cada conexion entre estaciones es una arista
# Cada arista tiene un costo, es decir, moverse entre estaciones tiene un costo, será tomado como minutos 
# Para este proyecto se esta trabajando las lineas A, B del metro y la linea K del metro cable
# Por lo tanto hay estaciones que sirven de punto de transferencia entre distintas lineas del metro
# Por ejemplo: San Antonio y Acevedo
# Estas estaciones de trasbordo no tendrian costo, es decir, pasar de San Antonio A para B no generaria costo
# Mismo ocurre entre Estacion Acevedo A y Acevedo Metrocable (K)
# Esto ultimo nos indicará que el costo de movimiento entre estaciones 
# Este costo de movimiento sobre el uso neto del sistema de transporte entre estaciones
# El costo no estima gasto economico ni gasto organico del usuario para moverse.
# Las estaciones de transferencia se visualizarán como un unico nodo.


grafo_transporte = {
    #Linea A del metro
    "Estrella": [("Sabaneta",4)],
    "Sabaneta": [("Estrella",4), ("Itagui",2)], 
    "Itagui": [("Sabaneta",2), ("Envigado",5)],
    "Envigado": [("Itagui",5),("Ayura",7)],
    "Ayura": [("Envigado",7),("Aguacatala",4)],
    "Aguacatala": [("Ayura",4), ("Poblado",5)],
    "Poblado": [("Aguacatala",5), ("Industriales", 6)],
    "Industriales": [("Poblado", 6), ("Exposiciones", 4)],
    "Exposiciones": [("Industriales", 4), ("Alpujarra", 2)],
    "Alpujarra": [("Exposiciones", 2), ("San Antonio", 3)],
    "San Antonio": [("Alpujarra", 3), ("Parque Berrio", 2), ("Cisneros",4)],
    "Parque Berrio": [("San Antonio", 2), ("Prado", 4)],
    "Prado": [("Parque Berrio", 4),("Hospital", 3)],
    "Hospital": [("Prado", 3), ("Universidad", 4)],
    "Universidad": [("Hospital", 4), ("Caribe", 5)],
    "Caribe": [("Universidad", 5), ("Tricentenario", 4)],
    "Tricentenario": [("Caribe", 4), ("Acevedo",3)],
    "Acevedo": [("Tricentenario", 3), ("Madera", 5), ("Andalucia", 6)],
    "Madera": [("Acevedo", 5), ("Bello", 4)],
    "Bello": [("Madera", 4), ("Niquia", 3)],
    "Niquia": [("Bello", 3)],

    #Linea B del metro
    #Estacion San Antonio ya fue realizada
    "Cisneros": [("San Antonio", 4), ("Suramericana", 3)],
    "Suramericana": [("Cisneros", 3), ("Estadio", 1)],
    "Estadio": [("Suramericana", 1), ("Floresta", 3)],
    "Floresta": [("Estadio", 3), ("Santa Lucia", 2)],
    "Santa Lucia": [("Floresta", 2), ("San Javier", 3)],
    "San Javier": [("Santa Lucia", 3)],

    #Linea K Metrocable
    #Acevedo ya fue realizada
    "Andalucia": [("Acevedo", 6), ("Popular", 7)],
    "Popular": [("Andalucia", 7), ("Santo Domingo",8)],
    "Santo Domingo": [("Popular", 8)]
}
Lineas = {
    "Linea A":[
        "Estrella","Sabaneta","Itagui","Envigado","Ayura","Aguacatala","Poblado","Industriales","Exposiciones","Alpujarra",
        "San Antonio","Parque Berrio","Prado","Hospital","Universidad","Caribe","Tricentenario","Acevedo",
        "Madera","Bello","Niquia"
    ],
    "Linea B":[
        "San Antonio","Cisneros","Suramericana","Estadio","Floresta","Santa Lucia","San Javier"],
    "Linea K":[
        "Acevedo", "Andalucia", "Popular", "Santo Domingo"
    ]
}
Estaciones_Transferencia ={
    "San Antonio": ["Linea A", "Linea B"],
    "Acevedo":["Linea A", "Linea K"]
}
def obtener_estaciones():
    return(list(grafo_transporte.keys()))

def obtener_conexiones(estacion):
    return grafo_transporte.get(estacion,[])

def existe_estacion(estacion):
    return estacion in grafo_transporte

def obtener_costo(origen,destino):
    for estacion_vecina, costo in obtener_conexiones(origen):
        if estacion_vecina == destino:
            return costo
    return None

def obtener_lin_estacion(estacion):
    lineas_estacion = []
    for nombre_linea, estaciones in Lineas.items():
        if estacion in estaciones:
            lineas_estacion.append(nombre_linea)

    return lineas_estacion

def es_esta_trans(estacion):
    return estacion in Estaciones_Transferencia
