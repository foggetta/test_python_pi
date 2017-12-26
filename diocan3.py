from IOPi import IOPi
from  ADCDACPi  import  ADCDACPi 

from time import sleep
from ServoPi import PWM
pwm = PWM(0x41)
pwm.set_pwm_freq(1000)
##output_enable()

adcdac  =  ADCDACPi(1)
adcdac.set_adc_refvoltage(3.3)



bus = IOPi(0x20)
bus.set_port_direction(0, 0x00)
bus.set_port_direction(1, 0xF0)
bus.write_port(0, 0)
bus.write_port(1, 0)
sleep(1)
bus.write_pin(9, 1)
sleep(1)

bus.set_pin_pullup(16,  1)
bus.set_pin_pullup(15,  1)
bus.set_pin_pullup(14,  1)
bus.invert_pin(16, 1)
bus.invert_pin(15, 1)
bus.invert_pin(14, 0)
count = 0
dc = 0
while True:
    if bus.read_pin(14) == 1:
        count += 1
        print ('\n\nbutton checked ' + str(count) + ' time')
        for i in range(1,6):
            bus.write_pin(i,1)
            #sleep(0.1)
        print ('Read relais 1=' + str(bus.read_pin(16)) + '\nRead relais 2=' + str(bus.read_pin(15)))
        dc =0
        #sleep(0.5)
    else:
        print ('\n\nbutton pressed ')
        print('Volt1=' + str(adcdac.read_adc_voltage(1,  0)) + 'Volt2=' + str(adcdac.read_adc_voltage(2, 0))  + 'ciao '+str(dc))
        if dc >= 4095:
            dc=0
        else:
            for i in range(1,4):
                pwm.set_pwm(i, dc, 0)
        for i in range(1,6):
            bus.write_pin(i,0)
        print ('Read relais 1=' + str(bus.read_pin(16)) + '\nRead relais 2=' + str(bus.read_pin(15)))
        dc += 10
        #sleep(0.1)
	 
