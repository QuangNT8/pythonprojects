import time
import serial

serialPort = serial.Serial(port = "/dev/ttyUSB0", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

serialString = ""                           # Used to hold data coming over UART

teststring = ""

while(1):
     # get keyboard input
    input = raw_input(">> ")
    if input == "quang":
        print ('huong')
    elif input == 'exit':
        serialPort.close()
        exit()
    else:
        serialPort.write(input + '\r\n')
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while serialPort.inWaiting() > 0:
            out += serialPort.read(1)

        if out != '':
            print (">> ") + out