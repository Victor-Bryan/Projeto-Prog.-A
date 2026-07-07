from Modelo import *

class Controlador:

    def __init__(self, view):
        self.view = view

        self.model =Model()
        self.figura_nova = None

        self.view.canvas.bind("<ButtonPress-1>", self.iniciar_figura_nova)
        self.view.canvas.bind("<B1-Motion>", self.atualizar_figura_nova)
        self.view.canvas.bind("<ButtonRelease-1>", self.incluir_figura_nova)

    def iniciar_figura_nova(self, event):

        cor = self.view.cor_borda_var.get()
        preench = self.view.cor_preench_var.get()
        tipo = self.view.tipo_figura_var.get()

        if tipo == "Linha":
            self.figura_nova = Linha(event.x, event.y, cor)

        elif tipo == "Rabisco":
            self.figura_nova = Rabisco(event.x, event.y, cor)

        elif tipo == "Retangulos":
            self.figura_nova = Retangulos(event.x, event.y, cor, preench)

        elif tipo == "Ovais":
            self.figura_nova = Ovais(event.x, event.y, cor, preench)

        elif tipo == "Circulos":
            self.figura_nova = Circulos(event.x, event.y, cor, preench)

        elif tipo == "Triangulo":
            self.figura_nova = Triangulo(event.x, event.y, cor, preench)

        elif tipo == "Pentagono":
            self.figura_nova = Pentagono(event.x, event.y, cor, preench)

    def atualizar_figura_nova(self, event):

        if self.figura_nova is None:
            return

        self.figura_nova.atualizar(event.x, event.y)

        self.view.redesenhar(self.model, self.figura_nova)

    def incluir_figura_nova(self, event):

        if self.figura_nova is None:
            return

        if not self.figura_nova.incompleta():
            self.model.adicionar(self.figura_nova)

        self.figura_nova = None

        self.view.redesenhar(self.model)