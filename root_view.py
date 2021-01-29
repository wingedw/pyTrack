import tkinter as tk
from tkinter.ttk import Notebook
import issues_view as iv
import dashboard_view as dash
import settings_view as sv
import add_view as av


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("pyTrack Issue Tracker")
        self.geometry('972x600')
        self.resizable(False, False)

        tab_control = Notebook(self)
        tab1 = tk.Frame(tab_control)
        tab2 = tk.Frame(tab_control)
        tab3 = tk.Frame(tab_control)
        tab4 = tk.Frame(tab_control)

        tab_control.add(tab1, text='Dashboard')
        tab_control.add(tab2, text='Add Issue')
        tab_control.add(tab3, text='Issues Details')
        tab_control.add(tab4, text='Project Settings')

        tab_control.pack(expand=1, fill="both")

        self.dash_board = dash.Dashboard(tab1)
        self.add_view = av.Add_Issue(tab2)
        self.list = iv.IssueList(tab3, height=15)
        self.form = iv.UpdateIssueForm(tab3)
        self.btn_new = tk.Button(tab3, text="Add new contact")
        self.settings = sv.Settings(tab4)

        self.dash_board.place(x=0, y=0)
        self.add_view.place(x=0,y=0)
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
        self.settings.place(x=0, y=0)

    def set_ctrl(self, ctrl):
        self.btn_new.config(command=ctrl.create_issue)
        self.list.bind_doble_click(ctrl.select_issue)
        self.form.bind_save(ctrl.update_issue)
        self.form.bind_delete(ctrl.delete_issue)

    def add_issue(self, issue):
        self.list.insert(issue)

    def update_issue(self, issue, index):
        self.list.update(issue, index)

    def remove_issue(self, index):
        self.form.clear()
        self.list.delete(index)

    def get_details(self):
        return self.form.get_details()

    def load_details(self, issue):
        self.form.load_details(issue)
