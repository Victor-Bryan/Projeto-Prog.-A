"""
Módulo responsável pela implementação do padrão State.

Este módulo contém a classe abstrata Estado e as classes
concretas responsáveis pela criação das figuras do sistema.
Seu objetivo é eliminar estruturas condicionais no controlador,
delegando a criação de cada figura ao estado correspondente.

@author: Victor Bryan
@author: José Alberto
@version: 1.0
@since: 1.0
"""
from abc import ABC, abstractmethod
from Modelo import *

class Estado(ABC):
    """
    Classe abstrata que representa um estado de criação de figuras.

    Define a interface utilizada por todos os estados concretos,
    responsáveis por criar diferentes tipos de figuras.

    """

    @abstractmethod
    def criar_figura(self, x, y, cor, preench):
        """
        Cria uma figura geométrica.

        @param x: Coordenada X inicial.
        @param y: Coordenada Y inicial.
        @param cor: Cor da borda da figura.
        @param preench: Cor de preenchimento da figura.
        @return: Objeto da classe Figura.
        @since: 1.0
        """
        pass

class EstadoLinha(Estado):
    def criar_figura(self, x, y, cor, preench):
        return Linha(x, y, cor)

class EstadoRabisco(Estado):
    def criar_figura(self, x, y, cor, preench):
        return Rabisco(x, y, cor)

class EstadoRetangulo(Estado):
    def criar_figura(self, x, y, cor, preench):
        return Retangulos(x, y, cor, preench)

class EstadoOval(Estado):
    def criar_figura(self, x, y, cor, preench):
        return Ovais(x, y, cor, preench)

class EstadoCirculo(Estado):
    def criar_figura(self, x, y, cor, preench):
        return Circulos(x, y, cor, preench)

class EstadoTriangulo(Estado):
    def criar_figura(self, x, y, cor, preench):
        return Triangulo(x, y, cor, preench)

class EstadoPentagono(Estado):
    def criar_figura(self, x, y, cor, preench):
        return Pentagono(x, y, cor, preench)