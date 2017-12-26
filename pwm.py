from ServoPi import PWM
pwm = PWM(0x41)
pwm.set_pwm_freq(1000)
##output_enable()
pwm.set_pwm(1, 0, 110)
