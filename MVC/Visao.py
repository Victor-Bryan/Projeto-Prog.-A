from tkinter import *
from tkinter import ttk

class View:

    def __init__(self):

        self.root = Tk()
        self.root.title("Editor de Desenhos")

        self.frame = Frame(self.root)
        self.frame.pack()

        paddings = {'padx': 5, 'pady': 5}

        ttk.Label(self.frame, text="Escolha a forma:" ).grid(row=0, column=0, sticky=W, **paddings,)
        ttk.Label(self.frame, text="Cor da borda:" ).grid(row=1, column=0, sticky=W, **paddings)
        ttk.Label(self.frame, text="Cor de preenchimento:").grid(row=2, column=0, sticky=W, **paddings)

        self.tipo_figura_var = StringVar(value="Linha")
        self.cor_borda_var = StringVar(value="black")
        self.cor_preench_var = StringVar(value="")

        ttk.OptionMenu(self.frame, self.tipo_figura_var, "Linha", "Linha", "Rabisco", "Retangulos","Ovais", "Circulos", "Triangulo", "Pentagono" ).grid(row=0, column=1, sticky=W, **paddings)

        ttk.OptionMenu( self.frame, self.cor_borda_var, "black", "black", "white", "red", "blue","green", "orange", "yellow", "purple","pink" ).grid(row=1, column=1, sticky=W, **paddings)

        ttk.OptionMenu(self.frame, self.cor_preench_var, "", "", "black", "white", "red", "blue","green", "orange", "yellow", "purple", "pink" ).grid(row=2, column=1, sticky=W, **paddings)

        self.canvas = Canvas( self.frame, width=600, height=600, bg="white")

        self.canvas.grid(row=3, column=0, columnspan=2, **paddings)
    
    def redesenhar(self, model, figura_nova=None):

        self.canvas.delete("all")

        for figura in model.listar():
            figura.desenhar(self.canvas)

        if figura_nova is not None:
            figura_nova.desenhar_nova(self.canvas)

    def iniciar(self):
        self.root.mainloop()        