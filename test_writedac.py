#!/usr/bin/env python
from ADCDACPi import ADCDACPi
import time
import RPi.GPIO as GPIO
#The ADC DAC Pi uses GPIO pin 22 to control the LDAC pin on the DAC.  For normal operation this pin needs to be kept low.  To do this we will use the RPi.GPIO library to set pin 22 as an output and make it low.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, False)
#Next we will create an instance of the ADCDACPi class, call it adcdac and set a DAC gain of 1.
adcdac = ADCDACPi(1)
while True:
   adcdac.set_dac_voltage(1, 1.5)
   time.sleep(0.5)
   adcdac.set_dac_voltage(1, 0)
   time.sleep(0.5)