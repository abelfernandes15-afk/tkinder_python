import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter import messagebox


janela= tk.Tk()
janela.title("formulario")
tk.Label(janela, text="nome:").grid(row=0, column=0)
entrada_nome=tk.Entry(janela, width=30,font=("Arial",14))
entrada_nome.grid(row=0,column=1)
opc=tk.IntVar
#radiobuton
tk.Label(janela,text="sexo").grid(row=1,column=0)
Frame_sx=Frame(janela)
Frame_sx.grid(row=1,column=1,padx=10,pady=5,sticky="w")
tk.Radiobutton(Frame_sx,text="masculino",font="arial",value=1,variable=opc)\
.pack(anchor="w")
tk.Radiobutton(Frame_sx,text="feminino",font=("arail"),value=2,variable=opc)\
    .pack(anchor="w")



























janela.mainloop()