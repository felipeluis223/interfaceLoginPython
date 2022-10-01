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

# ------------------Parte de cima------------------
frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief="flat" )
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

# Conteúdo da parte de cima:
l_login = Label(frame_cima, text="LOGIN", anchor=NE, font=("Ivy 20"), bg=cor1, fg=cor4)
l_login.place(x=5, y=5)

l_linha = Label(frame_cima, text="", width=275, anchor=NW, font=("Ivy 1"), bg=cor2, fg=cor4) 
l_linha.place(x=10, y=45)

# Parte de baixo:
frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief="flat" )
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# ------------------Conteúdo da parte de baixo------------------

# Label do user:
l_nome = Label(frame_baixo, text="User: ", anchor=NW, font=("Ivy 10"), bg=cor1, fg=cor4)
l_nome.place(x=10, y=20)

# Caixa de entrada(input) do user:
i_nome = Entry(frame_baixo, width=20, justify="left", font=("", 15), highlightthickness=1, relief="solid")
i_nome.place(x=14, y=50)

# Label da senha:
l_password = Label(frame_baixo, text="Password: ", anchor=NW, font=("Ivy 10"), bg=cor1, fg=cor4)
l_password.place(x=10, y=95)

# Caixa de entrada(input) do user:
i_password = Entry(frame_baixo, width=20, justify="left", font=("", 15), highlightthickness=1, relief="solid") # Caixa da entrada de dados:
i_password.place(x=14, y=130)


# ------------------Botão de Login------------------
b_login = Button(frame_baixo, text="Log in", width=35, height=2, font=("Ivy 8 bold"), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_login.place(x=15, y=180)

# Executar a aplicação:
janela.mainloop()
