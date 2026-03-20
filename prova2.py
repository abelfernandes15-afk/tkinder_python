import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter import messagebox

cadrastro= tk.Tk()
cadrastro.title("dados pessoais")
cadrastro.configure(background="blue")
def enviar():
   nome = entrada_nome.get()
   sobrenome = entrada_sobrenome.get()
   nasc = data_nasc.get()
   cpf=entrada_cpf.get()
   cep = entrada_cep.get()
   estado= entrada_estado.get()
   cidade = entrada_cidade.get()
   
   sexo="masculino" if dd==1 else "feminino"
   dados = f"nome:{nome}\nsobrenome:{sobrenome}\ndatanascimento:{nasc}\ncpf:\n{cpf}\ncep{cep}\nestado{estado}\ncidade{cidade}"
   messagebox.showinfo('dados enviados',dados)

tk.Label(cadrastro,text="FORMULARIO DE CADRASTRO",font=("arial",15)).grid(column=1,pady=20)
tk.Label(cadrastro, text="nome:").grid(row=1, column=0)
entrada_nome=tk.Entry(cadrastro, width=30,font=("Arial",14))
entrada_nome.grid(row=1,column=1)

tk.Label(cadrastro, text="sobrenome:").grid(row=2, column=0)
entrada_sobrenome=tk.Entry(cadrastro, width=30,font=("Arial",14))
entrada_sobrenome.grid(row=2,column=1)

tk.Label(cadrastro, text="datanasc:").grid(row=3, column=0)
data_nasc=tk.Entry(cadrastro, width=30,font=("Arial",14))
data_nasc.grid(row=3,column=1)

tk.Label(cadrastro, text="CPF:").grid(row=4, column=0)
entrada_cpf=tk.Entry(cadrastro, width=30,font=("Arial",14))
entrada_cpf.grid(row=4,column=1)

tk.Label(cadrastro, text="CEP:").grid(row=5, column=0)
entrada_cep=tk.Entry(cadrastro, width=30,font=("Arial",14))
entrada_cep.grid(row=5,column=1)

tk.Label(cadrastro, text="estado:").grid(row=6, column=0)
entrada_estado=tk.Entry(cadrastro, width=30,font=("Arial",14))
entrada_estado.grid(row=6,column=1)

tk.Label(cadrastro, text="cidade:").grid(row=7, column=0)
entrada_cidade=tk.Entry(cadrastro, width=30,font=("Arial",14))
entrada_cidade.grid(row=7,column=1)

dd=tk.IntVar()
#radiobuton
tk.Label(cadrastro,text="sexo").grid(row=8,column=0)
tk.Radiobutton(cadrastro,text="masculino",font="arial",value=1,variable=dd)\
    .grid(row=8,column=1)
tk.Radiobutton(cadrastro,text="feminino",font=("arial"),value=2,variable=dd)\
    .grid(row=18,column=1)

tk.Button(cadrastro,text="usuario cadrastado",command=enviar).grid(row=19,column=1,pady=20)

cadrastro.mainloop()