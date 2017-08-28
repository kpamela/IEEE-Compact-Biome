import Tkinter as tk
from Page import *

class Humidity(Page):
   def __init__(self, *args, **kwargs):
      Page.__init__(self, *args, **kwargs)
      container = tk.Frame(self)
      container.pack(side="top", expand =True, fill = "both")

      self.humidityScale = tk.Scale(container, from_=0, to=60, tickinterval=10, width= 30,
                             orient="horizontal", borderwidth = 0, highlightthickness= 0, length=800)
      self.humidityLabel = tk.Label(container, text="Humidity(%)" , fg='White')
      self.confirmButton = tk.Button(container, text="Confirm", bg='#b2b2b2',width=10,height=2,
                       font=(None, 12), command=self.set_humidity)

      self.humidityValue = 25
      self.humidityScale.set(25)

      self.humidityScale.pack(side="top")
      self.confirmButton.pack(side="bottom")
      self.humidityLabel.pack(side="bottom")

   def get_humidity(self):
      print self.humidityValue

   def set_humidity(self):
      self.humidityValue = self.humidityScale.get()
      print self.humidityValue
