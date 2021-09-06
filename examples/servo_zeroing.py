from robot_hat import PWM
from robot_hat import Servo

zeroing_pin = Servo(PWM('P11'))

zeroing_pin.angle(0) 

