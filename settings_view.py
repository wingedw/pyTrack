import tkinter as tk


class Settings(tk.Frame):
    def __init__(self,  master, **kwargs):
        super().__init__(master)
        self.Label = tk.Label(self,
                              text='Welcome to Your Project Settings').grid(column=0,
                                                                            row=0,
                                                                            padx=30,
                                                                            pady=30)
        self.Label = tk.Label(self, text='Project Settings to implemented in Version 2 and 3').grid(column=0,
                                                                                                    row=1,
                                                                                                    padx=2,
                                                                                                    pady=(5, 0))


