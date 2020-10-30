# Sparkmate standard README
![TypeBadge](https://img.shields.io/badge/contributor-Thomas-blue)
![TypeBadge](https://img.shields.io/badge/Type-Embedded-purple)
![TypeBadge](https://img.shields.io/badge/Python-FFD43B?style=&logo=python)
![TypeBadge](https://img.shields.io/badge/C-darkblue?style=&logo=c)
![TypeBadge](https://img.shields.io/badge/Arduino-lightblue?style=&logo=arduino)


##  1. <a name='Tableofcontents'></a>Table of contents


##  2. <a name='Description'></a>Description
This repository aims at giving you the perfect boiler plate for embedded system. It was prompted by the assessment that all embedded system end up using a few of the following elements:
- the need to establish communication (Serial, I2C, SPI)
- simple mechatronic system (relays, servo, DC & stepper motors)
- the need for precise analog readings (ADS 1x15, ADS 1256)
- wireless communication (TCP/UDP via WiFi, BLE, LoRaWAN)

The goal of this boiler plate is to help you create a first prototype quickly, therefore it consists of only 2 libraries, one in C (for Arduino & ESP32) and one in Python (for raspberry pi and linux based devices). The idea being that you install only 1 library and are ready to start testing right away.

Once you are done with you first prototype you can then go dive in those boilerplates and easily cherry pick the only functions you really need to improve performance.

This README will also quickly go through each of those differents elements in order to help you choose between the different development possibilities.


##  3. <a name='Installationinstructions'></a>Installation instructions
The installation instruction differs whether you are using the C library or the python packages. 

**Requirements:** A linux based system or at least a bash shell and:
- python3 and pip3 installed. To check those:
> python3 --version && pip3 --version
- the arduino framework or platform io (we recommend using it with vscode)

###  Installing the python package
1. clone this repository:
> git clone //TODO:
2. copy the folder **python-boilerplate** to your library project folder:
> cp -r embedded/python-boilerplate ~/Projects/YourProject/lib/
3. move to your project folder:
> cd ~/Projects/YourProject/
4. install the package dependencies:
> pip3 -r python-boilerplate/requirements.txt
5. add this import to your .py code:
> from python-boilerplate import *

### Installing the Arduino package
1. clone this repository:
> git clone //TODO:
2. copy the folder **c-boilerplate** to your project library folder root:
> cp -r embedded/c-boilerplate ~/Projects/YourProject/lib/
3. move to your project folder:
> cd ~/Projects/YourProject/
4. add this include to your .c code:
> #include "c-boilerplate.h"




##  10. <a name='License'></a>License
We distribute this software with a MIT licence:

MIT License

Copyright (c) 2020 Sparkmate

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
