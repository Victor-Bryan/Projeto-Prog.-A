from Modelo import *
from tkinter import filedialog
from Estados import *

class Controlador:
    """
    Classe responsável por controlar a interação entre a View e o Model.

    Gerencia os eventos do mouse para criação de figuras, além das
    operações de salvar e abrir desenhos.
    """
    def __init__(self, view):
        """
        Inicializa o controlador.

        Cria uma instância do modelo, registra os eventos da interface
        gráfica e configura os comandos dos botões.

        @param view: Objeto responsável pela interface gráfica da aplicação.
        """
        self.view = view

        self.model =Model()
        self.figura_nova = None
        self.estados = {
                "Linha": EstadoLinha(),
                "Rabisco": EstadoRabisco(),
                "Retangulos": EstadoRetangulo(),
                "Ovais": EstadoOval(),
                "Circulos": EstadoCirculo(),
                "Triangulo": EstadoTriangulo(),
                "Pentagono": EstadoPentagono()
                }
        self.view.canvas.bind("<ButtonPress-1>", self.iniciar_figura_nova)
        self.view.canvas.bind("<B1-Motion>", self.atualizar_figura_nova)
        self.view.canvas.bind("<ButtonRelease-1>", self.incluir_figura_nova)
        self.view.bt_salvar.config(command=self.salvar)
        self.view.bt_abrir.config(command=self.abrir)
        self.view.bt_limpar.config(command=self.limpar)

    def iniciar_figura_nova(self, event):
        """
       Inicia a criação de uma nova figura.

      Obtém as configurações escolhidas pelo usuário e delega
       a criação da figura ao estado correspondente.

      @param event: Evento do mouse contendo as coordenadas iniciais.
       """
        cor = self.view.cor_borda_var.get()
        preench = self.view.cor_preench_var.get()
        tipo = self.view.tipo_figura_var.get()

        estado = self.estados.get(tipo)

        if estado is not None:
           self.figura_nova = estado.criar_figura(
            event.x,
            event.y,
            cor,
            preench
            )

    def atualizar_figura_nova(self, event):
        """
        Atualiza as dimensões da figura que está sendo desenhada.

        Enquanto o botão do mouse permanece pressionado, atualiza a
        figura e solicita seu redesenho na interface.

        @param event: Evento do mouse contendo as novas coordenadas.
        """
        if self.figura_nova is None:
            return

        self.figura_nova.atualizar(event.x, event.y)

        self.view.redesenhar(self.model, self.figura_nova)

    def incluir_figura_nova(self, event):
        """
        Finaliza a criação da figura.

        Caso a figura seja válida, adiciona-a ao modelo e atualiza a
        interface gráfica.

        @param event: Evento de liberação do botão do mouse.
        """
        if self.figura_nova is None:
            return

        if not self.figura_nova.incompleta():
            self.model.adicionar(self.figura_nova)

        self.figura_nova = None

        self.view.redesenhar(self.model)
    
    def salvar(self):
        """
        Salva o desenho em um arquivo.

        Abre uma caixa de diálogo para que o usuário escolha o local
        onde o desenho será salvo com extensão '.des'.
        """
        arquivo = filedialog.asksaveasfilename(
                  defaultextension=".des",
                  filetypes=[("Arquivos de desenho", "*.des")]
                  )

        if arquivo:
             self.model.salvar(arquivo)
    
    def abrir(self):
        """
        Abre um desenho previamente salvo.

        Exibe uma caixa de diálogo para seleção de um arquivo '.des',
        carrega seu conteúdo no modelo e atualiza a interface gráfica.
        """
        arquivo = filedialog.askopenfilename(
             filetypes=[("Arquivos de desenho", "*.des")]
            )

        if arquivo:
            self.model.abrir(arquivo)
            self.view.redesenhar(self.model)
    
    def limpar(self):
       """
       Remove todas as figuras do desenho.

       Solicita ao modelo que remova todas as figuras e
       atualiza a interface gráfica.

       @return: None.
       @since: 1.0
       """
       self.model.limpar()
       self.figura_nova = None
       self.view.redesenhar(self.model)