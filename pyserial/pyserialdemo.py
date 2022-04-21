import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM2"
ser.open()
a = 12345
ser.write(a)
