import tkinter as tk 
#criaçao de janela
janela_main = tk.Tk()

janela_main.title("minha janela")
janela_main.configure(background="blue")
janela_main.minsize(200,200)
#janela_main.maxsize(500,500)
janela_main.geometry("300x300")

#objetos em janela
tk.Label(janela_main,
        text="hello word",
        bg="orange",
        font= ("arial",20,"bold"),
        ).pack()
         
tk.Label(janela_main,
        text="Douglas",
        bg= "gold",
        font= ("arial",15),
        ).pack()
#coloacar imagem
imagem=tk.PhotoImage(file="tigre.png")
imagem=imagem.subsample(3,3)
tk.Label(janela_main,image=imagem).pack()




janela_main.mainloop()