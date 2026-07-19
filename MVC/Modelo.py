"""
Módulo Modelo.

Este módulo contém a implementação do modelo da aplicação,
incluindo as classes que representam as figuras geométricas
e a classe responsável por armazená-las e realizar a persistência.

@author: Victor Bryan
@author: José Alberto
@version: 1.0
"""
from abc import ABC, abstractmethod
import pickle


class Model:
    """
    Model da aplicação.

    Responsável por armazenar todas as figuras do desenho
    e realizar as operações de persistência.

    @version: 1.0
    @since: 1.0
    """

    def __init__(self):
        """
         Inicializa o model.

         Cria uma lista vazia para armazenar as figuras.

         @return: None.
         @since: 1.0
        """

        self.figuras = []

    def adicionar(self, figura):
        """
        Adiciona a figura ao model.

        @param figura: Objeto da classe Figura que será armazenado.
        @return: None.
        @since: 1.0
        """

        self.figuras.append(figura)

    def listar(self):
        """
        Retorna todas as figuras armazenadas.

        @return: Lista contendo todas as figuras do desenho.
        @since: 1.0
        """
        return self.figuras
    
    def salvar(self, nome_arquivo):
        """
        Salva todas as figuras do desenho em um arquivo.

        Utiliza o módulo pickle para serializar a lista de figuras,
        permitindo que o desenho seja recuperado posteriormente.

       @param nome_arquivo: Caminho do arquivo onde o desenho será salvo.
       @return: None.
       @throws OSError: Caso ocorra erro durante a criação ou escrita do arquivo.
       @since: 1.0
       """
        with open(nome_arquivo, "wb") as arquivo:
            pickle.dump(self.figuras, arquivo)

    def abrir(self, nome_arquivo):
        """
        Carrega um desenho salvo anteriormente.

        Lê um arquivo serializado com o módulo pickle e restaura
        a lista de figuras armazenada no modelo.

        @param nome_arquivo: Caminho do arquivo que será aberto.
        @return: None.
        @throws FileNotFoundError: Caso o arquivo informado não exista.
        @throws OSError: Caso ocorra erro durante a leitura do arquivo.
        @throws pickle.UnpicklingError: Caso o conteúdo do arquivo seja inválido ou esteja corrompido.
        @since: 1.0
        """
        with open(nome_arquivo, "rb") as arquivo:
            self.figuras = pickle.load(arquivo)
    
    def limpar(self):
      """
      Remove todas as figuras armazenadas no modelo.
 
      Esvazia a lista de figuras, deixando o desenho em branco.

      @return: None.
      @since: 1.0
    """
      self.figuras.clear()

class Figura(ABC):
    """
    Classe abstrata que representa uma figura geométrica.

    Todas as figuras do sistema herdam desta classe e implementam
    seus métodos abstratos.

    @version: 1.0
    @since: 1.0
    """
    def __init__(self, cor, cor_preench = ''):
        """
        Inicializa uma figura.

        @param cor: Cor da borda da figura.
        @param cor_preench: Cor de preenchimento da figura.
        @return: None.
        @since: 1.0
        """
        self.cor = cor
        self.cor_preench = cor_preench
    @abstractmethod
    def atualizar(self, x, y):
        """
        Atualiza as dimensões da figura.

        @param x: Coordenada X.
        @param y: Coordenada Y.
        @return: None.
        """
        pass
    @abstractmethod
    def desenhar(self, canvas):
        """
        Desenha a figura no canvas.

        @param canvas: Área de desenho.
        @return: None.
        """
        pass
    @abstractmethod
    def desenhar_nova(self, canvas):
        """
        Desenha uma pré-visualização da figura.

        @param canvas: Área de desenho.
        @return: None.
        """
        pass
    @abstractmethod
    def incompleta(self):
        """
        Verifica se a figura está incompleta.

        @return: True se estiver incompleta, False caso contrário.
        """
        return False

