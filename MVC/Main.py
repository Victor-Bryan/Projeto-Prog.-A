"""
Módulo principal da aplicação.

Este módulo é responsável por inicializar a interface gráfica (View),
criar o controlador que conecta a View ao Model e iniciar o loop
principal da aplicação.
"""

from Visao import View
from Controlador import Controlador

janela = View()

controlador = Controlador(janela)

janela.iniciar()