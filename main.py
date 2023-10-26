import tkinter as tk
import json
class MiInterfaz(tk.Frame):
    def __init__(self, ventana):
        # Crea la ventana principal
        self.ventana = ventana
        self.ventana.title("CalculaTEC")

        # Crea al canvas de fondo
        self.canvas_fondo = tk.Canvas(self.ventana, bg='white', bd=2, highlightthickness=2, highlightbackground='white', width=10000, height=2000)
        self.canvas_fondo.pack(fill='both', expand=True)
        self.canvas_fondo.place(x=-10, y=90)
        self.canvas_fondo.configure(bg="white")
        # Crea los botones para seleccionar la carrera.
        self.boton1 = tk.Button(self.canvas_fondo, text="Ing. Electronica", font=("Noto Serif", 14), fg='white', bg='#004AAD', command=lambda: self.open_new_window("Ing. Electrónica"))
        self.boton1.configure(width=17, height=2)
        self.boton2 = tk.Button(self.canvas_fondo, text="Ing. Computación", font=("Noto Serif", 14), fg='white', bg="#004AAD", command=lambda: self.open_new_window("Ing. en Computación"))
        self.boton2.configure(width=17, height=2)
        # Inserta los botones en el canvas de fondo
        self.canvas_fondo.create_window(200, 300, window=self.boton1)
        self.canvas_fondo.create_window(700, 300, window=self.boton2)
        # Crea el canvas superior
        self.canvas = tk.Canvas(self.ventana, bg='#004AAD', bd=2, highlightthickness=2, highlightbackground="#004AAD", width=10000, height=130)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.place(x=0, y=0)  # Cambia las coordenadas x e y según tus necesidades
        self.canvas.configure(bg='#004AAD')
        # Agrega el título "CalculaTec" al canvas azul
        self.canvas_fondo.create_text(450, 70, text="Seleccione su carrera:", font=("telegraf", 15), fill="black")
        self.canvas.create_text(450, 65, text="CalculaTec", font=("Noto Serif", 40), fill="white")
    def on_closing(self, ventana):
        ventana.destroy()
        self.ventana.deiconify()
    def open_new_window(self, program):
        new_window = tk.Toplevel(self.ventana)
        new_window.title(program)
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(new_window))
        with open('program_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        if program == "Ing. en Computación":
            program = "Ingeniería en Computación"
        if program == "Ing. Electrónica":
            program = "Ingeniería Electrónica"
        if program in data:
            cursos = data[program]
            self.mostrar_plan_de_estudios(new_window, cursos)
        else:
            cursos = data["Ingeniería en Computación"]
            self.mostrar_plan_de_estudios(new_window, cursos)
    def mostrar_plan_de_estudios(self, window, cursos):
        canvas = tk.Canvas(window)
        canvas.pack(side="top", fill="both", expand=True)
        scrollbar = tk.Scrollbar(window, orient="horizontal", command=canvas.xview)
        scrollbar.pack(side="bottom", fill="x")
        canvas.configure(xscrollcommand=scrollbar.set)
        interior = tk.Frame(canvas)
        canvas.create_window((0, 0), window=interior, anchor="nw")
        for bloque, cursos_bloque in cursos.items():
            bloque_frame = tk.Frame(interior)
            bloque_frame.pack(side="left", padx=10)
            label_bloque = tk.Label(bloque_frame, text=f"{bloque}:")
            label_bloque.pack()
            for curso in cursos_bloque:
                curso_button = tk.Button(bloque_frame, text=curso, command=lambda c=curso: self.mostrar_informacion_curso(c))
                curso_button.pack()

        interior.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

ventana = tk.Tk()
ventana.geometry('900x550')
mi_interfaz = MiInterfaz(ventana)
ventana.mainloop()