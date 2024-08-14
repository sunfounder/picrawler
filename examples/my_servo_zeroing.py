from robot_hat import Servo
from robot_hat.utils import reset_mcu
from time import sleep
from robot_hat import Music, TTS
import board
import busio
import adafruit_ssd1306

# Initialize I2C and the OLED display
i2c = busio.I2C(board.SCL, board.SDA)

# Try to initialize the OLED display
try:
    display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
    oled_present = True
except Exception as e:
    print("OLED display not detected or initialization failed.")
    oled_present = False

# If OLED is present, clear the display
if oled_present:
    display.fill(0)  # 0 is black
    display.show()


# Define the text for resetting legs
reset_message = "Resetting legs..."
display.text(reset_message, 0, 0, 1)  # Display "Resetting legs..." at the top
display.show()

# Reset MCU
reset_mcu()
sleep(0.2)

# Initialize TTS
tts = TTS()

MANUAL = '''
Legs getting reset
'''

if __name__ == '__main__':
    print(MANUAL)
    tts.say("Resetting legs")

    for i in range(12):
        if oled_present:
            # Update the OLED display with the current servo being reset
            display.fill(0)  # Clear the display
            display.text(reset_message, 0, 0, 1)  # Keep the "Resetting legs..." message
            display.text(f"Servo {i} resetting", 0, 20, 1)  # Display which servo is resetting
            display.show()

        print(f"Servo {i} set to zero")
        Servo(i).angle(10)
        sleep(0.1)
        Servo(i).angle(0)
        sleep(0.1)

    # After all servos have been reset, display a message indicating completion
    if oled_present:
        display.fill(0)  # Clear the display
        display.text("Legs reset complete.", 0, 0, 1)
        display.show()

    while True:
        user_input = input("Enter 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        sleep(1)