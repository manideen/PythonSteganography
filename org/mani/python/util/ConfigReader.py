import os
from configparser import ConfigParser
from org.mani.python.util import PathUtil

config = ConfigParser()
config_path = os.path.join(PathUtil.get_root_path(), 'config', 'config.properties');
print(f"Config file path: {config_path}")
config.read(config_path)
print(config.sections())
#for getting steganography delimiter from config file
def getSteganographyDelimiter():
    try:
        return config.get('steganography', 'delimiter')
    except Exception as e:
        print(f"An error occurred while retrieving the property [delimiter]: {e}")
        return None

#for getting image mode from config file
def getSteganographyImageMode():
    try:
        return config.get('steganography', 'imgMode')
    except Exception as e:
        print(f"An error occurred while retrieving the property [imgMode]: {e}")
        return None

#for getting timestamp format from config file
def getSteganographyTimeStampFormat():
    try:
        timstmp = config.get('steganography', 'timestampFormat')
        return timstmp
    except Exception as e:
        print(f"An error occurred while retrieving the property [timestampFormat]: {e}")
        return None

#for getting image format from config file
def getSteganographyImageFormat():
    try:
        return config.get('steganography', 'imgFormat')
    except Exception as e:
        print(f"An error occurred while retrieving the property [imgFormat]: {e}")
        return None