import Tkinter as tk
from Settings import *
from Page import *

class Kill(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Choose a component to power down")
       label.pack(side="top")
       buttonFrame1= tk.Frame(self)
       buttonFrame1.pack(side="bottom", fill ="y")       
       buttonFrame2= tk.Frame(self)
       buttonFrame2.pack(side="bottom", fill ="y")

       B1 = tk.Button(buttonFrame1,
                       text="Component1",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
       B2 = tk.Button(buttonFrame1,
                       text="Component 2",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
       B3 = tk.Button(buttonFrame1,
                       text="Component 3",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
       B4 = tk.Button(buttonFrame1,
                       text="Component 4",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
       B5 = tk.Button(buttonFrame1,
                       text="Component 3",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
       B6  = tk.Button(buttonFrame1,
                       text="Component 4",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
    
       B1.pack(side = "left", expand = True)
       B2.pack(side = "left", expand = True)
       B3.pack(side = "left", expand = True)
       B4.pack(side = "left", expand = True)
       B5.pack(side = "left", expand = True)
       B6.pack(side = "left", expand = True)

       B7 = tk.Button(buttonFrame2,
                       text="Component1",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
       B8 = tk.Button(buttonFrame2,
                       text="Component 2",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
       B9 = tk.Button(buttonFrame2,
                       text="Component 3",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
       B10 = tk.Button(buttonFrame2,
                       text="Component 4",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
       B11 = tk.Button(buttonFrame2,
                       text="Component 3",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
       B12   = tk.Button(buttonFrame2,
                       text="Component 4",
                       bg='#f18973',
                       width=10,
                       height=1,
                       font=(None, 12))
    
       B7.pack(side = "left", expand = True)
       B8.pack(side = "left", expand = True)
       B9.pack(side = "left", expand = True)
       B10.pack(side = "left", expand = True)
       B11.pack(side = "left", expand = True)
       B12.pack(side = "left", expand = True)
