import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter import messagebox

janela= tk.Tk()
janela.title("formulario")

#entrada texto
label_entrada=ttk.Label(janela,text= "nome")
label_entrada.pack()
entrada=tk.Entry(janela)
entrada.pack()

#checkbox(campo marcar opçao)

checkbox = tk.IntVar()
chech =tk.Checkbutton(janela,text="aceito os termos",variable=checkbox)
chech.pack()

#opçoes
opçao= tk.IntVar()

opc1=tk.Radiobutton(janela,text="masculino",variable=opçao,value=1)
opc2=tk.Radiobutton(janela,text="feminino",variable=opçao,value=2)
opc3=tk.Radiobutton(janela,text="outro",variable=opçao,value=3)
opc1.pack()
opc2.pack()
opc3.pack()

#list box(lista)
lista=tk.Listbox(janela)
lista.insert(1, "python")
lista.insert(2, "java")
lista.insert(3, "php")
lista.insert(4, "c++")
lista.pack()

#combobox

combo = ttk.Combobox(janela,values=["MG","RJ","RS","RN"])
combo.set("Selecione um Estado")
combo.pack()

#botao
def clicar():
    messagebox.showinfo("aviso","botao acionado")
btn= tk.Button(janela,text= "mostrar mensagem",command=clicar)
btn.pack()






















janela.mainloop()
