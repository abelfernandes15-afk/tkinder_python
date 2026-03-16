import tkinter as tk 
#criaçao de janela
janela_main = tk.Tk()

janela_main.title("TIME")
janela_main.configure(background="blue")
janela_main.minsize(200,200)
#janela_main.maxsize(500,500)
janela_main.geometry("400x400")

#objetos em janela
tk.Label(janela_main,
        text="CRUZEIRO",
        bg="WHITE",
        font= ("arial",20,"bold"),
        ).pack()
         
#coloacar imagem
imagem=tk.PhotoImage(file="cruzeiro.png")
imagem=imagem.subsample(5,5)
tk.Label(janela_main,image=imagem).pack()

tk.Label(janela_main,
        text="imagem do cruzeiro respladece",
        bg= "gold",
        font= ("arial",15,"bold"),
        ).pack()


janela_main.mainloop()