import Tkinter as tk
import datetime
import time
from time import gmtime, strftime
from Page import *
        
class Settings(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Welcome to the settings page")
       label.grid(row = 0, column = 0, sticky= "nsew")
       container = tk.Frame(self)
       container.grid(row=0,column = 0)

       tempScale = tk.Scale(container, from_=0, to=60, tickinterval=10,
                             orient="horizontal", borderwidth = 0, highlightthickness= 0, length=800)       
       humidityScale = tk.Scale(container, from_=0, to=60, tickinterval=10,
                             orient="horizontal", borderwidth = 0, highlightthickness= 0, length=800)       

       cycleScale = tk.Scale(container, from_=0, to=60, tickinterval=10,
                             orient="horizontal", borderwidth = 0, highlightthickness= 0, length=800)              
       lightScale = tk.Scale(container, from_=0, to=60, tickinterval=10,
                             orient="horizontal", borderwidth = 0, highlightthickness= 0, length=800)
       
       T1 = tk.Label(container, text="Temperature (C)", fg='White')
       T2 = tk.Label(container, text="Humidity (%)", fg='White')  
       T3 = tk.Label(container, text="Cycle", fg='White')
       T4 = tk.Label(container, text="Light Sensitivity", fg='White')

       tempScale.grid( row = 0, column = 1)
       humidityScale.grid(row = 1, column = 1)
       cycleScale.grid(row = 2, column = 1)
       lightScale.grid(row = 3, column = 1)

       tempScale.set(25)                                        #Sets the default temperature value to 25C
       humidityScale.set(25)                                    #Sets humidity values to 25%
       cycleScale.set(25)                                       #Sets cycle values to 25%
       lightScale.set(25)                                       #Sets light values to 25%

       T1.grid(row=0, column=2)
       T2.grid(row=1, column=2)
       T3.grid(row=2, column=2)
       T4.grid(row=3, column=2)
