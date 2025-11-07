import os
import configparser
from PIL import Image
from datetime import datetime
from org.mani.python.util import ConfigReader

image_path = input("Provide the Image file path:")
message = input("Provide the message needs to be hidden in above image:")
timestmp = datetime.now();
timestmpstr = timestmp.strftime(ConfigReader.getSteganographyTimeStampFormat());
timestmpstr = timestmpstr[:-3]
fileName, extn = os.path.splitext(os.path.basename(image_path))
destination_file = os.path.dirname(image_path) + os.sep + fileName + "_" + timestmpstr + extn;

def encode_image(image_path, message, output_path):
    imgMode = ConfigReader.getSteganographyImageMode();
    print("image mode:",imgMode)
    try:
        #Open the input image
        img = Image.open(image_path)
        if img.mode != imgMode:
            img = img.convert(imgMode);
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return
    except Exception as e:
        print(f"An error occurred while opening the image: {e}")
        return
    #Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += ConfigReader.getSteganographyDelimiter()  # Delimiter to indicate end of message
    #Get the image pixels
    pixels = list(img.getdata())
    #Check if the image can hold the message
    if len(binary_message) > len(pixels) * 3:
        raise ValueError("Error: The message is too long to be hidden in this image.")

    # Embed the binary message into the image pixels
    new_pixels = []
    message_index = 0
    for pixel in pixels:
        if message_index < len(binary_message):
            #Modify the least significant bit of each color channel
            new_pixel = (
                pixel[0] & ~1 | int(binary_message[message_index]),
                pixel[1],
                pixel[2]
            )
            message_index += 1
        else:
            new_pixel = pixel
        new_pixels.append(new_pixel)
    #Update the image with the new pixels
    img.putdata(new_pixels)
    try:
        #Save the modified image
        img.save(output_path, format=ConfigReader.getSteganographyImageFormat())
        print(f"Message successfully encoded into {output_path}")
    except Exception as e:
        print(f"An error occurred while saving the image: {e}")

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

#Encode the message into the image
encode_image(image_path, message, destination_file);
decodeMessage = decode_image(destination_file);
print("Decoded Message: ", decodeMessage);