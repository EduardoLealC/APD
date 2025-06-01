from simulador_APD import simular_apd
from interfazEntrada import datosEntrada
from interfazSalida import mostrarResultado

def main():
    # Obtener los datos iniciales una sola vez
    transiciones, estado_inicial, acepta_por, estados_finales, palabra = datosEntrada()

    #Bucle para realizar multiples simulaciones con diferentes palabras
    while True: 
        # Simular con la palabra actual
        resultado = simular_apd(transiciones, estado_inicial, acepta_por, estados_finales, palabra)
        # Mostrar el resultado y obtener una nueva palabra (o None para terminar)
        otraPalabra = mostrarResultado(palabra, resultado, transiciones)
        
        if otraPalabra is None or otraPalabra.strip().lower() == "salir":
            print("Fin de la simulación.")
            break
        else:
            palabra = list(otraPalabra)  # Usar nueva palabra

if __name__ == "__main__":
    main()
