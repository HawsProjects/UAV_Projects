import pigpio
import time

servo = 18
 
pwm = pigpio.pi() 
pwm.set_mode(servo, pigpio.OUTPUT)
 
pwm.set_PWM_frequency(servo, 50)
pwm.set_PWM_range(servo, 20000) # 1,000,000 / 50 = 20,000us for 100% duty cycle