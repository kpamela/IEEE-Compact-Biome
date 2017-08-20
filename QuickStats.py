import Tkinter as tk
from Page import *

class QuickStats(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page ")
       label.pack(side="top", fill="both", expand=True)
