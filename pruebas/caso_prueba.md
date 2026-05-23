Este archivo contiene los casos de prueba propuestos para dar el funcionamiento de los algoritmos de busqueda

Los algoritmos deben calcular una ruta entre una estación origen, una estación destino, evidenciando la ruta encontrada y el costo total de tomar dicha ruta

# Caso 1
Origen: San Antonio
Destino: Cisneros

El objetivo es validar una conexion directa entre la linea A y B del metro
    Se espera encontrar una conexión directa con un costo estimado de 4

# Caso 2
Origen: Acevedo
Destino: Andalucia

El objetivo es validar conexión y transferencia entre la linea A y K del metro
    Se espera encontrar una conexión directa con un costo de 6

# Caso 3 
Origen: Poblado
Destino: Envigado

El objetivo es validar una ruta que no tiene conexiones directas, es decir requiere pasar por estaciones intermedias dentro de la linea
    Ruta esperada:
    Poblado - Aguacatala - Ayura - Envigado

# Caso 4 
Origen: San Javier
Destino: Santo Domingo

Validar una ruta extensa que requiere dos transferencias de linea, de la Linea B a la A y de la Linea A a la linea K.
    Ruta esperada:
    San Javier - Santa Lucia - Floresta - Estadio - Suramericana - Cisneros - San Antonio - Parque Berrio - Prado - Hospital - Universidad - 
    Caribe - Tricentenario - Acevedo - Andalucia - Popular - Santo Domingo

