import Tkinter as tk
from Page import *

class Override(Page):
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)
        B1 = tk.Button(buttonFrame1,
                        text="Fans Only",
                        bg='#f18973',
                        width=10,
                        height=1,
                        font=(None, 12))
        B2 = tk.Button(buttonFrame1,
                        text="Heating System",
                        bg='#f18973',
                        width=10,
                        height=1,
                        font=(None, 12))
        B3 = tk.Button(buttonFrame1,
                        text="Cooling System",
                        bg='#f18973',
                        width=10,
                        height=1,
                        font=(None, 12))
        B4 = tk.Button(buttonFrame1,
                        text="Lights",
                        bg='#f18973',
                        width=10,
                        height=1,
                        font=(None, 12))
        B5 = tk.Button(buttonFrame1,
                        text="Feeding",
                        bg='#f18973',
                        width=10,
                        height=1,
                        font=(None, 12))

        B1.pack(side = "left", expand = True)
        B2.pack(side = "left", expand = True)
        B3.pack(side = "left", expand = True)
        B4.pack(side = "left", expand = True)
        B5.pack(side = "left", expand = True)
   def set_light():
   def set_feeding():
   def set_fans():
   def set_cooling():
   def set_heating():
