import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter import messagebox

janela= tk.Tk()
janela.title("FORMULARIO")
janela.geometry("300x300")

def enviar():
   nome = entrada_nome.get()
   estado = combo_estado.get()
   sexo = opc.get()
   sexo_texto="masculino" if sexo==1 else "feminino"
   msg = f"nome:{nome}\nestado:{estado}\nsexo:{sexo_texto}"
   messagebox.showinfo('dados enviados',enviar)


#entrada de texto
tk.Label(janela,text="FORMULARIO DE CADRASTRO",font=("arial",15)).grid(column=1,pady=20)
tk.Label(janela, text="nome:").grid(row=1, column=0)
entrada_nome=tk.Entry(janela, width=30,font=("Arial",14))
entrada_nome.grid(row=1,column=1)

opc=tk.IntVar()
#radiobuton
tk.Label(janela,text="sexo").grid(row=3,column=0)
tk.Radiobutton(janela,text="masculino",font="arial",value=1,variable=opc)\
    .grid(row=4,column=1)
tk.Radiobutton(janela,text="feminino",font=("arail"),value=2,variable=opc)\
    .grid(row=5,column=1)

#combobox
tk.Label(janela,text="estado").grid(row=6,column=0)
combo_estado=ttk.Combobox(janela,values=['MG',"SP","RJ","RN","BA"])
combo_estado.grid(row=7,column=1)
#botao
tk.Button(janela,text="enviar",command=enviar).grid(row=8,column=1,pady=20)




janela.mainloop()