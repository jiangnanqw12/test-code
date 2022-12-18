import pyserial as serial

def open_serial():
    ser = serial.Serial('COM3', 9600, timeout=0.5)
    return ser
def close_serial(ser):
    ser.close()
def read_serial(ser):
    return ser.readline()
#get current screen resolution
def get_screen_resolution():
    return (GetSystemMetrics(0), GetSystemMetrics(1))