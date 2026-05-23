from reglas import(
    estacion_valida,
    conexion_directa,
    puede_desplazarse,
    costo_desplazamiento,
    lineas_estacion,
    permite_transf,
)

def prueba_estacion(estacion):
    print(f"Estacion consultada: {estacion}")
    print(f"¿Existe la estacion {estacion} en el sistema?: {estacion_valida(estacion)}")
    print(f"Lineas disponibles: {lineas_estacion(estacion)}")
    print(f"¿La estacion permite transferencia? {permite_transf(estacion)}")


def prueba_conexion(origen,destino):
    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print(f"¿Existe una conexión directa? {conexion_directa(origen,destino)}")
    print(f"¿Puede desplazarse directamente?: {puede_desplazarse(origen,destino)}")
    print(f"El costo de desplazamiento es {costo_desplazamiento(origen, destino)}")


def main():
    print("sistema de ruteo inteligente IA Chatgpt10Claude15")
    print("---------------------------------------------------")
    print("pruebas iniciales de reglas logicas y base de conocimiento")
    
    prueba_estacion("San Antonio")
    prueba_estacion("Acevedo")
    prueba_estacion("Poblado")

    prueba_conexion("San Antonio","Cisneros")
    prueba_conexion("Acevedo","Andalucia")
    prueba_conexion("Poblado","Envigado")
if __name__== "__main__":
    main()