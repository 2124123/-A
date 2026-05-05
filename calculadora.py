import tkinter as tk

# Função para adicionar números/operadores ao visor
def clicar(valor):
    entrada.set(entrada.get() + str(valor))

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.set(resultado)
    except:
        entrada.set("Erro")

# Função para limpar
def limpar():
    entrada.set("")

# Criando janela principal
janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.StringVar()

# Campo de texto
visor = tk.Entry(janela, textvariable=entrada, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
visor.grid(row=0, column=0, columnspan=4)

# Botões
botoes = [
    (7,1,0),(8,1,1),(9,1,2),("/",1,3),
    (4,2,0),(5,2,1),(6,2,2),("*",2,3),
    (1,3,0),(2,3,1),(3,3,2),("-",3,3),
    (0,4,0),(".",4,1),("=",4,2),("+",4,3),
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        botao = tk.Button(janela, text=texto, padx=20, pady=20, command=calcular)
    else:
        botao = tk.Button(janela, text=texto, padx=20, pady=20, command=lambda t=texto: clicar(t))
    botao.grid(row=linha, column=coluna)

# Botão limpar
botao_limpar = tk.Button(janela, text="C", padx=79, pady=20, command=limpar)
botao_limpar.grid(row=5, column=0, columnspan=4)

janela.mainloop()