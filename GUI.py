from Tkinter import *

#------------------------------------------
# Default values
#------------------------------------------

master = Tk()
temperature = 25
feed_cycle  = 0

#Night templates
night_font  = "white"
night_bg    = "black"

#Day template
day_font    = "black"
day_bg      = "white"


#------------------------------------------
# Display information
#------------------------------------------

#------------------------------------------
# Settings
#------------------------------------------

# Set time
def set_time():
    w = Scale(master, from_=0, to=200,
              orient=HORIZONTAL,
              tickinterval=8,
              length=600,
              background="blue")
    w.pack()
    w.set(25)
# Set temperature
def set_temp():
    w = Scale(master, from_=0, to=200,
              orient=HORIZONTAL,
              tickinterval=8,
              length=600,
              background="black",
              fg="white" )
    w.pack()
    w.set(temperature)
set_temp()
set_time()
mainloop()
