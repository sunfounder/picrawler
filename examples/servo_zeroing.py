from robot_hat import PWM,Servo
from robot_hat.utils import reset_mcu
from time import sleep

reset_mcu()
sleep(0.2)

# zeroing_pin = Servo(PWM('P11'))
# zeroing_pin.angle(0) 

if __name__ == '__main__':
    for i in range(12):
        print(f"Servo {i} set to zero")
        Servo(PWM(i)).angle(10)
        sleep(0.1)
        Servo(PWM(i)).angle(0)
        sleep(0.1)
    while True:
        sleep(1)