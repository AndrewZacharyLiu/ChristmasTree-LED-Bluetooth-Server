# ChristmasTree-LED-Bluetooth-Server

Personal project over winter break. Uses an Arduino UNO, HC-05 Bluetooth Module, and RGB individually serializable LEDs strip. This Django project starts up a webserver with bluetooth connection to the arduino. This allows anyone to connect to the webserver to control the color, gradient, and animation of the LED strips. 

# Description of files
HC05_CONFIGURATOR_ATCOMMANDS copy.ino - arduino script to compile and upload  
on.py - initialize communication with the arduino, where you can type in commands in terminal to transmit to arduino.   
ledwebserver - folder containing basic django webserver  
# Notes
Due to the limited amount of memory on the arduino uno, the script is limited in the amount of LED lights it can control. The bluetooth connection is over the serial port "/dev/cu.DSDTECHHC-05", which could be named differently depending on the hc-05 module and manfacturer. This was ran on a Mac. The naming scheme of serial ports also likely differ for Windows. 
