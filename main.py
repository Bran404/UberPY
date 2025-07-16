from classes import *   # Import required-Only classes
import time
# Resources initialization
pass

# Main (represents APP)
def main():
    #Creacion de chofer
    chofer = Chofer(Auto("Toyota", "Corolla"), "Carlos", [ZonaDeTrabajo("Ituzaingó")])
    print(f"Creacion de clases")
    print(f"Chofer creado: {chofer.nombre} con auto {chofer.auto.marca} {chofer.auto.modelo}")
    
    print("\nBienvenido a UberPY") # Ejemplo solicitar un viaje
    # Creación de pasajeros
    pasajeros = []
    
    # Carga de pasajero principal
    pasajeroPrincipal = Pasajero("Ana")
    pasajeros.append(pasajeroPrincipal)

    print("Solicitando un viaje...")
    print("Formulario de viaje")
    #Selecciona un destino
    print("\nSeleccion de destino:")
    # Ejemplo de ubicacion actual GPS
    origen = "Los pozos"
    print(f"Ubicacion actual: {origen}")
    destino = input("Ingrese el destino del viaje: ")
    direccion = Direccion(origen, destino)
    pasajeroPrincipal.agregarDireccion(direccion)
    
    # Selecciona el tipo de viaje
    print("\nSeleccion de tipo de viaje:")
    print("Listado de tipos de viaje:")
    listadoTiposViaje = [tipo.value for tipo in EnumTipoViaje.TipoViaje] #Carga de tipos de viaje
    for tipo in listadoTiposViaje:
        print(f"- {tipo}")

    while True:
        try:
            tipoDeViaje = input("Ingrese el tipo de viaje: ").capitalize()
            tipoViaje = TipoViaje(tipoDeViaje)
            if tipoViaje.getTipoViaje() == EnumTipoViaje.TipoViaje.Compartido.value:
                print("Tipo de viaje compartido seleccionado.")
                #Ingresa los otros pasajeros
                while True:
                    nombrePasajero = input("Ingrese el nombre del pasajero (o 'salir' para terminar): ")
                    if nombrePasajero.lower() == 'salir':
                        break
                    nuevoPasajero = Pasajero(nombrePasajero)
                    pasajeros.append(nuevoPasajero)

            break
        except ValueError as e:
            print(f"Error: {e}")

    print("Informacion de Solicitud de viaje:")#Valida datos del viaje(sin instancia de viaje aun)
    print(f"Pasajero: {pasajeroPrincipal.getNombre()}")
    print(f"Pasajeros adicionales: {len(pasajeros) - 1}")
    print(f"Ruta de viaje: \nOrigen: {direccion.getOrigen()}\nDestino: {direccion.getDestino()}")
    print(f"Tipo de viaje seleccionado: {tipoViaje.getTipoViaje()}")

    # Selecciona el metodo de pago
    print("\nSeleccion de metodo de pago:")
    print("Listado de métodos de pago:")
    listadoMetodosPago = [metodo.value for metodo in EnumMetodoPago.MetodoPago]  # Carga de métodos de pago
    for metodo in listadoMetodosPago:
        print(f"- {metodo}")
    while True:
        try:
            metodoPago = input("Ingrese el método de pago: ").capitalize()
            metodoDePago = MetodoPago(metodoPago)
            break
        except ValueError as e:
            print(f"Error: {e}")

    print("\n")
    # Crea el pago - Procesa Pago
    pago = Pago(metodoDePago, tipoViaje)

    # Crea el viaje - Pasajero confirma el viaje
    viaje = Viaje(pasajeros, pago)
    print("Buscando choferes disponibles...")

    time.sleep(3)  # Simula la búsqueda de choferes

    # Chofer acepta el viaje
    chofer.aceptarViaje(viaje)
    print(f"Chofer {chofer.nombre} ha aceptado el viaje.")

    # APP asigna chofer al viaje
    viaje.asignarChofer(chofer)
    
    viaje.generarCodigoViaje()
    print(f"Código de viaje generado: {viaje.codigoViaje}") # Vista del pasajero

    # Seguimiento del viaje
    viaje.seguimientoViaje()

    time.sleep(6) # Simula el tiempo de chofer a pasajero

    print("\nEl chofer ha llegado al punto de encuentro.")
    codigo = input("Ingrese el código de viaje para empezar el viaje: ") # Vista del chofer 
    if codigo == viaje.codigoViaje:
        print("Código de viaje confirmado. El viaje ha comenzado.")
        time.sleep(4) # Simula el tiempo del viaje
        # Calcular el total del viaje
        total = viaje.calcularViaje()
        
        print("\n")
        print("Viaje finalizado")
        print(f"Total del viaje: ${total}")
        viaje.setEstadoViaje(EstadoPago.PAGADO.value)  # Cambia el estado del viaje a PAGADO
        print(f"Estado del viaje: {viaje.estadoViaje}") # Vista del pasajero
        opcionCalificar = input("Desea calificar el viaje? (s/n): ").lower() # Vista del pasajero
        if opcionCalificar == 's':
            # Calificación del viaje
            while True:
                try:
                    calificacion = input("Ingrese la calificación del viaje (0 a 5): ")
                    viaje.setCalificacionViaje(int(calificacion))
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