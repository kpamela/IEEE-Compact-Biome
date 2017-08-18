from Tkinter import *
import random
import datetime
from time import gmtime, strftime

root = Tk()

class App(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Biome")
        self.master.tk_setPalette(background='#3b3a30')
        Label(self,text="Hi")
##------------------
#
#  Settings
#
##------------------

def settings():
    
    
    w2 = Scale(root, from_=0, to=60,
               tickinterval=10,
               orient=HORIZONTAL,
               borderwidth = 0,
               highlightthickness= 0)
    w3 = Scale(root, from_=0, to=60,
               tickinterval=10,
               orient=HORIZONTAL,
               borderwidth = 0,
               highlightthickness= 0,
               width = 10,
               length=400)
    w2.set(25)                                        #Sets the default temperature value to 25C
    w2.grid( row = 0, column = 1)
    w3.set(25)
    w3.grid(row = 1, column = 1)
    #w2.pack()

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
                       font=(None, 30))
    L2 = Button(root,
                       text="Kill",
                       fg='White',
                       bg='#07575B',
                       width=10,
                       height=1,
                       font=(None, 30))
    L3 = Button(root,
                       text="Override",
                       fg='White',
                       bg='#66A5AD',
                       width=10,
                       height=1,
                       font=(None, 30))
    L4 = Button(root,
                       text="Settings",
                       fg='White',
                       bg='#C4DFE6',
                       width=10,
                       height=1,
                       font=(None, 30))
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

mainPage()
settings()
app= App(root)
app.mainloop()
