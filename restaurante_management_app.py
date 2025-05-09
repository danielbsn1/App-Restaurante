
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from PIL import Image, ImageTk


class RestauranteApp:
    def __init__(self):
        self.monthly_data = {}  # Armazena os dados por mês

    def add_monthly_data(self, mes, revenue, expense, clientes):
        if revenue < 0 or expense < 0 or clientes < 0:
            return False
        self.monthly_data[mes] = (revenue, expense, clientes)
        return True

    def total_annual_revenue(self):
        return sum([data[0] for data in self.monthly_data.values()])

    def total_annual_expenses(self):
        return sum([data[1] for data in self.monthly_data.values()])

    def total_annual_clientes(self):
        return sum([data[2] for data in self.monthly_data.values()])

    def get_stats(self):
        months = len(self.monthly_data)
        if months == 0:
            return "Nenhum dado registrado ainda!"

        stats = (
            f"Meses registrados: {months}\n"
            f"Receita mensal média: R${self.total_annual_revenue() / months:.2f}\n"
            f"Gastos mensais médios: R${self.total_annual_expenses() / months:.2f}\n"
            f"Clientes mensais médios: {self.total_annual_clientes() / months:.2f}\n"
            f"Renda anual: R${self.total_annual_revenue():.2f}\n"
            f"Gastos anuais: R${self.total_annual_expenses():.2f}\n"
            f"Clientes anuais: {self.total_annual_clientes()}\n"
        )
        return stats


def load_icon(path):
    try:
        img = Image.open(path)
        img = img.resize((20, 20),)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None  # Retorna None se o ícone não for carregado


