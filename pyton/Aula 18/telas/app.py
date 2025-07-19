import tkinter as tk
from tela1 import Tela1
from tela2 import Tela2
from tela3 import Tela3


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicativo com Multiplas Telas")
        self.geometry("400x200")
        self.resizable(True, True)

        # Istanciar as telas
        self.frame1 = Tela1(self)
        self.frame2 = Tela2(self)
        self.frame3 = Tela3(self)

        # Configurar layout responsivo
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Exibir a tela inicial
        self.show_frame(self.frame1)

    def show_frame(self, frame):
        frame.tkraise()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
