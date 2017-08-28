
import Tkinter as tk
import datetime
import time
from time import gmtime, strftime
from Page import *
from Settings import *
from Kill import *
from Override import *
from QuickStats import *
from config import *


p_LED       = 18
p_Fan1      = 22
p_Fan2      = 29
p_Peltier   = 31
p_Nichrome  = 32
p_WaterPump = 33
p_Solenoid1 = 35
p_Solenoid2 = 36
p_Solenoid3 = 37
p_Solenoid4 = 38
p_Solenoid5 = 40


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = QuickStats(self)
        p2 = Kill(self)
        p3 = Override(self)
        p4 = Settings(self)
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        statsFrame= tk.Frame(self)
        statsFrame.pack(side="top", fill="x", expand=False)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #--------------MENU BAR-----------------------
        b1 = tk.Button(buttonframe,
                       text="QuickStats",
                       bg='#bc5a45',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0,
                       command=p1.lift)
        b2 = tk.Button(buttonframe,
                       text="Kill",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0,
                       command=p2.lift)
        b3 = tk.Button(buttonframe,
                       text="Override",
                       bg='#f4e1d2',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0,
                       command=p3.lift)
        b4 = tk.Button(buttonframe,
                       text="Settings",
                       bg='#b2b2b2',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0,
                       command=p4.lift)
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
     
        p1.show()

        #------------------QUICK STATS----------------------------
        #------------LeftStats------------------------
        T = tk.Text(statsFrame, height= 4, width=50, borderwidth=0)
        T.insert(tk.END, "T: \n"+ "H: \n"+ "Water:") 
        T.pack(side="left")
        #------------RightStats------------------------
        T = tk.Text(statsFrame, height= 4, width=50, borderwidth=0)
        T.pack(side="right")

        #-----------------Time----------------------------
        sysTime = ''
        clock = tk.Label(statsFrame, font=( None,30,'bold'))
        clock.pack(side="top")
        def updateTime():
            global sysTime
            sysTime = time.strftime('%H:%M:%S')
            clock.config(text=sysTime)
            clock.after(400, updateTime)
        updateTime()

        #---------------Date------------------------

        sysDate = ''
        date = tk.Label(statsFrame, font=( None,10,'bold'))
        date.pack(side="top")
        def updateDate():
            global sysTime
            sysTime = time.strftime('%d/%m/%y')
            date.config(text=sysTime)
            date.after(400, updateDate)
        updateDate()
        

 
if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    root.wm_title("Biome")
    root.tk_setPalette(background='#383A3A') 
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x500")
    root.mainloop()
