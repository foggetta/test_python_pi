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
bus.set_port_direction(0, 0xFF)
bus.set_port_direction(1, 0x00)
bus.write_pin(16, 1)
bus.write_pin(16, 0)
bus.write_pin(10, 0)
bus.write_pin(10, 1)

bus.write_pin(10, 0)
bus.set_pin_pullup(8,  1)
bus.set_pin_pullup(9,  1)
bus.invert_pin(9,  0)
bus.invert_pin(8,  0)
count = 0
dc = 0
while True:
    if bus.read_pin(7) == 1:
        count += 1
        print ('button checked ' + str(count) + ' time')
        for i in range(9,13):
            bus.write_pin(i,1)
            sleep(0.1)
        bus.write_pin(16,1)
        dc =0
        sleep(0.5)
    else:
        print ('button pressed ')
        print('Volt1=' + str(adcdac.read_adc_voltage(1,  0)) + 'Volt2=' + str(adcdac.read_adc_voltage(2, 0))  + 'ciao '+str(dc))
        pwm.set_pwm(1, 4095-dc, dc)
        for i in range(9,13):
            bus.write_pin(i,0)
        bus.write_pin(16,0)
        dc += 10
        sleep(0.1)
	 
