import RPi.GPIO as GPIO

import time

from tkinter import *

master = Tk()
master.geometry("175x175")

radios = {"Red" : "1",
          "Green" : "2",
          "Blue" : "3"}


GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

GPIO.setup(16, GPIO.OUT)

GPIO.setup(18, GPIO.OUT)


v = StringVar(master, "1")

def end():
    master.quit()
    master.destroy
    GPIO.cleanup()
    exit()


def setLight():
    print(v.get())
    if (v.get() == "1"):
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
    elif (v.get() == "2"):
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
    elif (v.get() == "3"):
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)


Label(master, text="Choose a light to enable:",
         justify = LEFT,
         padx = 20).pack()

for (text, value) in radios.items():
    Radiobutton(master, text = text, variable = v,
        value = value).pack(side = TOP, ipady = 3)

Button(master, text="Send Command", command = setLight).pack()
Button(master, text="Exit Program", command = end).pack()


mainloop()
