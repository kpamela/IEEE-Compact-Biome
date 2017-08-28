import Tkinter as tk
from Page import *
'''
import RPi.GPIO as GPIO
import dht11
'''
class QuickStats(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="IEEE BIOME")
       label.pack(side="top", fill="both", expand=True)
'''
        # initialize GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

        # read data using pin 14
        instance = dht11.DHT11(pin = 14)
        result = instance.read()

        if result.is_valid():
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
        else:
            print("Error: %d" % result.error_code)
'''
