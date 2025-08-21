from classes import *
import time
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# Consola
def run_console():
    chofer = Chofer(Auto("Toyota", "Corolla"), "Carlos", [ZonaDeTrabajo("Ituzaingó")])
    print(f"Creacion de clases")
    print(f"Chofer creado: {chofer.nombre} con auto {chofer.auto.marca} {chofer.auto.modelo}")
    
    print("\nBienvenido a Uber")
    pasajeros = []
    pasajeroPrincipal = Pasajero("Ana")
    pasajeros.append(pasajeroPrincipal)

    print("Solicitando un viaje...")
    origen = "Los pozos"
    print(f"Ubicacion actual: {origen}")
    destino = input("Ingrese el destino del viaje: ")
    direccion = Direccion(origen, destino)
    pasajeroPrincipal.agregarDireccion(direccion)

    print("\nListado de tipos de viaje:")
    listadoTiposViaje = [tipo.value for tipo in EnumTipoViaje.TipoViaje]
    for tipo in listadoTiposViaje:
        print(f"- {tipo}")
    while True:
        try:
            tipoDeViaje = input("Ingrese el tipo de viaje: ").capitalize()
            tipoViaje = TipoViaje(tipoDeViaje)
            if tipoViaje.getTipoViaje() == EnumTipoViaje.TipoViaje.Compartido.value:
                print("Tipo de viaje compartido seleccionado.")
                while True:
                    nombrePasajero = input("Ingrese el nombre del pasajero (o 'salir' para terminar): ")
                    if nombrePasajero.lower() == 'salir':
                        break
                    pasajeros.append(Pasajero(nombrePasajero))
            break
        except ValueError as e:
            print(f"Error: {e}")

    print("\nListado de métodos de pago:")
    listadoMetodosPago = [metodo.value for metodo in EnumMetodoPago.MetodoPago]
    for metodo in listadoMetodosPago:
        print(f"- {metodo}")
    while True:
        try:
            metodoPago = input("Ingrese el método de pago: ").capitalize()
            metodoDePago = MetodoPago(metodoPago)
            break
        except ValueError as e:
            print(f"Error: {e}")

    pago = Pago(metodoDePago, tipoViaje)
    viaje = Viaje(pasajeros, pago)
    print("Buscando choferes disponibles...")
    time.sleep(2)
    chofer.aceptarViaje(viaje)
    viaje.asignarChofer(chofer)
    codigo = viaje.generarCodigoViaje()
    print(f"Código de viaje generado: {codigo}")

    viaje.seguimientoViaje()
    time.sleep(2)
    codigo_ingresado = input("\nIngrese el código de viaje para empezar el viaje: ")
    if codigo_ingresado != viaje.codigoViaje:
        print("Código de viaje incorrecto. El viaje no puede comenzar.")
        return

    print("Código de viaje confirmado. El viaje ha comenzado.")
    time.sleep(2)
    total = viaje.calcularViaje()
    viaje.setEstadoViaje(EstadoPago.PAGADO.value)
    print(f"\nViaje finalizado. Total: ${total} - Estado: {viaje.estadoViaje}")

    opcionCalificar = input("Desea calificar el viaje? (s/n): ").lower()
    if opcionCalificar == "s":
        while True:
            try:
                calificacion = int(input("Ingrese calificación (0-5): "))
                viaje.setCalificacionViaje(calificacion)
                print(f"Calificación registrada: {viaje.calificacion}")
                break
            except ValueError as e:
                print(f"Error: {e}")
    else:
        print("Gracias por usar UberPY. ¡Hasta luego!")


#Tkinter version grafica

class UberApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("UberPY")
        self.geometry("500x400")
        self.pasajeros = []
        self.viaje = None
        self.chofer = Chofer(Auto("Toyota", "Corolla"), "Carlos", [ZonaDeTrabajo("Ituzaingó")])

        tk.Label(self, text="Nombre del pasajero:").pack(pady=5)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack(pady=5)

        tk.Label(self, text="Destino:").pack(pady=5)
        self.entry_destino = tk.Entry(self)
        self.entry_destino.pack(pady=5)

        tk.Label(self, text="Tipo de viaje:").pack(pady=5)
        self.combo_tipo = ttk.Combobox(self, values=[t.value for t in EnumTipoViaje.TipoViaje])
        self.combo_tipo.pack(pady=5)

        tk.Label(self, text="Método de pago:").pack(pady=5)
        self.combo_pago = ttk.Combobox(self, values=[m.value for m in EnumMetodoPago.MetodoPago])
        self.combo_pago.pack(pady=5)

        tk.Button(self, text="Solicitar viaje", command=self.solicitar_viaje).pack(pady=15)

        self.lbl_info = tk.Label(self, text="", font=("Arial", 10))
        self.lbl_info.pack(pady=10)

    def solicitar_viaje(self):
        nombre = self.entry_nombre.get().strip()
        destino = self.entry_destino.get().strip()
        tipo = self.combo_tipo.get()
        metodo = self.combo_pago.get().strip()
        if not (nombre and destino and tipo and metodo):
            messagebox.showwarning("Error", "Completa todos los campos")
            return

        pasajero = Pasajero(nombre)
        pasajero.agregarDireccion(Direccion("Los pozos", destino))
        self.pasajeros = [pasajero]

        tipo_viaje = TipoViaje(tipo)
        metodo_pago = MetodoPago(metodo)
        pago = Pago(metodo_pago, tipo_viaje)

        self.viaje = Viaje(self.pasajeros, pago)
        self.chofer.aceptarViaje(self.viaje)
        self.viaje.asignarChofer(self.chofer)
        codigo = self.viaje.generarCodigoViaje()

        self.lbl_info.config(text=f"Chofer: {self.chofer.nombre}\nAuto: {self.chofer.auto.marca} {self.chofer.auto.modelo}\nCódigo: {codigo}")

        # Pedir código
        codigo_ingresado = simpledialog.askstring("Código de viaje", "Ingrese el código de viaje:")
        if codigo_ingresado != self.viaje.codigoViaje:
            messagebox.showerror("Error", "Código de viaje incorrecto. La aplicación se cerrará.")
            self.destroy()
            return

        # Viaje confirmado
        total = self.viaje.calcularViaje()
        self.viaje.setEstadoViaje(EstadoPago.PAGADO.value)
        messagebox.showinfo("Viaje finalizado", f"Viaje confirmado!\nTotal: ${total}\nEstado: {self.viaje.estadoViaje}")

        # Calificación
        opcion = messagebox.askyesno("Calificación", "Desea calificar el viaje?")
        if opcion:
            while True:
                calif = simpledialog.askinteger("Calificación", "Ingrese calificación (0-5):", minvalue=0, maxvalue=5)
                if calif is not None:
                    self.viaje.setCalificacionViaje(calif)
                    messagebox.showinfo("Gracias", f"Calificación registrada: {self.viaje.calificacion}")
                    break
        else:
            messagebox.showinfo("Fin", "Gracias por usar Uber")

# Selector de modo
if __name__ == "__main__":
    print("Elige modo de ejecución:")
    print("1. Consola")
    print("2. Interfaz gráfica")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        run_console()
    elif opcion == "2":
        app = UberApp()
        app.mainloop()
    else:
        print("Opción inválida")
