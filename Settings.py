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

       self.p1 = Temperature(self)
       self.p2 = FeedCycle(self)
       self.p3 = LightSensitivity(self)
       self.p4 = Humidity(self)

       p1= self.p1
       p2= self.p2
       p3= self.p3
       p4= self.p4
       infoFrame = tk.Frame(self)
       infoFrame.pack(side="top")
       buttonFrame = tk.Frame(self)
       buttonFrame.pack(side="top")
       container = tk.Frame(self)
       container.pack(side="top", expand =True, fill = "both")
       confirmFrame = tk.Frame(self)
       confirmFrame.pack(side="top")
       info_str = "Current Settings" + "\nHumidity:" + str(p4.humidityValue)+ "\nTemperature"+str(p1.tempValue)
       info = tk.Label(infoFrame, bd =0,text=info_str)

       b1 = tk.Button(buttonFrame,
                       text="Temperature",
                       bg='#b2b2b2',
                       width=20,
                       height=10,
                       font=(None, 12),
                       borderwidth=1,
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
                       command=p3.lift)
       b4 = tk.Button(buttonFrame,
                       text="Humidity",
                       bg='#b2b2b2',
                       width=20,
                       height=10,
                       font=(None, 12),
                       borderwidth=1,
                      command=p4.lift)

       def update_info(self):
           info_str = "Current Settings" + "\nHumidity:" + str(p4.humidityValue)+ "%\nTemperature: "+str(p1.tempValue) + "C\nLightValue: "+str(p3.lightValue)
           info.config(text=info_str)

       p1.confirmButton.bind("<Button>",update_info, add="+")
       p2.confirmButton.bind("<Button>",update_info, add="+")
       p3.confirmButton.bind("<Button>",update_info, add="+")
       p4.confirmButton.bind("<Button>",update_info, add="+")
       info.pack(side="top")

       b1.pack(side="left")
       b2.pack(side="left")
       b3.pack(side="left")
       b4.pack(side="left")

       p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

       self.lightVal = 50
       def update():
           self.lightVal = self.p3.lightValue
           self.tempVal = self.p1.tempValue
           self.humidityVal = self.p4.humidityValue
           
           print "hi"+str(self.lightVal)
           print "hi"+str(self.tempVal)
           print "hi"+str(self.humidityVal)

           self.after(3000,update)
       update()
