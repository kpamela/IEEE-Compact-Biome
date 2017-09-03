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

#Settings are for BCM(so GPIO1, GPIO 2, etc. NOT the pins
p_led       =  24


p_solenoid1 =  19
p_solenoid2 =  16
p_solenoid3 =  26 
p_solenoid4 =  20
p_solenoid5 =  21

p_nichrome  =  12
p_peltier   =  6

p_fan1      =  25
p_fan2      =  5




class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = QuickStats(self)
        p2 = Kill(self)
        p3 = Override(self)
        p4 = Settings(self)
        buttonframe = tk.Frame(self)
        statsFrame= tk.Frame(self)
        container =tk.Frame(self)
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
                       width=22,
                       height=1,
                       font=(None, 15),
                       borderwidth=0,
                       command=p1.lift)
        b2 = tk.Button(buttonframe,
                       text="Kill",
                       bg='#f18973',
                       width=22,
                       height=1,
                       font=(None, 15),
                       borderwidth=0,
                       command=p2.lift)
        b3 = tk.Button(buttonframe,
                       text="Override",
                       bg='#f4e1d2',
                       width=22,
                       height=1,
                       font=(None, 15),
                       borderwidth=0,
                       command=p3.lift)
        b4 = tk.Button(buttonframe,
                       text="Settings",
                       bg='#b2b2b2',
                       width=22,
                       height=1,
                       font=(None, 15),
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

        #---------------Collect all settings--------------
        self.lightIntensity = p4.lightVal
        def update_settings():
            self.lightIntensity= p4.lightVal
            self.tempSetting = p4.tempVal
            print self.lightIntensity
            print self.tempSetting
            self.after(3000, update_settings)
        update_settings()

        #------------Collect all current measurements--------

        #-----------Initialize with collected settings------
        '''
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(p_led, GPIO.OUT)
        GPIO.setup(p_solenoid1,GPIO.OUT)
        GPIO.setup(p_solenoid2,GPIO.OUT)
        GPIO.setup(p_solenoid3,GPIO.OUT)
        GPIO.setup(p_solenoid4,GPIO.OUT)
        GPIO.setup(p_solenoid5,GPIO.OUT)

        light_pwm = GPIO.PWM(p_led, 100)
        light_pwm.start(self.lightIntensity)

        def refresh_pins():
            #_______Temperature
            if(currentTemp > tempSetting):
                GPIO.output(p_nichrome, GPIO.HIGH)

            elif(currentTemp < tempSetting):
                GPIO.output(p_nichrome, GPIO.HIGH)
            else:
                GPIO.output(p_fan1, GPIO.HIGH)

            #_______Light settings
            p.ChangeDutyCycle(self.lightIntensity)
            self.after(3000, refresh_pins)
        refresh_pins
        '''
if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    root.wm_title("Biome")
    root.tk_setPalette(background='#383A3A') 
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x500")
    root.mainloop()
