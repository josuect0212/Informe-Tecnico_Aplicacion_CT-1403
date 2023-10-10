import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        f2 = GradientFrame(self, "blue", "purple", borderwidth=1, relief="sunken", width=1024, height=600)
        f2.pack(side="bottom", fill="both", expand=True)

        w = tk.Label(self, text="Test", relief="raised")
        w.place(relx=0.5, rely=0.4, anchor="center")

        button = tk.Button(self, text="Ing. en Computación", command=self.on_button_click)
        button.place(relx=0.4, rely=0.5, anchor="center")

        button2 = tk.Button(self, text="Ing. Electrónica", command=self.on_button_click)
        button2.place(relx=0.6, rely=0.5, anchor="center")
        
    def on_button_click(self):
        print("Test")

class GradientFrame(tk.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
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
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(0, i, width, i, tags=("gradient",), fill=color)
        self.lower("gradient")

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
