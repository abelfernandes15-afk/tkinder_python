import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter import messagebox

cadrastro= tk.Tk()
cadrastro.title("dados pessoais")

def enviar():
   nome = entrada_nome.get()
   idade = entrada_idade.get()
   dados_profissao =combo_prof.get()
   escolaridade= combo_esc.get()
   
   cargo="gerente" if dd==1 else "funcionario"
   msg = f"nome:{nome}\nidade:{idade}\ndados_profissao:{dados_profissao}\nescolaridade: {escolaridade}"
   messagebox.showinfo('dados enviados',msg)

tk.Label(cadrastro,text="FORMULARIO DE CADRASTRO",font=("arial",15)).grid(column=1,pady=20)
tk.Label(cadrastro, text="nome:").grid(row=1, column=0)
entrada_nome=tk.Entry(cadrastro, width=30,font=("Arial",14))
entrada_nome.grid(row=1,column=1)

tk.Label(cadrastro,text="FORMULARIO DE CADRASTRO",font=("arial",15)).grid(column=1,pady=20)
tk.Label(cadrastro, text="idade").grid(row=2, column=0)
entrada_idade=tk.Entry(cadrastro, width=30,font=("Arial",14))
entrada_idade.grid(row=2,column=1)

#combobox
tk.Label(cadrastro,text="profissao").grid(row=3,column=0)
combo_prof=ttk.Combobox(cadrastro,values=["mecanico","auxilar de produçao","engenheiro"])
combo_prof.grid(row=4,column=1)

tk.Label(cadrastro,text="escolaridade").grid(row=5,column=0)
combo_esc=ttk.Combobox(cadrastro,values=["ensino fundamental","ensino medio","superior"])
combo_esc.grid(row=6,column=1)

dd=tk.IntVar()
#radiobuton
tk.Label(cadrastro,text="cargo").grid(row=7,column=0)
tk.Radiobutton(cadrastro,text="funcionario",font="arial",value=1,variable=dd)\
    .grid(row=8,column=1)
tk.Radiobutton(cadrastro,text="gerente",font=("arial"),value=2,variable=dd)\
    .grid(row=9,column=1)

tk.Button(cadrastro,text="enviar",command=enviar).grid(row=10,column=1,pady=20)

cadrastro.mainloop()