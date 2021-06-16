import serial 
portno = 'COM1'
rate = 9600
a = serial.Serial(portno,rate)

yn='y'

while(yn=='y'):
    line=a.readline()
    print(line)