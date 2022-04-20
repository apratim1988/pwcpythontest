from configparser import ConfigParser
from Utilities.filepath import *

def readConfig(section,key):
    config = ConfigParser()
    config.read(FilePath.configrdr_path)
    return config.get(section,key)