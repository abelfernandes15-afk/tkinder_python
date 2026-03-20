import tkinter as tk

janela=tk.Tk()
janela.geometry('400x400')
janela.title("mover elementos")

texto=tk.Label(text="nome")
texto.place(x=50,y=60)

janela.mainloop()