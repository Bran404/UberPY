from classes import *   # Import required-Only classes
from time import sleep
# Resources initialization
print("Inicialización del programa...")
input("Presione enter para continuar...")
sleep(2)

#Creacion de chofer
chofer = Chofer(Auto("Toyota", "Corolla"), "Carlos", [ZonaDeTrabajo("Ituzaingó")])
chofer.available = True
print(f"Chofer creado: {chofer.nombre} con auto {chofer.auto.marca} {chofer.auto.modelo} y zona de trabajo {chofer.zonasDeTrabajo[0].codigo}")
    
# Creación de pasajeros
pasajeros: list[Pasajero] = []
    
# Carga de pasajero principal
pasajeroPrincipal = Pasajero("Ana")
pasajeros.append(pasajeroPrincipal)
pasajeroPrincipal.agregarDireccion(Direccion("Avenida Siempreviva",742))

print("iniciando main...")
input("Presione enter para continuar...")
sleep(3)


# Main (represents APP)
def main():
    print("Solicitando un viaje...")
    sleep(1)

    print("Formulario de viaje")
    sleep(1)

    print("rellenado del formulario...")
    sleep(5)

    #Se obtiene la ubicación actual del usuario
    inicio=pasajeros[0].direcciones[0]
    print(f"Ubicación actual: {inicio.calle} {inicio.altura}")
    sleep(1)

    calle="Autopista Nuncamuerta"
    altura=368
    fin=Direccion(calle,altura)
    print(f"Solicitado destino: {calle} {altura}")
    sleep(2)

    tipoViaje=TipoViaje.INDIVIDUAL
    print(f"Seleccionado un viaje {tipoViaje.value}")
    sleep(1)

    print("Procesando solicitud de viaje...")
    sleep(0.5)
    print("Información de Solicitud de viaje:") # Valida datos del viaje(sin instancia de viaje aun)
    sleep(0.5)
    print(f"Pasajero: {pasajeros[0].nombre}")
    sleep(0.5)
    print(f"Ruta de viaje:[",f"  Origen: {inicio.calle} {inicio.altura}",f"  Destino: {fin.calle} {fin.altura}","]", sep="\n")
    sleep(0.5)
    print(f"Tipo de viaje seleccionado: {tipoViaje.value}")
    sleep(0.5)
    print(f"Método de pago (Obtenido de la configuración del usuario): {pasajeros[0].metodoDePago.value}")
    input("Presione enter para continuar...")
    print("\n")
    sleep(0.5)


    # Crea el viaje - Pasajero confirma el viaje
    viaje = Viaje(pasajeros,inicio,fin,tipoViaje)
    print("Buscando choferes disponibles...")
    sleep(5)  # Simula la búsqueda de choferes

    # Chofer acepta el viaje
    chofer.aceptarViaje(viaje)
    print(f"Chofer {chofer.nombre} ha aceptado el viaje.")
    sleep(1)

    print(f"Código de viaje generado: {viaje.codigoViaje}") # Vista del pasajero
    sleep(1)

    # Seguimiento del viaje
    viaje.seguimientoViaje()

    sleep(6) # Simula el tiempo de chofer a pasajero

    print("\nEl chofer ha llegado al punto de encuentro.")
    codigo = ""
    while codigo != viaje.codigoViaje:
        codigo = input("Ingrese el código de viaje para empezar el viaje: ") # Vista del chofer 
        if codigo == viaje.codigoViaje:
            print("Código de viaje confirmado. El viaje ha comenzado.")
            total = viaje.pago.total
            print("\n")
            sleep(8) # Simula el tiempo del viaje
            # Calcular el total del viaje
            
            viaje.estadoViaje = EstadoViaje.FINALIZADO
            print("Viaje finalizado")
            sleep(1)

            print(f"Total del viaje: ${total}") #Este dato también se guarda en viaje.pago.subtotal, esto es por demo
            sleep(1)

            print(f"Estado del viaje: {viaje.estadoViaje.value}") # Vista del pasajero
            sleep(2)

            opcionCalificar = input("Desea calificar el viaje? (s/n): ").lower() # Vista del pasajero
            if opcionCalificar == 's':
                # Calificación del viaje
                while True:
                    try:
                        calificacion = input("Ingrese la calificación del viaje (0 a 5): ")
                        viaje.calificacion = int(calificacion)
                        print(f"Calificación del viaje: {viaje.calificacion}")
                        print("Gracias por calificar el viaje.")
                        break
                    except ValueError as e:
                        print(f"Error: {e}")
            else:
                print("Gracias por usar UberPY. ¡Hasta luego!")
        else:
            print("Código de viaje incorrecto. El viaje no puede comenzar.")

# Execution
if __name__ == '__main__':
    main()