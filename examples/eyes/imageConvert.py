import board
import busio
import adafruit_ssd1306
from PIL import Image
import time

# Initialize I2C and the OLED display
i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

def load_and_convert_image(image_path, display_width=128, display_height=64):
    """
    Load an image file, convert it to monochrome, handle transparency, and resize it to fit the display.
    Returns the processed image.
    """
    try:
        # Open the image
        img = Image.open(image_path)

        # Convert transparency to black
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            img = img.convert('RGBA')
            background = Image.new('RGBA', img.size, (0, 0, 0))
            background.paste(img, (0, 0), img)
            img = background.convert('1')  # Convert to monochrome
        else:
            img = img.convert('1')

        # Resize the image to fit the OLED display
        img = img.resize((display_width, display_height))

        return img
    except Exception as e:
        print(f"Error loading or processing image: {e}")
        return None

def display_images(image_paths, cycles=3, delay=0.5):
    """
    Cycle through a list of image paths and display each one on the OLED screen.
    Repeats the cycle a specified number of times.
    """
    for _ in range(cycles):
        for path in image_paths:
            image = load_and_convert_image(path)
            if image:
                # Clear the display
                display.fill(0)
                display.show()

                # Display the image
                display.image(image)
                display.show()

                # Wait before displaying the next image
                time.sleep(delay)
            else:
                print(f"Error displaying image: {path}")

# List of image file paths
image_paths = ['eye.png', 'eye2.png', 'eye3.png', 'eye4.png']  # Update with your image file paths

# Display images with cycling
display_images(image_paths, cycles=3, delay=0.5)  # Adjust delay as needed
