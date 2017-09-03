import Tkinter as tk
from Page import *

class LightSensitivity(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       container = tk.Frame(self)
       container.pack(side="top", expand =True, fill = "both")
       self.lightValue= 50
       
       self.lightScale = tk.Scale(container, from_=0, to=100, tickinterval=10,
                           orient="horizontal", borderwidth = 0, highlightthickness= 0, length=800)
       self.confirmButton = tk.Button(container, text="Confirm", bg='#b2b2b2',width=10,height=2,
                           font=(None, 12), command=self.set_lightValue)

       self.lightScale.set(50)
       
       self.lightScale.pack(side="top")
       self.confirmButton.pack(side="bottom")

   def get_lightValue(self):
      print self.lightValue

   def set_lightValue(self):
      self.lightValue = self.lightScale.get()
      print self.lightValue
