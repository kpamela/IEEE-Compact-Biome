import Tkinter as tk
from Settings import *
from Page import *

class Kill(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This isbpage 3")
       #label.pack(side="top", fill="both", expand=True)

       B1 = tk.Button(self,
                       text="Component1",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0)
       B2 = tk.Button(self,
                       text="Component 2",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0)
       B3 = tk.Button(self,
                       text="Component 3",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0)
       B4 = tk.Button(self,
                       text="Component 4",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0)
       B5 = tk.Button(self,
                       text="Component 3",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0,
                       padx=10,
                       pady =10)
       B6  = tk.Button(self,
                       text="Component 4",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0,
                       padx =10,
                       pady =10)
    
       B1.grid(row=0, column=0)
       B2.grid(row=0, column=1)
       B3.grid(row=0, column=2)
       B4.grid(row=1, column=0)
       B5.grid(row=1, column=1)
       B6.grid(row=1, column=2)
