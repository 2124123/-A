import tkinter as tk
from tkinter import messagebox

# Janela
janela = tk.Tk()
janela.configure(bg="#ffd6e7")
janela.geometry("600x400")
janela.title("Dia das Mães")

# Texto
texto = tk.Label(
    janela,
    text="Mãe, resgate seu presente 🎁",
    font=("Arial", 20, "bold"),
    bg="#ffd6e7",
    fg="#7a284b"
)

texto.pack(pady=40)

# Função do botão
def resgatar():
    messagebox.showinfo(
        "Resgatado!",
        "Eu sabia que você preferia o meu abraço!\n"
        "Feliz Dia das Mães! Te amo ❤️"
    )

# Botão
btn_presente = tk.Button(
    janela,
    text="Lavo a louça por 1 semana",
    font=("Arial", 12),
    command=resgatar
)

btn_presente.pack(pady=10)

# Mudar texto ao passar mouse
def mudar_texto(event):
    btn_presente.config(text="Um beijo e abraço 💖")

# Voltar texto original
def voltar_texto(event):
    btn_presente.config(text="Lavo a louça por 1 semana")

btn_presente.bind("<Enter>", mudar_texto)
btn_presente.bind("<Leave>", voltar_texto)

# Executar
janela.mainloop()