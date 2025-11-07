import os
from PIL import Image
from org.mani.python.util import ConfigReader

embeded_image_path = input("Provide the path of Embeded image file:")

def decode_image(image_path):
    pixels = []
    binary_message = ''

    try:
        #Open the embeded image
        img = Image.open(image_path)
        pixels = list(img.getdata())

        for pixel in pixels:
            binary_message += str(pixel[0] & 1)  # Extract LSB from Red channel

        message = ''
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i+8]
            if byte == ConfigReader.getSteganographyDelimiter():  # Check for delimiter
                break
            message += chr(int(byte, 2))
        return message
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return
    except Exception as e:
        print(f"An error occurred while opening the image: {e}")
        return

decodeMessage = decode_image(embeded_image_path);
print("Decoded Message: ", decodeMessage)