class Linha(Figura):
    """
    Representa uma linha.

    Permite criar, atualizar e desenhar uma linha.

    @version: 1.0
    @since: 1.0
    """
    def __init__(self, x1, y1, cor, cor_preench=''):
        """
        Inicializa uma linha.

        @param x1: Coordenada X inicial.
        @param y1: Coordenada Y inicial.
        @param cor: Cor da linha.
        @param cor_preench: Não utilizado.
        @return: None.
        """
        super().__init__(cor, cor_preench)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1
        self.y2 = y1
    def atualizar(self, x, y):
        """
        Atualiza o ponto final da linha.

        @param x: Nova coordenada X.
        @param y: Nova coordenada Y.
        @return: None.
        """
        self.x2 = x
        self.y2 = y
    def desenhar(self, canvas):
        """
        Desenha a linha no canvas.

        @param canvas: Área de desenho.
        @return: None.
        """
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor)
    def desenhar_nova(self, canvas):
        """
        Desenha uma prévia da linha.

        @param canvas: Área de desenho.
        @return: None.
        """
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor, dash=(4, 2))
    def incompleta(self):
        """
        Verifica se a linha possui comprimento.

        @return: True se os pontos inicial e final forem iguais.
        """
        return self.x1 == self.x2 and self.y1 == self.y2

class Rabisco(Figura):
    """
    Representa um rabisco desenhado livremente pelo usuário.

    Permite criar, atualizar e desenhar um Rabisco.

    @version: 1.0
    @since: 1.0
    """
    def __init__(self, x1, y1, cor):
        """
        Inicializa um Rabisco.
        @param pontos: Coordenada X inicial e coordenada Y inicial em uma lista.
        @param cor: Cor da linha.
        @param cor_preench: Não utilizado.
        @return: None.
        """
        super().__init__(cor)
        self.pontos = [(x1, y1)]
    def atualizar(self, x, y):
        """
        Adiciona novos pares de coordenadas a lista pontos

        @param x: Nova coordenada X.
        @param y: Nova coordenada Y.
        @return: None.
        """
        self.pontos.append((x, y))
    def desenhar(self, canvas):
        """
        Desenha o rabisco conectando todos os pontos armazenados.

        @param canvas: Área de desenho.
        @return: None.
        """
        canvas.create_line(self.pontos, fill=self.cor)
    def desenhar_nova(self, canvas):
         """
        Desenha uma prévia do rabisco.

        @param canvas: Área de desenho.
        @return: None.
        """
         canvas.create_line(self.pontos, fill=self.cor, dash=(4, 2))
    def incompleta(self):
        """
        Verifica se o rabisco possui comprimento.

        @return: True se a lista pontos tiver tamanho 1 ou menos.
        """
        return len(self.pontos) <= 1

class Retangulos(Linha):
    """
    Representa um Retangulo.

    Herda da classe Linha e utiliza as coordenadas inicial e final
    para determinar as dimensões do Retangulo desenhado no canvas.

    @version: 1.0
    @since: 1.0
    """
    def __init__(self, x1, y1, cor, cor_preench):
        """
        Inicializa o __init__ de Linha 
        @return: None.
        """
        super().__init__(x1, y1, cor, cor_preench)
    def desenhar(self, canvas):
        """
        Desenha um retangulo no canvas.

        @param canvas: Área de desenho.
        @return: None.
        """
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor, fill=self.cor_preench)
    def desenhar_nova(self, canvas):
        """
        Desenha uma prévia do retangulo.

        @param canvas: Área de desenho.
        @return: None.
        """
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor, fill=self.cor_preench, dash=(4, 2))

class Triangulo(Linha):
    """
    Representa um Triangulo.

    Herda da classe Linha e utiliza as coordenadas inicial e final
    para determinar as dimensões do triangulo desenhado no canvas.

    @version: 1.0
    @since: 1.0
    """
    def __init__(self, x1, y1, cor, cor_preench):
        """
        Inicializa o __init__ de Linha 
        @return: None.
        """
        super().__init__(x1, y1, cor, cor_preench)
    def desenhar(self, canvas):
        """
        Desenha um Triangulo no canvas.

        @param x3 : Novo ponto para forma o Triangulo
        @param y3 : Novo ponto para forma o Triangulo
        @param canvas: Área de desenho.
        @return: None.
        """
        x3 = self.x1
        y3 = self.y2
        canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, x3, y3, outline=self.cor, fill=self.cor_preench)
    def desenhar_nova(self, canvas):
        """
        Desenha uma prévia do triangulo


        @param canvas: Área de desenho.
        @param x3 : Novo ponto para forma o Triangulo
        @param y3 : Novo ponto para forma o Triangulo
        @return: None.
        """
        x3 = self.x1
        y3 = self.y2
        canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, x3, y3, outline=self.cor, fill=self.cor_preench, dash=(4, 2))

