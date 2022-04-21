import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM1"
ser.open()
ser.write(b"AD")
