# Projeto simples utilizando Tkinter
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

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

credenciais = [
		{
			"user": "Luis", 
			"password": "123456"
		}
	]

def verificar():
	# obtendo os dados digitados:
	user = i_user.get()
	password = i_password.get()

	# Verificando se é o administrador
	if user == "admin" and password == "admin":
		messagebox.showinfo("Login", "Seja Bem vindo Administrador!")
		print("Adm acessou o sistema.")

	# Verificando se é o usuário:
	elif user == credenciais[0]["user"] and password == credenciais[0]["password"]:
		messagebox.showinfo("Login", f"Seja Bem vindo(a) {user}!")
		print(f"Usuário {user} acessou o sistema.")

		# Percorrendo os frames e destruindo os conteúdos(limpar):
		for widget in frame_cima.winfo_children():
			widget.destroy()

		for widget in frame_baixo.winfo_children():
			widget.destroy()

		novaJanela()

	# Caso os dados sejam inválidos:
	else:
		messagebox.showinfo("Falha no Login","Ops! Credênciais inválidas...")
		print("Falha ao logar no sistema.")


def novaJanela():
	l_login = Label(frame_cima, text=f"Seja Bem vindo(a): {credenciais[0]['user']}", anchor=NE, font=("Ivy 15"), bg=cor1, fg=cor4)
	l_login.place(x=5, y=5)

	l_linha = Label(frame_cima, text="", width=275, anchor=NW, font=("Ivy 1"), bg=cor2, fg=cor4) 
	l_linha.place(x=10, y=45)

	l_user = Label(frame_baixo, text="Textos e informações", anchor=NW, font=("Ivy 15"), bg=cor1, fg=cor4)
	l_user.place(x=5, y=105)	

# Parte de baixo:
frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief="flat" )
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# ------------------Conteúdo da parte de baixo------------------

# Label do user:
l_user = Label(frame_baixo, text="User: ", anchor=NW, font=("Ivy 10"), bg=cor1, fg=cor4)
l_user.place(x=10, y=20)

# Caixa de entrada(input) do user:
i_user = Entry(frame_baixo, width=20, justify="left", font=("", 15), highlightthickness=1, relief="solid")
i_user.place(x=14, y=50)

# Label da senha:
l_password = Label(frame_baixo, text="Password: ", anchor=NW, font=("Ivy 10"), bg=cor1, fg=cor4)
l_password.place(x=10, y=95)

# Caixa de entrada(input) do user:
i_password = Entry(frame_baixo, width=20, show="*", justify="left", font=("", 15), highlightthickness=1, relief="solid")
i_password.place(x=14, y=130)


# ------------------Botão de Login------------------
b_login = Button(frame_baixo, text="Log in", width=35, height=2, font=("Ivy 8 bold"), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE, command=verificar)
b_login.place(x=15, y=180)

# Executar a aplicação:
janela.mainloop()
