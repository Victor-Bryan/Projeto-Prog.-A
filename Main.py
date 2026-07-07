from Figura import (Linha, Rabisco, Retangulos, Triangulo, Ovais, Circulos, Pentagono)
from tkinter import *
from tkinter import ttk


def iniciar_figura_nova(event):
    global figura_nova
    cor = cor_borda_var.get()
    preench = cor_preench_var.get()
    if tipo_figura_var.get() == "Linha":
        figura_nova = Linha(event.x, event.y, cor)
    elif tipo_figura_var.get() == "Rabisco":
        figura_nova = Rabisco(event.x, event.y, cor)
    elif tipo_figura_var.get() == "Retangulos":
        figura_nova = Retangulos(event.x, event.y, cor, preench)
    elif tipo_figura_var.get() == 'Triangulo':
        figura_nova = Triangulo(event.x, event.y, cor, preench)
    elif tipo_figura_var.get() == "Ovais":
        figura_nova = Ovais(event.x, event.y, cor, preench)
    elif tipo_figura_var.get() == 'Pentagono':
        figura_nova = Pentagono(event.x, event.y, cor, preench)
    else:
        figura_nova = Circulos(event.x, event.y, cor, preench)
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova is None:
        return
    figura_nova.atualizar(event.x, event.y)
    desenhar_figuras()
    figura_nova.desenhar_nova(canvas)
def incluir_figura_nova(event):
    global figura_nova
    if figura_nova is None:
        return
    if not figura_nova.incompleta():
        figuras.append(figura_nova)
    figura_nova = None
    desenhar_figuras()
def desenhar_figuras():
    canvas.delete("all")
    for figura in figuras:
        figura.desenhar(canvas)
    if figura_nova is not None:
        figura_nova.desenhar_nova(canvas)
    
figuras = []      
figura_nova = None 

root = Tk()
root.title('Exemplo de aplicação')
frame = Frame(root)

paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame,  text='Escolha a forma do desenho:')
label.grid(column=0, row=0, sticky=W, **paddings)
label_cor = ttk.Label(frame, text='Cor da borda:')
label_cor.grid(column=0, row=1, sticky=W, **paddings)
label_preenchi = ttk.Label(frame, text='Cor de Preenchimento:')
label_preenchi.grid(column=0, row=2, sticky=W, **paddings)

tipo_figura_var = StringVar(root) 
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco','Retangulos', 'Ovais', 'Circulos', 'Triangulo', 'Pentagono')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

cor_borda_var = StringVar(root)
option_cor = ttk.OptionMenu(
    frame,
    cor_borda_var,
    'black',
    'black',
    'white',
    'red',
    'blue',
    'green',
    'orange',
    'yellow',
    'purple',
    'pink'
)
option_cor.grid(column=1, row=1, sticky=W, **paddings)

cor_preench_var = StringVar(root)

option_corP = ttk.OptionMenu(
    frame,
    cor_preench_var,
    '',
    '',
    'black',
    'white',
    'red',
    'blue',
    'green',
    'orange',
    'yellow',
    'purple',
    'pink'
)
option_corP.grid(column=1, row=2, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=3, columnspan=2, sticky=W, **paddings)

frame.pack()

canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
