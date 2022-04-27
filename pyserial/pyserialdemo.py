import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM2"
ser.open()
a = "1"
packet = bytearray()
packet.append(173)
packet.append(0x7b)
ser.write(packet)
ser.write(b"\x12")
while True:
    s = ser.read()
    print(s)

# ser.send(b"1")
