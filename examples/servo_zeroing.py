from robot_hat import PWM,Servo
from robot_hat.utils import reset_mcu
from time import sleep

reset_mcu()
sleep(0.2)

zeroing_pin = Servo(PWM('P11'))
zeroing_pin.angle(0) 

