import Tkinter as tk
import datetime
import time
from time import gmtime, strftime


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
    def show(self):
        self.lift()

class QuickStats(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)

class Kill(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This isbpage 3")
       #label.pack(side="top", fill="both", expand=True)

       B1 = tk.Button(self,
                       text="Component1",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0)
       B2 = tk.Button(self,
                       text="Component 2",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0)
       B3 = tk.Button(self,
                       text="Component 3",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0)
       B4 = tk.Button(self,
                       text="Component 4",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0)
       B5 = tk.Button(self,
                       text="Component 3",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0)
       B6  = tk.Button(self,
                       text="Component 4",
                       bg='#f18973',
                       width=30,
                       height=1,
                       font=(None, 12),
                       borderwidth=0)
       B1.grid(row=0, column=0)
       B2.grid(row=0, column=1)
       B3.grid(row=0, column=2)
       B4.grid(row=1, column=0)
       B5.grid(row=1, column=1)
       B6.grid(row=1, column=2)
class Override(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

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
       cycleScale.set(25)                                       #Sets humidity values to 25%
       lightScale.set(25)                                       #Sets humidity values to 25%

       T1.grid(row=0, column=2)
       T2.grid(row=1, column=2)
       T3.grid(row=2, column=2)
       T4.grid(row=3, column=2)
       
       

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

        #------------------Time----------------------------
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
        
        #------------LeftStats------------------------

        
        #------------RightStats-----------------------
        
if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    root.wm_title("Biome")
    root.tk_setPalette(background='#383A3A') 
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x500")
    root.mainloop()
