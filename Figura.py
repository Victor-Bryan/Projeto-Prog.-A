
from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, cor, cor_preench = ''):
        self.cor = cor
        self.cor_preench = cor_preench
    @abstractmethod
    def atualizar(self, x, y):
        pass
    @abstractmethod
    def desenhar(self, canvas):
        pass
    @abstractmethod
    def desenhar_nova(self, canvas):
        pass
    @abstractmethod
    def incompleta(self):
        return False

class Linha(Figura):
    def __init__(self, x1, y1, cor, cor_preench=''):
        super().__init__(cor, cor_preench)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1
        self.y2 = y1
    def atualizar(self, x, y):
        self.x2 = x
        self.y2 = y
    def desenhar(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor)
    def desenhar_nova(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor, dash=(4, 2))
    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2

class Rabisco(Figura):
    def __init__(self, x1, y1, cor):
        super().__init__(cor)
        self.pontos = [(x1, y1)]
    def atualizar(self, x, y):
        self.pontos.append((x, y))
    def desenhar(self, canvas):
        canvas.create_line(self.pontos, fill=self.cor)
    def desenhar_nova(self, canvas):
         canvas.create_line(self.pontos, fill=self.cor, dash=(4, 2))
    def incompleta(self):
        return len(self.pontos) <= 1

class Retangulos(Linha):
    def __init__(self, x1, y1, cor, cor_preench):
        super().__init__(x1, y1, cor, cor_preench)
    def desenhar(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor, fill=self.cor_preench)
    def desenhar_nova(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor, fill=self.cor_preench, dash=(4, 2))

class Ovais(Linha):
    def __init__(self, x1, y1, cor, cor_preench):
        super().__init__(x1, y1, cor, cor_preench)
    def desenhar(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline=self.cor, fill=self.cor_preench)
    def desenhar_nova(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline=self.cor, fill=self.cor_preench, dash=(4, 2))

class Circulos(Ovais):
    def __init__(self, x1, y1, cor, cor_preench):
        super().__init__(x1, y1, cor, cor_preench)
    def atualizar(self, x, y):

        lado = min(abs(x - self.x1), abs(y - self.y1))

        if x >= self.x1:
            self.x2 = self.x1 + lado
        else:
            self.x2 = self.x1 - lado

        if y >= self.y1:
            self.y2 = self.y1 + lado
        else:
            self.y2 = self.y1 - lado

class Triangulo(Linha):
    def __init__(self, x1, y1, cor, cor_preench):
        super().__init__(x1, y1, cor, cor_preench)
    def desenhar(self, canvas):
        x3 = self.x1
        y3 = self.y2
        canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, x3, y3, outline=self.cor, fill=self.cor_preench);
    def desenhar_nova(self, canvas):
        x3 = self.x1
        y3 = self.y2
        canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, x3, y3, outline=self.cor, fill=self.cor_preench, dash=(4, 2))

class Pentagono(Linha):
    def __init__(self, x1, y1, cor, cor_preench):
        super().__init__(x1, y1, cor, cor_preench)

    def desenhar(self, canvas):
        largura = self.x2 - self.x1
        altura = self.y2 - self.y1
        xm = (self.x1 + self.x2) / 2
        canvas.create_polygon( xm, self.y1, self.x2, self.y1 + altura*0.35,self.x2 - largura*0.2, self.y2, self.x1 + largura*0.2, self.y2, self.x1, self.y1 + altura*0.35, outline=self.cor,fill=self.cor_preench0)

    def desenhar_nova(self, canvas):
        largura = self.x2 - self.x1
        altura = self.y2 - self.y1
        xm = (self.x1 + self.x2) / 2
        canvas.create_polygon(xm, self.y1, self.x2, self.y1 + altura*0.35,self.x2 - largura*0.2, self.y2, self.x1 + largura*0.2, self.y2, self.x1, self.y1 + altura*0.35, outline=self.cor,fill=self.cor_preench)