class Pentagono(Linha):
    """
    Representa um Pentágono.

    Herda da classe Linha e utiliza as coordenadas inicial e final
    para determinar as dimensões do pentágono desenhado no canvas.

    @version: 1.0
    @since: 1.0
    """

    def __init__(self, x1, y1, cor, cor_preench):
        """
        Inicializa o __init__ de Linha 
        @return: None.
        """
        super().__init__(x1, y1, cor, cor_preench)

    def desenhar(self, canvas):
        """
        Desenha o pentágono no canvas.

        O pentágono é construído a partir das coordenadas inicial
        e final definidas pelo usuário.

        @param canvas: Área de desenho onde o pentágono será exibido.
        @return: None.
        @since: 1.0
        """
        largura = self.x2 - self.x1
        altura = self.y2 - self.y1
        xm = (self.x1 + self.x2) / 2
        canvas.create_polygon( xm, self.y1, self.x2, self.y1 + altura*0.35,self.x2 - largura*0.2, self.y2, self.x1 + largura*0.2, self.y2, self.x1, self.y1 + altura*0.35, outline=self.cor,fill=self.cor_preench)

    def desenhar_nova(self, canvas):
        """
        Desenha uma pré-visualização do pentágono.

        Exibe o pentágono enquanto o usuário ainda está definindo
        suas dimensões.

        @param canvas: Área de desenho onde a pré-visualização será exibida.
        @return: None.
        @since: 1.0
        """
        largura = self.x2 - self.x1
        altura = self.y2 - self.y1
        xm = (self.x1 + self.x2) / 2
        canvas.create_polygon(xm, self.y1, self.x2, self.y1 + altura*0.35,self.x2 - largura*0.2, self.y2, self.x1 + largura*0.2, self.y2, self.x1, self.y1 + altura*0.35, outline=self.cor,fill=self.cor_preench)

class Ovais(Linha):
    """
    Representa uma figura oval.

    Herda da classe Linha e utiliza as coordenadas inicial e final
    para definir as dimensões da oval desenhada no canvas.

    @version: 1.0
    @since: 1.0
    """
    def __init__(self, x1, y1, cor, cor_preench):
        """
        Inicializa o __init__ de Linha 
        @return: None.
        """
        super().__init__(x1, y1, cor, cor_preench)
    def desenhar(self, canvas):
        """
        Desenha a figura oval no canvas.

        Utiliza as coordenadas inicial e final para definir o
        retângulo delimitador da oval.

        @param canvas: Área de desenho onde a oval será exibida.
        @return: None.
        @since: 1.0
        """
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline=self.cor, fill=self.cor_preench)
    def desenhar_nova(self, canvas):
        """
        Desenha uma pré-visualização da figura oval.

        Exibe a oval enquanto o usuário ainda está definindo
        suas dimensões.

        @param canvas: Área de desenho onde a pré-visualização será exibida.
        @return: None.
        @since: 1.0
        """
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline=self.cor, fill=self.cor_preench, dash=(4, 2))

class Circulos(Ovais):
    """
    Representa um círculo.

    Herda da classe Ovais e garante que a largura e a altura
    sejam iguais, mantendo a forma circular independentemente
    do movimento do mouse.

    @version: 1.0
    @since: 1.0
    """
    def __init__(self, x1, y1, cor, cor_preench):
        """
        Inicializa o __init__ de Linha 
        @return: None.
        """
        super().__init__(x1, y1, cor, cor_preench)
    def atualizar(self, x, y):
        """
        Atualiza as dimensões do círculo.

        Calcula um único valor para largura e altura, garantindo
        que o desenho mantenha o formato circular.

        @param x: Nova coordenada X do cursor.
        @param y: Nova coordenada Y do cursor.
        @return: None.
        @since: 1.0
        """

        lado = min(abs(x - self.x1), abs(y - self.y1))

        if x >= self.x1:
            self.x2 = self.x1 + lado
        else:
            self.x2 = self.x1 - lado

        if y >= self.y1:
            self.y2 = self.y1 + lado
        else:
            self.y2 = self.y1 - lado
