from classes import *   # Import required-Only classes
from time import sleep
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# ------------------ Tu código original ------------------
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

# Main (representa la APP de consola)
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
    print("Información de Solicitud de viaje:")
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
    sleep(5)

    # Chofer acepta el viaje
    chofer.aceptarViaje(viaje)
    print(f"Chofer {chofer.nombre} ha aceptado el viaje.")
    sleep(1)

    print(f"Código de viaje generado: {viaje.codigoViaje}")
    sleep(1)

    # Seguimiento del viaje
    viaje.seguimientoViaje()
    sleep(6)

    print("\nEl chofer ha llegado al punto de encuentro.")
    codigo = ""
    while codigo != viaje.codigoViaje:
        codigo = input("Ingrese el código de viaje para empezar el viaje: ")
        if codigo == viaje.codigoViaje:
            print("Código de viaje confirmado. El viaje ha comenzado.")
            total = viaje.pago.total
            print("\n")
            sleep(8)

            viaje.estadoViaje = EstadoViaje.FINALIZADO
            print("Viaje finalizado")
            sleep(1)

            print(f"Total del viaje: ${total}")
            sleep(1)

            print(f"Estado del viaje: {viaje.estadoViaje.value}")
            sleep(2)

            opcionCalificar = input("Desea calificar el viaje? (s/n): ").lower()
            if opcionCalificar == 's':
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

# Interfaz Tkinter
class UberApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("UberPY")
        self.geometry("500x400")
        self.pasajeros = []
        self.viaje = None
        self.chofer = Chofer(Auto("Toyota", "Corolla"), "Carlos", [ZonaDeTrabajo("Ituzaingó")])
        self.chofer.available = True

        tk.Label(self, text="Nombre del pasajero:").pack(pady=5)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack(pady=5)

        tk.Label(self, text="Destino:").pack(pady=5)
        self.entry_destino = tk.Entry(self)
        self.entry_destino.pack(pady=5)

        tk.Label(self, text="Tipo de viaje:").pack(pady=5)
        self.combo_tipo = ttk.Combobox(self, values=[t.value for t in TipoViaje])
        self.combo_tipo.pack(pady=5)

        tk.Label(self, text="Método de pago:").pack(pady=5)
        self.combo_pago = ttk.Combobox(self, values=[m.value for m in MetodoPago])
        self.combo_pago.pack(pady=5)

        tk.Button(self, text="Solicitar viaje", command=self.solicitar_viaje).pack(pady=15)

        self.lbl_info = tk.Label(self, text="", font=("Arial", 10))
        self.lbl_info.pack(pady=10)

    def solicitar_viaje(self):
        nombre = self.entry_nombre.get().strip()
        destino = self.entry_destino.get().strip()
        tipo_str = self.combo_tipo.get().strip()
        metodo_str = self.combo_pago.get().strip()
        if not (nombre and destino and tipo_str and metodo_str):
            messagebox.showwarning("Error", "Completa todos los campos")
            return

        #Crear pasajero
        pasajero = Pasajero(nombre)
        pasajero.agregarDireccion(Direccion("Los pozos", destino))
        self.pasajeros = [pasajero]

        #Convertir strings a enums
        tipo_viaje = next((t for t in TipoViaje if t.value == tipo_str), None)
        metodo_pago = next((m for m in MetodoPago if m.value == metodo_str), None)

        if tipo_viaje is None or metodo_pago is None:
            messagebox.showerror("Error", "Tipo de viaje o método de pago inválido")
            return

        #Crear el viaje
        inicio = pasajero.direcciones[0]
        fin = Direccion("Destino", destino)
        self.viaje = Viaje(self.pasajeros, inicio, fin, tipo_viaje)

        #Chofer acepta el viaje
        self.chofer.aceptarViaje(self.viaje)
        codigo = self.viaje.codigoViaje
        self.lbl_info.config(text=f"Chofer: {self.chofer.nombre}\nAuto: {self.chofer.auto.marca} {self.chofer.auto.modelo}\nCódigo: {codigo}")

        #Pedir código
        while True:
            codigo_ingresado = simpledialog.askstring("Código de viaje", "Ingrese el código de viaje:")
            if codigo_ingresado is None:
                messagebox.showinfo("Cancelado", "El viaje no pudo comenzar.")
                return
            if codigo_ingresado == codigo:
                break
            else:
                messagebox.showerror("Error", "Código incorrecto. Inténtalo de nuevo.")

        #Viaje confirmado
        total = self.viaje.pago.calcularTotal(len(self.pasajeros))
        self.viaje.estadoViaje = EstadoViaje.FINALIZADO
        messagebox.showinfo("Viaje finalizado", f"Viaje confirmado!\nTotal: ${total}\nEstado: {self.viaje.estadoViaje.value}")

        #Calificación
        if messagebox.askyesno("Calificacion", "Desea calificar el viaje?"):
            while True:
                calif = simpledialog.askinteger("Calificación", "Ingrese calificación (0-5):", minvalue=0, maxvalue=5)
                if calif is not None:
                    self.viaje.calificacion = calif
                    messagebox.showinfo("Gracias", f"Calificación registrada: {self.viaje.calificacion}")
                    break
        else:
            messagebox.showinfo("Fin", "Gracias por usar UberPY")


# Selector de modo
if __name__ == "__main__":
    print("Elige modo de ejecución:")
    print("1. Consola")
    print("2. Interfaz gráfica")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        main() 
    elif opcion == "2":
        app = UberApp()
        app.mainloop()
    else:
        print("Opción inválida")
