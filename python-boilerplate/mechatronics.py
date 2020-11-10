"""@package functions used to handle the mechatronics
"""

import RPi.GPIO as GPIO #used to interract with the general purpose Input Output pins of the raspberry pi
import time

def changePinState(pin,tension):
    """
    set pin to desired tension (tension must be either GPIO.LOW or GPIO.HIGH)
    """
    GPIO.output(pin,tension)

def relayON(pin):
    # print("turning pin "+str(pin)+" on")
    changePinState(pin,GPIO.LOW)

def relayOFF(pin):
    # print("turning pin "+str(pin)+" off")
    changePinState(pin,GPIO.HIGH)
    time.sleep(0.05)
    changePinState(pin,GPIO.HIGH)

def pinModeSetup(pinArray,mode):
    """
    setup all gpio pins according to pinArray and mode
    example: pinModeSetup(OUTPUT_PIN_ARRAY,GPIO.OUT)
    """
    for i in range(len(pinArray)):
        if (mode == GPIO.OUT):
            GPIO.setup(pinArray[i],mode)
            GPIO.output(pinArray[i],GPIO.HIGH) 
            print("setup pin: ", pinArray[i])
        else:
            GPIO.setup(pinArray[i],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
            print("setup pin: ", pinArray[i])

def millis():
    return int(round(time.time() * 1000))

def readADC(adc, pin, gain):
    return adc.read_adc(pin, gain=gain)