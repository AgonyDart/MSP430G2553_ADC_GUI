import serial
from msp430 import util

# Crea una conexión serial
ser = serial.Serial("COM3", 9600)

# Lee los datos del MSP430
data = ser.read()

# Imprime los datos leídos
while True:
    print(util.hexdump(data))
