import Tkinter as tk
import datetime
import time
from time import gmtime, strftime
from Page import *
from Humidity import *
from LightSensitivity import *
from Temperature import *
from FeedCycle import *

class Settings(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       p1 = Temperature(self)
       p2 = FeedCycle(self)
       p3 = LightSensitivity(self)
       p4 = Humidity(self)

       buttonFrame = tk.Frame(self)
       buttonFrame.pack(side="top")
       container = tk.Frame(self)
       container.pack(side="top", expand =True, fill = "both")

       b1 = tk.Button(buttonFrame,
                       text="Temperature",
                       bg='#b2b2b2',
                       width=20,
                       height=10,
                       font=(None, 12),
                       borderwidth=1,
                       pady = 5,
                       command=p1.lift)
       b2 = tk.Button(buttonFrame,
                       text="FeedCycle",
                       bg='#b2b2b2',
                       width=20,
                       height=10,
                       font=(None, 12),
                       borderwidth=1,
                      padx = 5,
                      pady = 5,
                       command=p2.lift)
       b3 = tk.Button(buttonFrame,
                       text="Light Sensitivity",
                       bg='#b2b2b2',
                       width=20,
                       height=10,
                       font=(None, 12),
                       borderwidth=1,
                      padx = 5,
                      pady = 5,
                       command=p3.lift)
       b4 = tk.Button(buttonFrame,
                       text="Humidity",
                       bg='#b2b2b2',
                       width=20,
                       height=10,
                       font=(None, 12),
                       borderwidth=1,
                      padx = 5,
                      pady = 5,
                       command=p4.lift)
       b1.pack(side="left")
       b2.pack(side="left")
       b3.pack(side="left")
       b4.pack(side="left")

       p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

       hm= Humidity()
       print hm.get_humidity()
