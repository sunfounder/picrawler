import board
import busio
import adafruit_ssd1306

# Initialize I2C and the OLED display
i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear the display
display.fill(0)  # 0 is black
display.show()

# Define the text lines and their positions
lines = [
    ("Hello, World!", 0, 0),          # Line 1 at (0, 0)
    ("This is line 2", 0, 10),        # Line 2 at (0, 10)
    ("And line 3 here", 0, 20),       # Line 3 at (0, 20)
    ("More text!", 0, 30)             # Line 4 at (0, 30)
]

# Write text to the display
for text, x, y in lines:
    display.text(text, x, y, 1)  # 1 is white

# Update the display
display.show()
