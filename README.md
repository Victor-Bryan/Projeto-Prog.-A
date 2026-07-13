# Documentação do Sistema – Editor de Desenhos

# Nome da equipe
  Equipe G2

# Integrantes
- JOSÉ ALBERTO CAMPOS GÓIS
- VICTOR BRYAN ALVES SANTOS

# Breve descrição do sistema

O sistema é um editor gráfico desenvolvido em Python utilizando a biblioteca Tkinter e o padrão de arquitetura MVC (Model-View-Controller). Ele permite ao usuário desenhar diferentes figuras geométricas, como linhas, rabiscos, retângulos, ovais, círculos, triângulos e pentágonos, escolhendo as cores da borda e do preenchimento. Além disso, oferece funcionalidades para salvar e abrir desenhos por meio de arquivos com extensão `.des`.

## Quantidade de classes documentadas

Foram documentadas **12 classes**:

1. Controlador
2. View
3. Model
4. Figura
5. Linha
6. Rabisco
7. Retangulos
8. Ovais
9. Circulos
10. Triangulo
11. Pentagono
12. (Módulo Main documentado como módulo, não como classe)

## Quantidade de métodos documentados

Foram documentados **29 métodos**:

### Controlador (6)
- `__init__()`
- `iniciar_figura_nova()`
- `atualizar_figura_nova()`
- `incluir_figura_nova()`
- `salvar()`
- `abrir()`

### View (3)
- `__init__()`
- `redesenhar()`
- `iniciar()`

### Model (5)
- `__init__()`
- `adicionar()`
- `listar()`
- `salvar()`
- `abrir()`

### Figura (5)
- `__init__()`
- `atualizar()`
- `desenhar()`
- `desenhar_nova()`
- `incompleta()`

### Linha (5)
- `__init__()`
- `atualizar()`
- `desenhar()`
- `desenhar_nova()`
- `incompleta()`

### Rabisco (5)
- `__init__()`
- `atualizar()`
- `desenhar()`
- `desenhar_nova()`
- `incompleta()`

### Retangulos (3)
- `__init__()`
- `desenhar()`
- `desenhar_nova()`

### Triangulo (3)
- `__init__()`
- `desenhar()`
- `desenhar_nova()`

### Pentagono (3)
- `__init__()`
- `desenhar()`
- `desenhar_nova()`

### Ovais (3)
- `__init__()`
- `desenhar()`
- `desenhar_nova()`

### Circulos (2)
- `__init__()`
- `atualizar()`