class RestauranteAppGUI:
    def __init__(self, root):
        self.btn_export_csv = None
        self.btn_excluir = None
        self.btn_editar = None
        self.root = root
        self.tree = ttk.Treeview(self.root, columns=("Mês", "Receita", "Despesa", "Clientes"), show="headings")
        self.btn_show_stats = ttk.Button(self.root, text="Mostrar Estatísticas", command=self.show_stats)
        self.btn_add_data = None
        self.entry_clientes = ttk.Entry(self.root)
        self.entry_despesas = ttk.Entry(self.root)
        self.entry_receita = None
        self.entry_mes = ttk.Entry(self.root)
        self.app = RESTAURANTEAPP()
        self.root = root
        self.root.title("App Restaurante")
        self.create_widgets()

    def create_widgets(self):
        # Carregando ícones para uso nos botões
        icon_add = load_icon("add_icon.png") or None
        icon_export = load_icon("export_icon.png") or None
        icon_edit = load_icon("edit_icon.png") or None
        icon_delete = load_icon("delete_icon.png") or None

        # Título
        ttk.Label(self.root, text="App Restaurante", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Campo para o mês
        ttk.Label(self.root, text="Mês:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_mes.grid(row=1, column=1, padx=10, pady=5)

        # Entradas para receita, despesas e clientes
        ttk.Label(self.root, text="Receita mensal (R$):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_receita = ttk.Entry(self.root)
        self.entry_receita.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Gastos mensais (R$):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_despesas.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Clientes mensais:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_clientes.grid(row=4, column=1, padx=10, pady=5)

        # Botões principais
        self.btn_add_data = ttk.Button(
            self.root, text="Adicionar Dados", image=icon_add, compound="left", command=self.add_data
        )
        self.btn_add_data.image = icon_add
        self.btn_add_data.grid(row=5, column=0, padx=10, pady=10)

        self.btn_show_stats.grid(row=5, column=1, padx=10, pady=10)

        # Tabela de dados
        self.tree.heading("Mês", text="Mês")
        self.tree.heading("Receita", text="Receita (R$)")
        self.tree.heading("Despesa", text="Despesa (R$)")
        self.tree.heading("Clientes", text="Clientes")
        self.tree.grid(row=6, column=0, columnspan=2, sticky="nsew")

        # Botões de edição
        self.btn_editar = ttk.Button(self.root, text="Editar Dados", image=icon_edit, compound="left",
                                     command=self.editar_dados)
        self.btn_editar.image = icon_edit
        self.btn_editar.grid(row=7, column=0, padx=10, pady=5)

        self.btn_excluir = ttk.Button(self.root, text="Excluir Dados", image=icon_delete, compound="left",
                                      command=self.excluir_dados)
        self.btn_excluir.image = icon_delete
        self.btn_excluir.grid(row=7, column=1, padx=10, pady=5)

        # Botão para exportar CSV
        self.btn_export_csv = ttk.Button(
            self.root, text="Exportar CSV", image=icon_export, compound="left", command=self.exportar_csv
        )
        self.btn_export_csv.image = icon_export
        self.btn_export_csv.grid(row=8, column=0, columnspan=2, pady=10)

    def add_data(self):
        self.entry_mes.get().strip()

class RESTAURANTEAPP:
    def __init__(self):
        self.monthly_data = {}  # Armazena os dados por mês

    def add_monthly_data(self, mes, revenue, expense, clientes):
        if revenue < 0 or expense < 0 or clientes < 0:
            return False
        self.monthly_data[mes] = (revenue, expense, clientes)
        return True

    def total_annual_revenue(self):
        return sum([data[0] for data in self.monthly_data.values()])

    def total_annual_expenses(self):
        return sum([data[1] for data in self.monthly_data.values()])

    def total_annual_clientes(self):
        return sum([data[2] for data in self.monthly_data.values()])

    def get_stats(self):
        months = len(self.monthly_data)
        if months == 0:
            return "Nenhum dado registrado ainda!"

        stats = (
            f"Meses registrados: {months}\n"
            f"Receita mensal média: R${self.total_annual_revenue() / months:.2f}\n"
            f"Gastos mensais médios: R${self.total_annual_expenses() / months:.2f}\n"
            f"Clientes mensais médios: {self.total_annual_clientes() / months:.2f}\n"
            f"Renda anual: R${self.total_annual_revenue():.2f}\n"
            f"Gastos anuais: R${self.total_annual_expenses():.2f}\n"
            f"Clientes anuais: {self.total_annual_clientes()}\n"
        )
        return stats


    def load_icon(self):
        try:
          img = Image.open(self)
          img = img.resize((20, 20),)
          return ImageTk.PhotoImage(img)
        except Exception:
          return None  # Retorna None se o ícone não for carregado


class RESTAURANTEAPP1:
    def __init__(self, root):
        self.editar_dados = None
        self.btn_export_csv = None
        self.btn_excluir = None
        self.btn_editar = None
        self.root = root
        self.tree = ttk.Treeview(self.root, columns=("Mês", "Receita", "Despesa", "Clientes"), show="headings")
        self.btn_show_stats = ttk.Button(self.root, text="Mostrar Estatísticas", command=self.show_stats)
        self.btn_add_data = None
        self.entry_clientes = ttk.Entry(self.root)
        self.entry_despesas = ttk.Entry(self.root)
        self.entry_receita = None
        self.entry_mes = ttk.Entry(self.root)
        self.app = RESTAURANTEAPP()
        self.root = root
        self.root.title("App Restaurante")
        self.create_widgets()

    def create_widgets(self):
        # Carregando ícones para uso nos botões
        icon_add = load_icon("add_icon.png") or None
        icon_export = load_icon("export_icon.png") or None
        icon_edit = load_icon("edit_icon.png") or None
        icon_delete = load_icon("delete_icon.png") or None

        # Título
        ttk.Label(self.root, text="App Restaurante", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Campo para o mês
        ttk.Label(self.root, text="Mês:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_mes.grid(row=1, column=1, padx=10, pady=5)

        # Entradas para receita, despesas e clientes
        ttk.Label(self.root, text="Receita mensal (R$):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_receita = ttk.Entry(self.root)
        self.entry_receita.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Gastos mensais (R$):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_despesas.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Clientes mensais:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_clientes.grid(row=4, column=1, padx=10, pady=5)

        # Botões principais
        self.btn_add_data = ttk.Button(
            self.root, text="Adicionar Dados", image=icon_add, compound="left", command=self.add_data
        )
        self.btn_add_data.image = icon_add
        self.btn_add_data.grid(row=5, column=0, padx=10, pady=10)

        self.btn_show_stats.grid(row=5, column=1, padx=10, pady=10)

        # Tabela de dados
        self.tree.heading("Mês", text="Mês")
        self.tree.heading("Receita", text="Receita (R$)")
        self.tree.heading("Despesa", text="Despesa (R$)")
        self.tree.heading("Clientes", text="Clientes")
        self.tree.grid(row=6, column=0, columnspan=2, sticky="nsew")

        # Botões de edição
        self.btn_editar = ttk.Button(self.root, text="Editar Dados", image=icon_edit, compound="left",
                                     command=self.editar_dados)
        self.btn_editar.image = icon_edit
        self.btn_editar.grid(row=7, column=0, padx=10, pady=5)

        self.btn_excluir = ttk.Button(self.root, text="Excluir Dados", image=icon_delete, compound="left",
                                      command=self.excluir_dados)
        self.btn_excluir.image = icon_delete
        self.btn_excluir.grid(row=7, column=1, padx=10, pady=5)

        # Botão para exportar CSV
        self.btn_export_csv = ttk.Button(
            self.root, text="Exportar CSV", image=icon_export, compound="left", command=self.exportar_csv
        )
        self.btn_export_csv.image = icon_export
        self.btn_export_csv.grid(row=8, column=0, columnspan=2, pady=10)

    def add_data(self):
        mes = self.entry_mes.get().strip()
        if not mes:
            messagebox.showerror("Erro", "O campo 'Mês' não pode estar vazio.")
            return

        try:
            receita = float(self.entry_receita.get())
            despesas = float(self.entry_despesas.get())
            clientes = int(self.entry_clientes.get())

            if mes in self.app.monthly_data:
                messagebox.showerror("Erro", f"Dados para o mês '{mes}' já existem.")
                return

            if self.app.add_monthly_data(mes, receita, despesas, clientes):
                self.atualizar_tabela()
                messagebox.showinfo("Sucesso", f"Dados de '{mes}' adicionados com sucesso.")
                self.clear_entries()
            else:
                messagebox.showerror("Erro", "Os valores não podem ser negativos.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para receita, despesas e clientes.")

    def atualizar_tabela(self):
        self.tree.delete(*self.tree.get_children())
        for mes, (receita, despesa, clientes) in self.app.monthly_data.items():
            self.tree.insert("", "end", values=(mes, f"R${receita:.2f}", f"R${despesa:.2f}", clientes))

    def excluir_dados(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Selecione um mês para excluir.")
            return

        mes: str = self.tree.item(selected_item)["values"][0]
        confirmar = messagebox.askyesno("Excluir Dados", f"Deseja excluir os dados de '{mes}'?")
        if confirmar:
            del self.app.monthly_data[mes]
            self.atualizar_tabela()

    def show_stats(self):
        stats = self.app.get_stats()
        messagebox.showinfo("Estatísticas", stats)

    def clear_entries(self):
        self.entry_mes.delete(0, tk.END)
        self.entry_receita.delete(0, tk.END)
        self.entry_despesas.delete(0, tk.END)
        self.entry_clientes.delete(0, tk.END)

    def exportar_csv(self, csv=None):
        try:
            with open("dados_restaurante.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Mês", "Receita (R$)", "Despesa (R$)", "Clientes"])
                for mes, (receita, despesa, clientes) in self.app.monthly_data.items():
                    writer.writerow([mes, f"R${receita:.2f}", f"R${despesa:.2f}", clientes])
            messagebox.showinfo("Sucesso", "Dados exportados para 'dados_restaurante.csv'.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar CSV: {e}")


def main():
    root = tk.Tk()

    RESTAURANTEAPP1(root)

    root.mainloop()


if __name__ == "__main__":
     main()