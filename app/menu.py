from tkinter import *
from app.pages.vehicles_page import VehiclesPage
from app.pages.exit_page import ExitPage

class Menu(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        self.sidebar = Frame(self, bg='#ADD8E6', width=200)
        self.sidebar.pack(side=LEFT, fill=Y)

        self.container = Frame(self, bg='#B0E0E6')
        self.container.pack(side=RIGHT, fill=BOTH, expand=True)

        self.current_page = None

        self.create_button("VEICULOS", VehiclesPage)
        self.create_button("SAIR", ExitPage)

    def create_button(self, text, page):
        Button(
            self.sidebar,
            text=text,
            bd=0,
            bg="#ADD8E6",
            font="sylfaen 13 bold",
            command=lambda: self.show_page(page)
        ).pack(pady=20)

    def show_page(self, page_class):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = page_class(self.container)
        self.current_page.pack(fill="both", expand=True)