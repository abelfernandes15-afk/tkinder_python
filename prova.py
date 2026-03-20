import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter import messagebox

janela= tk.Tk()
janela.title("acesso")
janela.configure(background="blue")


tk.Label(janela,text="FORMULARIO DE CADRASTRO",font=("arial",15)).grid(column=1,pady=20)
tk.Label(janela, text="nome:").grid(row=1, column=0)
entrada_nome=tk.Entry(janela, width=30,font=("Arial",14))
entrada_nome.grid(row=1,column=1)

tk.Label(janela,text="FORMULARIO DE CADRASTRO",font=("arial",15)).grid(column=1,pady=20)
tk.Label(janela, text="senha").grid(row=2, column=0)
entrada_senha=tk.Entry(janela, width=30,font=("Arial",14))
entrada_senha.grid(row=2,column=1)

def enviar():
   nome = entrada_nome.get()
   senha = entrada_senha.get()

entrar = f"nome{entrada_nome}{entrada_senha}"
messagebox.showinfo('dados enviados',entrar)

tk.Button(janela,text="usuario logado com sucesso",command=enviar).grid(row=10,column=1,pady=20)

imagem=tk.PhotoImage(file="tigre.png")
imagem=imagem.subsample(3,3)
tk.Label(janela,image=imagem).place(x=450,y=10)


























janela.mainloop()