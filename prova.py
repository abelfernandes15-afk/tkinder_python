import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

janela = tk.Tk()
janela.title("FORMULARIO") 
#janela.geometry("400x400")
janela.configure(background="white")


tk.Label(janela, text="USUARIO", font=("arial", 15)).grid(row=1, column=0)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=1, column=1)

tk.Label(janela, text="SENHA", font=("arial", 15)).grid(row=2, column=0)
entrada_senha = tk.Entry(janela)
entrada_senha.grid(row=2, column=1)

def enviar():
    nome = "\n bem vindo"

    enviar= f'Douglas:{nome}'
    messagebox.showinfo('{douglas}bem vindo ao sistema',enviar)




tk.Button(janela, text="enviar", font=("arial", 16), command=enviar).grid(row=3, column=1, pady=20)

imagem=tk.PhotoImage(file="tigre.png")
label_imagem=tk.Label(janela,image=imagem)
label_imagem.place(x=600,y=10)






















janela.mainloop()