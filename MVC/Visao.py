from tkinter import *
from tkinter import ttk

class View:
    """
    Representa a interface gráfica da aplicação.

    É responsável por criar a janela principal, os componentes
    gráficos (botões, menus e canvas) e exibir as figuras
    armazenadas no modelo.

    @author: Victor Bryan
    @author: José Alberto
    @version: 1.0
    """
    def __init__(self):
        """
        Inicializa a interface gráfica.

        Cria a janela principal da aplicação, os menus para seleção
        do tipo de figura, cores da borda e preenchimento, os botões
        para salvar e abrir desenhos e o canvas utilizado para desenhar.

        @return: None.
        @since: 1.0
        """
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
        self.bt_salvar = ttk.Button(self.frame, text="Salvar")
        self.bt_salvar.grid(row=0, column=2)
        self.bt_abrir = ttk.Button(self.frame, text="Abrir")
        self.bt_abrir.grid(row=1, column=2)
        ttk.OptionMenu(self.frame, self.tipo_figura_var, "Linha", "Linha", "Rabisco", "Retangulos","Ovais", "Circulos", "Triangulo", "Pentagono" ).grid(row=0, column=1, sticky=W, **paddings)

        ttk.OptionMenu( self.frame, self.cor_borda_var, "black", "black", "white", "red", "blue","green", "orange", "yellow", "purple","pink" ).grid(row=1, column=1, sticky=W, **paddings)

        ttk.OptionMenu(self.frame, self.cor_preench_var, "", "", "black", "white", "red", "blue","green", "orange", "yellow", "purple", "pink" ).grid(row=2, column=1, sticky=W, **paddings)

        self.canvas = Canvas( self.frame, width=600, height=600, bg="white")

        self.canvas.grid(row=3, column=0, columnspan=2, **paddings)

    def redesenhar(self, model, figura_nova=None):
        """
        Atualiza o conteúdo do canvas.

        Remove todos os desenhos atuais e desenha novamente as figuras
        armazenadas no modelo. Caso exista uma figura em construção,
        ela é exibida como uma pré-visualização.

        @param model: Modelo que contém a lista de figuras.
        @param figura_nova: Figura em construção que será exibida como pré-visualização. Pode ser None.
        @return: None.
        @since: 1.0
        """
        self.canvas.delete("all")

        for figura in model.listar():
            figura.desenhar(self.canvas)

        if figura_nova is not None:
            figura_nova.desenhar_nova(self.canvas)

    def iniciar(self):
        """
        Inicia a execução da interface gráfica.

        Executa o laço principal (mainloop) do Tkinter,
        permitindo a interação do usuário com a aplicação.

        @return: None.
        @since: 1.0
        """
        self.root.mainloop()