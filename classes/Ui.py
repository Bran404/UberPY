# UI.py
import tkinter as tk
from tkinter import messagebox, ttk
from classes import *

class UberApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("UberPY")
        self.geometry("500x400")

        # Objetos del sistema
        self.pasajeros = []
        self.viaje = None
        self.chofer = Chofer(Auto("Toyota", "Corolla"), "Carlos", [ZonaDeTrabajo("Ituzaingó")])

        # --- Widgets ---
        tk.Label(self, text="Nombre del pasajero:").pack(pady=5)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack(pady=5)

        tk.Label(self, text="Origen:").pack(pady=5)
        self.entry_origen = tk.Entry(self)
        self.entry_origen.insert(0, "Los pozos")
        self.entry_origen.pack(pady=5)

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

        # Botón confirmar código (aparece después)
        self.btn_confirmar = tk.Button(self, text="Confirmar viaje", command=self.confirmar_viaje)
        self.entry_codigo = tk.Entry(self)

    def solicitar_viaje(self):
        nombre = self.entry_nombre.get().strip()
        origen = self.entry_origen.get().strip()
        destino = self.entry_destino.get().strip()
        tipo = self.combo_tipo.get()
        metodo = self.combo_pago.get()

        if not (nombre and destino and tipo and metodo):
            messagebox.showwarning("Error", "Completa todos los campos")
            return

        pasajero = Pasajero(nombre)
        pasajero.agregarDireccion(Direccion(origen, destino))
        self.pasajeros = [pasajero]

        tipo_viaje = TipoViaje(tipo)
        metodo_pago = MetodoPago(metodo)
        pago = Pago(metodo_pago, tipo_viaje)

        self.viaje = Viaje(self.pasajeros, pago)
        self.chofer.aceptarViaje(self.viaje)
        self.viaje.asignarChofer(self.chofer)
        codigo = self.viaje.generarCodigoViaje()

        self.lbl_info.config(
            text=f"Chofer asignado: {self.chofer.nombre}\n"
                 f"Auto: {self.chofer.auto.marca} {self.chofer.auto.modelo}\n"
                 f"Código de viaje: {codigo}\n"
        )

        # Mostrar campo para confirmar código
        self.entry_codigo.pack(pady=5)
        self.btn_confirmar.pack(pady=5)

    def confirmar_viaje(self):
        codigo_ingresado = self.entry_codigo.get().strip()
        if codigo_ingresado != self.viaje.codigoViaje:
            messagebox.showerror("Error", "Código incorrecto, no se puede iniciar el viaje.")
            return

        total = self.viaje.calcularViaje()
        self.viaje.setEstadoViaje(EstadoPago.PAGADO.value)

        messagebox.showinfo("Viaje finalizado",
            f"Total: ${total}\nEstado: {self.viaje.estadoViaje}"
        )

        # Preguntar calificación
        calif = tk.simpledialog.askinteger("Calificación", "Ingrese una calificación (0-5):", minvalue=0, maxvalue=5)
        if calif is not None:
            self.viaje.setCalificacionViaje(calif)
            messagebox.showinfo("Gracias", f"Calificación registrada: {self.viaje.calificacion}")

        self.destroy()  # cerrar app al terminar


def run_ui():
    app = UberApp()
    app.mainloop()
