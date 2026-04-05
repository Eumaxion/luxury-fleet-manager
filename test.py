import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema")
        self.geometry("400x300")

        self.frame_atual = None
        self.mostrar_login()

    def trocar_frame(self, novo_frame):
        if self.frame_atual is not None:
            self.frame_atual.destroy()  # apaga tela atual

        self.frame_atual = novo_frame(self)
        self.frame_atual.pack(fill="both", expand=True)

    def mostrar_login(self):
        self.trocar_frame(LoginFrame)

    def mostrar_menu(self):
        self.trocar_frame(MenuFrame)


class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Usuário").pack()
        self.user = tk.Entry(self)
        self.user.pack()

        tk.Label(self, text="Senha").pack()
        self.senha = tk.Entry(self, show="*")
        self.senha.pack()

        tk.Button(self, text="Login", command=self.verificar).pack()

    def verificar(self):
        if self.user.get() == "admin" and self.senha.get() == "123":
            self.master.mostrar_menu()  # troca de tela
        else:
            print("Login errado")


class MenuFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="MENU PRINCIPAL").pack()

        tk.Button(self, text="Opção 1").pack()
        tk.Button(self, text="Opção 2").pack()

        tk.Button(self, text="Logout", command=master.mostrar_login).pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()