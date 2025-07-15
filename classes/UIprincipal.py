import tkinter as tk

class UberFront(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Uber - Frontend")
        self.geometry("400x600")  # Tamaño de la ventana
        self.config(bg="#f5f5f5")

        # Crear el 'mapa' (simple color de fondo)
        self.canvas = tk.Canvas(self, bg="lightblue", width=400, height=400)
        self.canvas.pack(pady=10)

        # Título de la aplicación
        self.label = tk.Label(self, text="Bienvenido a Uber", font=("Helvetica", 16), bg="#f5f5f5")
        self.label.pack(pady=20)

        # Botón para solicitar viaje
        self.request_button = tk.Button(self, text="Solicitar Viaje", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=self.request_trip)
        self.request_button.pack(pady=10)

        # Botón para ver historial de viajes
        self.history_button = tk.Button(self, text="Historial de Viajes", font=("Helvetica", 12), bg="#2196F3", fg="white", command=self.view_history)
        self.history_button.pack(pady=10)

    def request_trip(self):
        print("Solicitud de viaje en proceso...")

    def view_history(self):
        print("Mostrando historial de viajes...")

# Iniciar la interfaz
if __name__ == "__main__":
    app = UberFront()
    app.mainloop()