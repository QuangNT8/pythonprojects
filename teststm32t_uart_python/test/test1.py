import time
import serial

serialPort = serial.Serial(port = "/dev/ttyUSB0", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

serialString = ""                           # Used to hold data coming over UART

teststring = ""

# line = []

def receiver_rsp():
    out = ''
    while serialPort.inWaiting() > 0:
        c = serialPort.read(1)
        out += c
        if c == '\n':
            print (out)
            return 1

result = ""
while 1:
    input = raw_input(">> ")
    # if input == "blink":
        # print (input + '\r\n')
    if input == 'exit':
        serialPort.close()
        exit()
    else:
        out = ''
        serialPort.write(input + '\r\n')
        waitrsp = 1
        while waitrsp:
            while serialPort.inWaiting() > 0:
                c = serialPort.read(1)
                out += c
                if c == '\n':
                    print (out)
            # if receiver_rsp() == 1:
                    waitrsp = 0
    
serialPort.close()

        