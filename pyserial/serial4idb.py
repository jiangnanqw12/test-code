import time
import serial
import sys
import glob
import zlib
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def send_str(port, baudrate, parity, value):

    port_set = serial.Serial(port=port, baudrate=baudrate, parity=parity)

    port_set.write(value)

    # delay 100ms if receive is blank, just waiting 5s.
    n = 0
    while port_set.inWaiting() == 0:
        time.sleep(0.1)
        n = n + 1
        if n > 50:
            # send frame again
            port_set.write(value)
            break
    # every 100ms check the data receive is ready
    byte_number_1 = 0
    byte_number_2 = 1
    while byte_number_1 != byte_number_2:
        byte_number_1 = port_set.inWaiting()
        time.sleep(0.1)
        byte_number_2 = port_set.inWaiting()

    receive_frame = port_set.read_all()

    return receive_frame

def get_send_list(data_send,listsend):
    if data_send>0xffffffff:
        print("error")
    for i in range(4):
        temp=(data_send>>(32-8*(i+1)))&0xff
        #print("%x"%temp)
        listsend.append(temp)
        #print(listsend)
def send_data(data_send,listsend):
    get_send_list(data_send,listsend)
    ser.write(listsend)
def get_crc():
    s=str(synccode)+str(cmd)+str(des)+str(data1)+str(data2)
    print(s)
    t1=zlib.crc32(bytes(s.encode("utf-8")))
    print(hex(t1))
if __name__ == '__main__':
    synccode=0xAD7BC565
    cmd=0x00180100
    des=0x00b00000
    data1=0x037a037c
    data2=0x037e0380
    check=0XA6D5D986

    print(serial_ports())
    ser=serial.Serial("COM4",57600,timeout=1)
    if ser.is_open!=True:
        print("can't open ")
    listsend=[]
    send_data(synccode,listsend)
    listsend=[]
    send_data(cmd,listsend)
    listsend=[]
    send_data(des,listsend)
    listsend=[]
    send_data(data1,listsend)
    listsend=[]
    send_data(data2,listsend)
    listsend=[]
    send_data(check,listsend)
    rs=ser.read(100)
    print(rs)
    s2=zlib.crc32(b"123")
    print(s2)

    get_crc()
