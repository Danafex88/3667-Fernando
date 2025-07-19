import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface Grafica Responsavel")
        self.geometry("400x200")
        self.resizable(True, True)

        # Configurar lunhas e colunsa para se expandirem
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Frames para as duas telas
        self.frame_input = tk.Frame(self)
        self.frame_welcome = tk.Frame(self)

        # Exibir a Primeira tela
        self.show_frame(self.frame_input)

        # Variavel para armazenar o nome do usuário
        self.user_name = tk.StringVar()

        # Inicializar as telas
        self.create_input_frame()
        self.create_welcome_frame()

    def create_input_frame(self):
        # Configurar grid para centralização
        self.frame_input.grid(row=0, column=0, sticky="nsew")
        self.frame_input.grid_rowconfigure(0, weight=1)
        self.frame_input.grid_columnconfigure(0, weight=1)

    # Frame central dentro da tela de input
        inner_frame = tk.Frame(self.frame_input)
        inner_frame.grid(row=0, column=0, sticky="nsew")

    # Centralizar o conteudo dentro do frame
        inner_frame.grid_rowconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(0, weight=1)

   # Label e Entry contralizados
        label = tk.Label(
            inner_frame, text="Informe seu nome: ", font=("Arial", 12))
        label.grid(row=0, column=0, pady=10, sticky="n")

        entry_name = tk.Entry(
            inner_frame, textvariable=self.user_name, font=("Arial", 12))
        entry_name.grid(row=1, column=0, padx=10, pady=10, sticky="n")

        btn_next = tk.Button(inner_frame, text="Continuar",
                             command=self.show_welcome_frame)
        btn_next.grid(row=2, column=0, pady=10, sticky="n")

    def create_welcome_frame(self):
        # Configurar grid para centralização
        self.frame_welcome.grid(row=0, column=0,  sticky="nsew")
        self.frame_welcome.grid_rowconfigure(0, weight=1)
        self.frame_welcome.grid_columnconfigure(0, weight=1)

        # Frame central dentro da tela de boas-vindas
        inner_frame = tk.Frame(self.frame_welcome)
        inner_frame.grid(row=0, column=0, sticky="nsew")

        # Centralizar o conteudo dentro do frame
        inner_frame.grid_rowconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(0, weight=1)

        # Mensagem de Boas Vindas
        welcome_message = f"Bem-vindo à interface gráfica de Python, {self.user_name.get()}"
        label_welcome = tk.Label(inner_frame, text=welcome_message,
                                 font=("Arial", 14), wraplength=300, justify="center")
        label_welcome.grid(row=0, column=0, padx=20, pady=20, sticky="n")

    def show_frame(self, frame):
        frame.tkraise()

    def show_welcome_frame(self):
        # Atualiar o texto de boas vindas com o nome informado
        self.create_welcome_frame()
        self.show_frame(self.frame_welcome)


if __name__ == "__main__":
    # Cria a instancia principal do aplicativo
    app = Application()
    # Inicia o loop principal do tkinter para manter a janela aberta
    app.mainloop()
