#!/usr/bin/env python
from ADCDACPi import ADCDACPi
import time
from math import log10,log
adcdac = ADCDACPi(1) #DAC gain (1 o 2)
adcdac.set_adc_refvoltage(3.3)
Rf = 10000.
c1 = 1.009249522e-03
c2 = 2.378405444e-04
c3 = 2.019202697e-07
V0=4.98

def thermistor_t(V):
     Rt = (V0/V-1)*Rf
     print(Rt)
     logR2 = log(Rt)
     T = (1.0 / (c1 + c2*logR2 + c3*logR2**3))
     T = T - 273.15;
     return T
    
while True:
    Vr=adcdac.read_adc_voltage(2, 0)    
    print("Vr="+str(Vr)+" - temp="+str(thermistor_t(Vr))+"\n")
    
    time.sleep(0.5)
   
