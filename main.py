import tkinter as tk
import json

class main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        f2 = GradientFrame(self, "blue", "purple", borderwidth=1, relief="sunken", width=1024, height=600)
        f2.pack(side="bottom", fill="both", expand=True)

        w = tk.Label(self, text="App", relief="raised")
        w.place(relx=0.5, rely=0.3, anchor="center")
        w.config(bg="#6495ED", highlightbackground="#581845", highlightcolor="#581845", font=("Times", 20, "italic bold"))

        button = tk.Button(self, text="Ing. en Computación", command=lambda: self.open_new_window("Ing. en Computación"))
        button.place(relx=0.3, rely=0.5, anchor="center")
        button.config(bg="#6495ED", highlightbackground="#581845", highlightcolor="#581845", font=("Times", 20, "italic bold"))

        button2 = tk.Button(self, text="Ing. Electrónica", command=lambda: self.open_new_window("Ing. Electrónica"))
        button2.place(relx=0.7, rely=0.5, anchor="center")
        button2.config(bg="#6495ED", highlightbackground="#581845", highlightcolor="#581845", font=("Times", 20, "italic bold"))

    def open_new_window(self, program):
        new_window = tk.Toplevel(self)
        new_window.title(program)

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

class GradientFrame(tk.Canvas):
    def __init__(self, parent, color1="red", color2="black", **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = height
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(0, i, width, i, tags=("gradient",), fill=color)
        self.lower("gradient")

if __name__ == "__main__":
    root = tk.Tk()
    main(root).pack(fill="both", expand=True)
    root.mainloop()
