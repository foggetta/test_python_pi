from IOPi import IOPi
import time
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
while True:
    if bus.read_pin(7) == 1:
        count += 1
        print ('button checked ' + str(count) + ' time')
        bus.write_pin(10, 1)
        bus.write_pin(16, 1)
        time.sleep(0.5)
    else:
        print ('button pressed ')
        bus.write_pin(10, 0)
        bus.write_pin(16, 0)
