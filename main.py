# Projeto simples utilizando Tkinter
from tkinter import *
from tkinter import Tk, ttk

# Cores em hexadecimal:
cor0 = "#f0f3f5" # Preta
cor1 = "#feffff" # Branca
cor2 = "#3fb5a3" # verda
cor3 = "#38576b" # cor para valor
cor4 = "#403d3d" # cor para letra

# Configuração da janela da aplicação:
janela = Tk()
janela.title("")
janela.geometry("310x300")
janela.configure(background = cor1)
janela.resizable(width=False, height=False)

# Dividindo o conteúdo da janela:

# Parte de cima:
frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief="flat" )
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

# Parte de baixo:
frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief="flat" )
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Executar a aplicação:
janela.mainloop()
