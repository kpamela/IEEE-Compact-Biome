import Tkinter as tk
from Page import *
'''
import RPi.GPIO as GPIO
'''
class QuickStats(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="IEEE BIOME")
       label.pack(side="top", fill="both", expand=True)
