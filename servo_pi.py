import pigpio
import time

servo = 18
 
pwm = pigpio.pi() 
pwm.set_mode(servo, pigpio.OUTPUT)

pwm.set_PWM_frequency(servo, 100)
pwm.set_PWM_range(servo, 2000) # 1,000,000 / 50 = 20,000us for 100% duty cycle