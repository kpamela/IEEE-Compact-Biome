from Tkinter import *
import random
import datetime
from time import gmtime, strftime
from config import *


root = Tk()

class App(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Biome")
        self.master.tk_setPalette(background='#383A3A')
        Label(self,text="Hi")
##------------------
#
#  Settings
#
##------------------

def settings():
  
    tempScale = Scale(root, from_=0, to=60,
               tickinterval=10,
               orient=HORIZONTAL,
               borderwidth = 0,
               highlightthickness= 0,
               length=400)
    tempScale.set(25)                                        #Sets the default temperature value to 25C
    tempScale.grid( row = 0, column = 1)
    T1 = Label(root, text="Temperature (C)", fg='White')
    
    
    humidityScale = Scale(root, from_=0, to=60,
               tickinterval=10,
               orient=HORIZONTAL,
               borderwidth = 0,
               highlightthickness= 0,
               length=400)
    humidityScale.set(25)                                    #Sets humidity values to 25%          
    humidityScale.grid(row = 1, column = 1)
    T2 = Label(root, text="Humidity (%)", fg='White')
    
    cycleScale = Scale(root, from_=0, to=60,
               tickinterval=10,
               orient=HORIZONTAL,
               borderwidth = 0,
               highlightthickness= 0,
               length=400)
    cycleScale.set(25)                                      #Sets humidity values to 25%          
    cycleScale.grid(row = 2, column = 1)
    T3 = Label(root, text="Cycle", fg='White')
    
    
    lightScale = Scale(root, from_=0, to=100,
               tickinterval=10,
               orient=HORIZONTAL,
               borderwidth = 0,
               highlightthickness= 0,
               length=400)
    lightScale.set(25)                                     #Sets humidity values to 25%          
    lightScale.grid(row = 3, column = 1)
    T4 = Label(root, text="Light Sensitivity", fg='White')

    T1.grid(row=0, column=2)
    T2.grid(row=1, column=2)
    T3.grid(row=2, column=2)
    T4.grid(row=3, column=2)

    

##------------------
#
#  Mini Stats
#
##------------------
num_Of_Buttons = 4
def miniStats():
    T = Text(root,
             height=10,
             width=30,
             borderwidth=0)
    T.insert(END, "Temperature: \n"+
             "Cycle mode: \n" +
             strftime("%Y-%m-%d %H:%M:%S", gmtime())) #Set to the current system time
    T.grid(row=0, rowspan = num_Of_Buttons, column=1)
    
##------------------
#
#  Main landing page
#
##------------------
def mainPage():
    L1 =Button(root,
               text="Stats",
               fg='White',
               bg='#003B46',
               width=10,
               height=1,
               font=(None, 30),
               borderwidth=0)
    L2 = Button(root,
                text="Kill",
                fg='White',
                bg='#07575B',
                width=10,
                height=1,
                font=(None, 30),
                borderwidth=0)
    L3 = Button(root,
                text="Override",
                fg='White',
                bg='#66A5AD',
                width=10,
                height=1,
                font=(None, 30),
                borderwidth=0)
    L4 = Button(root,
                text="Settings",
                fg='White',
                bg='#C4DFE6',
                width=10,
                height=1,
                font=(None, 30),
                borderwidth=0)
    L1.grid(row= 0, column = 0)
    L2.grid(row= 1, column = 0)
    L3.grid(row=2, column = 0)
    L4.grid(row=3, column = 0)
    testButton = Button(root, text="TestButton")

##------------------
#
#  Driver
#
##------------------

pageVar = "Main"
mainPage()
settings()
app= App(root)
app.mainloop()