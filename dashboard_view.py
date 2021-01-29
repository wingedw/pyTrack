import tkinter as tk


class Dashboard(tk.Frame):
    def __init__(self,  master, **kwargs):
        super().__init__(master)
        self.Label = tk.Label(self,
                              text="Welcome to Your Dashboard").grid(column=0,
                                                                     row=0,
                                                                     padx=30,
                                                                     pady=30)
        self.Label = tk.Label(self, text='Dashboard to implemented in Version 2').grid(column=0,
                                                                                       row=1,
                                                                                       padx=2,
                                                                                       pady=(5, 0))
        quit_btn = tk.Button(master, text="Exit pyTrack", command=self.quit)
        quit_btn.place(x=870, y=5)


