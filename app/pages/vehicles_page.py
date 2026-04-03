from tkinter import *
from tkinter import ttk
from app.database import Database

class VehiclesPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.db = Database()

        frame = LabelFrame(self, text="FROTA")
        frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        self.table = ttk.Treeview(
            frame,
            columns=('ID', 'placa', 'tipo'),
            show='headings'
        )

        self.table.heading('ID', text='ID')
        self.table.heading('placa', text='PLACA')
        self.table.heading('tipo', text='TIPO')

        self.table.pack(fill=BOTH, expand=True)

        self.load_data()

    def load_data(self):
        query = "SELECT id_veiculo, placa, tipo FROM automoveis"
        for item in self.db.query(query).fetchall():
            self.table.insert('', 'end', values=item)