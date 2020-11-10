"""@package functions used to handle the communication with user or with the Arduino
"""

import serial
from datetime import datetime
import os
import time


def initSerial(port, baudrate, timeout=1):
    """
    initialize the serial connection (via USB) with the Arduino
    flush the buffer as well, just in case
    """
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        ser.flush()
        return ser
    except:
        print("init Serial: FAILED")
        return None


def readSerial(ser):
    """
    get the next line in the Serial buffer 
    """
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            return line
    except:
        return None

def parseData(datastream, separator=';', beginChar = '<', endChar='>'):
    """
    parse the data from serial and convert it from string to an int array
    by default the data comes with the following shape:
    "<val1,val2,val3,>"
    and therefore:
    parseData("<val1,val2,val3,>") returns [val1, val2, val3]
    """
    dataList = datastream.split(separator)
    result = []
    for i in range(len(dataList)-1):
        if (dataList[i]!= ''):
            data = dataList[i]
            if ((data!='<') or (data!='>')):    
                try:
                    result.append(int(data))
                except:
                    return []
    return(result)


def timestamp(TIMESTAMP_FORMAT= "%m%d_%Hh%M"):
    """
    return a timestamp, used to create directory
    """
    dateStamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    return dateStamp


def createDir(LOG_PATH="log/"):
    """
    create a directory, make sure to not overwrite one
    """
    path=LOG_PATH+timestamp()
    i=0
    try:
        while (os.path.exists(path+'_'+str(i))):
            i += 1
        
        os.mkdir(path+'_'+str(i))
        return path+'_'+str(i)+'/'
    except OSError:
        print ("Creation of the directory %s failed" % path)



def query_yes_no(question, default="yes"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        print(question + prompt)
        choice = input().lower() #python 2: raw_input
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")