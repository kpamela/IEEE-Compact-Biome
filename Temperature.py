import Tkinter as tk
from Page import *

class Temperature(Page):
   def __init__(self, *args, **kwargs):
      Page.__init__(self, *args, **kwargs)
      container = tk.Frame(self)
      container.pack(side="top", expand =True, fill = "both")

      self.tempScale = tk.Scale(container, from_=0, to=60, tickinterval=10, width= 30,
                             orient="horizontal", borderwidth = 0, highlightthickness= 0, length=800)
      self.tempLabel = tk.Label(container, text="Temperature(C)\n \nCurrent temperature setting:"+ str(self.tempScale.get()) , fg='White')
      self.confirmButton = tk.Button(container, text="Confirm", bg='#b2b2b2',width=10,height=2,
                       font=(None, 12), command=self.set_temp)

      self.tempValue = 25
      self.tempScale.set(25)

      self.tempScale.pack(side="top")
      self.confirmButton.pack(side="bottom")
      self.tempLabel.pack(side="bottom")

   def get_temp(self):
      print self.tempValue

   def set_temp(self):
      self.tempValue = self.tempScale.get()
      self.tempLabel.config(text="Temperature(C)\n \nCurrent temperature setting:"+ str(self.tempScale.get()))
