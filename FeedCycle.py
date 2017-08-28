import Tkinter as tk
from Page import *


class FeedCycle(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       container = tk.Frame(self)
       container.pack(side="top", expand =True, fill = "both")
       feedScale = tk.Scale(container, from_=0, to=60, tickinterval=10,
                           orient="horizontal", borderwidth = 0, highlightthickness= 0, length=800)
