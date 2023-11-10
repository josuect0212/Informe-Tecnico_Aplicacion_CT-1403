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
        self.boton1 = tk.Button(self.canvas_fondo, text="Ing. Electrónica", font=("Noto Serif", 14), fg='white', bg='#004AAD', command=lambda: self.open_new_window("Ing. Electrónica"))
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
        # Cargar los datos del archivo JSON
        with open('program_data.json', 'r', encoding='utf-8') as json_file:
            datos_carreras = json.load(json_file)

        new_window = tk.Toplevel(self.ventana)
        new_window.title(program)
        new_window.geometry('900x550')

        new_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(new_window))

        # Crea al canvas de fondo
        self.canvas_fondo = tk.Canvas(new_window, bg='white', bd=2, highlightthickness=2, highlightbackground='white', width=10000, height=2000)
        self.canvas_fondo.pack(fill='both', expand=True)
        self.canvas_fondo.place(x=-10, y=90)
        self.canvas_fondo.configure(bg="white")
        # Crea el canvas superior
        self.canvas = tk.Canvas(new_window, bg='#004AAD', bd=2, highlightthickness=2, highlightbackground="#004AAD", width=10000, height=130)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.place(x=0, y=0)  # Cambia las coordenadas x e y según tus necesidades
        self.canvas.configure(bg='#004AAD')

        # Crear una lista de control de variables para los cursos
        curso_vars = []
        
        # Crear una función para actualizar el nivel de dificultad
        def actualizar_nivel_dificultad():
            total_creditos = 0
            nivel_dificultad = 0
            cantidad_cursos = 0  # Contador de cursos seleccionados
            for i, curso_var in enumerate(curso_vars):
                if curso_var.get() == 1:
                    curso = datos_carreras[program]['cursos'][i]
                    total_creditos += curso['creditos']
                    nivel_dificultad += curso['creditos'] * curso['nivel_dificultad']
                    cantidad_cursos += 1
            
            nivel_semestre = (nivel_dificultad / total_creditos) * cantidad_cursos if total_creditos > 0 else 0
            if nivel_semestre < 10.5:
                dificultad = "Dificultad baja"
            elif 10.5 <= nivel_semestre < 16.5:
                dificultad = "Dificultad moderada"
            else:
                dificultad = "Dificultad alta"
            nivel_dificultad_label.config(text=f"Nivel de Dificultad del Semestre: {dificultad}")
            cantidad_creditos_label.config(text=f"Cantidad total de créditos: {total_creditos:.2f}")
        x= 270
        y= 120
        # Crear checkboxes para seleccionar cursos
        for i, curso in enumerate(datos_carreras[program]['cursos']):
            y += 20
            curso_var = tk.IntVar(value=0)
            curso_vars.append(curso_var)
            curso_checkbox = tk.Checkbutton(new_window, text=curso['nombre'], variable=curso_var, command=actualizar_nivel_dificultad, font=("telegraf", 12))
            curso_checkbox.place(x=x, y=y)

        nivel_dificultad_label = tk.Label(new_window, text="Nivel de Dificultad del Semestre: 0.00", font=("telegraf", 12)) 
        nivel_dificultad_label.grid(row=len(datos_carreras[program]['cursos']), column=10, columnspan=80, padx=300, pady=20)

        cantidad_creditos_label = tk.Label(new_window, text="Cantidad total de créditos: 0.00", font=("telegraf", 12))
        cantidad_creditos_label.grid(row=len(datos_carreras[program]['cursos'])+1, column=10, columnspan=80, padx=300, pady=30)


ventana = tk.Tk()
ventana.geometry('900x550')
mi_interfaz = MiInterfaz(ventana)
ventana.mainloop()