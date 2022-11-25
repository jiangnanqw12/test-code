import time

from typing import ByteString
import serial
import sys
import glob
import zlib
import binascii
import CRC

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
    listsend=[]
    get_send_list(data_send,listsend)

    ser.write(listsend)
def get_crc():
    s=str(synccode)+str(cmd)+str(des)+str(data1)+str(data2)
    print(s)
    t1=zlib.crc32(bytes(s.encode("utf-8")))
    print(hex(t1))
def crc32mpeg2(buf, crc=0xffffffff):
    for val in buf:
        crc ^= val << 24
        for _ in range(8):
            crc = crc << 1 if (crc & 0x80000000) == 0 else (crc << 1) ^ 0x104c11db7
    return crc
def hex2str(hexdata):
    strData=str(hex(hexdata))
    #print(len(strData))
    if len(strData)==10:
        return strData[2:]
    elif len(strData)<10:
        #print(10*"0")
        return (10-len(strData))*"0"+strData[2:]
def test_case1():
    synccode=0xAD7BC565
    cmd=0x00180100
    des=0x00b00000
    data1=0x037a037c
    data2=0x037e0380
    check=0XA6D5D986
    global ser
    ser=serial.Serial("COM4",57600,timeout=1)
    if ser.is_open!=True:
        print("can't open ")
    str_send=''
    listsend=[]
    send_data(synccode,listsend)
    str_send+=hex2str(synccode)

    send_data(cmd,listsend)
    str_send+=hex2str(cmd)

    send_data(des,listsend)
    str_send+=hex2str(des)

    send_data(data1,listsend)
    str_send+=hex2str(data1)

    send_data(data2,listsend)
    str_send+=hex2str(data2)

    send_data(check,listsend)
    rs=ser.read(20)
    print(rs)
    for i in rs:
        print(hex(i))
    print(str_send)
def send_synccode(send_data_hex):
    str_send=''
    listsend=[]
    send_data(send_data_hex,listsend)
    str_send+=hex2str(send_data_hex)
    return str_send
def generate_cmd(config,cmd_type=0x100):
    data_frame_lenght=4+4+4+config[1]*2+4
    #print(hex(data_frame_lenght)+"0100")
    #cmd=eval(hex(data_frame_lenght)+"0100")
    #print(data_frame_lenght)
    cmd=(data_frame_lenght<<16)+cmd_type
    #print(hex(cmd))
    return cmd,data_frame_lenght
def send_data_hex_in4(send_data_hex):
    str_send=''
    listsend=[]
    send_data(send_data_hex,listsend)
    str_send+=hex2str(send_data_hex)
    return str_send
def generate_des(i,column):
    base1=(pic_num+i)*0x00080000
    base2=base1+column*0x400
    return base2
def generate_send_list(linelist,row,column):
    send_list=[]
    temp=""
    for i in range(row):

        if (i+1)%2==0:
            temp2=eval(linelist[column*config[0]+i])
            send_list.append((temp2<<16)+temp1)
        else:
            temp1=eval(linelist[column*config[0]+i])
    #print(send_list)

    return send_list
def test1():
    data1=123
    data2=12
    data3=(123<<16)+data2
    print(data3)
def hex_data_2_bytes_list(hex_data,data_frame_length):
    list_send=[]
    for i in range(data_frame_length):
        temp=(hex_data>>(data_frame_length*8-(i+1)*8))&0xff
        list_send.append(temp)
    return list_send


def store_data(hex_data_send,data):
    hex_data_send=(hex_data_send<<32)+data
    #print(hex(hex_data_send))
    return hex_data_send
def test_case2():
    global synccode
    synccode=0xAD7BC565
    cmd=0x00180100
    des=0x00b00000
    data1=0x037a037c
    data2=0x037e0380
    check=0XA6D5D986
    calibritionNA=[256,256,132,2,1,"calibritionNA"]
    testcase1=[4,4,3,9,1,"testcase1"]
    print(serial_ports())
    global ser
    ser=serial.Serial("COM4",57600,timeout=1)
    if ser.is_open!=True:
        print("can't open ")
    global str_send
    global listsend
    str_send=""
    listsend=[]
    global config
    config=testcase1

    for i in range(config[2]):
        f= open(config[5]+"/"+str(i+1)+".txt",encoding="utf-8")
        linelist = f.readlines()


        for column in range(config[0]):
            hex_data_send=synccode

            #print(str_send)
            cmd_code,data_frame_length=generate_cmd(config)
            #print(data_frame_length)
            #print(hex(cmd_code),config)
            hex_data_send=store_data(hex_data_send,cmd_code)

            #print(str_send)
            des_code=generate_des(i,column)
            hex_data_send=store_data(hex_data_send,des_code)
            #hex_data_send=(hex_data_send<<32)+des_code
            #print(hex(hex_data_send))
            #print(des_code)
            # str_send_temp=send_data_hex_in4(des_code)
            # str_send+=str_send_temp
            #print(str_send)
            #for row in range(config[1]):
            send_list=generate_send_list(linelist,config[0],column)
            #print(send_list)
            for d in send_list:
                hex_data_send=store_data(hex_data_send,d)

            #print(hex(hex_data_send))
            check_code=crc32mpeg2(binascii.a2b_hex(hex(hex_data_send)[2:]))
            #print(hex(check_code))
            hex_data_send=store_data(hex_data_send,check_code)

            #print(hex(hex_data_send))
            #send_data_hex_in4(s3)
            temp=hex_data_send
            list_send=hex_data_2_bytes_list(hex_data_send,data_frame_length)
            # print(list_send)
            # for d1 in list_send:
            #     print(hex(d1))
            ser.write(list_send)
            rs=ser.read(20)
            print(rs)
            #print(hex(rs[-5]))
            # for i in rs:
            #     print(hex(i))
            #send_data_list()
            # generate_check()
            # send_check()
    #print(0xAD7BC5650018010000B00000037A037C037E0380)
    # s4=binascii.crc32mpeg2(binascii.a2b_hex('AD'))
    # print(hex(s4))
    #s2=zlib.crc32(s4)
    #print(hex(s2))

    # get_crc()

    # print(hex(int((len(str_send)+8)/2)))
    # s3=crc32mpeg2(binascii.a2b_hex('AD7BC5650018010000B00000037A037C037E0380'))
    # print(hex(s3))
    # s3=crc32mpeg2(binascii.a2b_hex(str_send))
    # print(hex(s3))
def chip_erase():
    synccode=0xAD7BC565
    hex_data_send=synccode
    config=[0,0,0,0,1,"chip_erase"]
    # global ser
    # ser=serial.Serial("COM4",57600,timeout=1)
    # if ser.is_open!=True:
    #     print("can't open ")
    cmd_code,data_frame_length=generate_cmd(config,0x0300)
    hex_data_send=store_data(hex_data_send,cmd_code)
    hex_data_send=store_data(hex_data_send,0x0)
    check_code=0x7d731943
    hex_data_send=store_data(hex_data_send,check_code)
    list_send=hex_data_2_bytes_list(hex_data_send,data_frame_length)

    ser.write(list_send)
    rs=ser.read(20)
    if (hex(rs[-5]))!="0xaa":
        for d in list_send:
            print(hex(d))
        print("\n")
        for d in rs:
            print(hex(d))

        raise Exception("flash busy")

    if (hex(rs[-6]))!="0xaa":
        for d in list_send:
            print(hex(d))
        print("\n")
        for d in rs:
            print(hex(d))
        raise Exception("crc32mpeg2 FAILED")
    time.sleep(10)
    rs5=0x55
    counter=0
    while(hex(rs5)!="0xaa"):
        time.sleep(10)
        rs5=get_status()
        counter+=1
        print(counter)
    #print(rs)
def get_status2():
    synccode=0xAD7BC565
    hex_data_send=synccode
    config=[0,0,0,0,1,"get_status"]
    # global ser
    # ser=serial.Serial("COM4",57600,timeout=1)
    # if ser.is_open!=True:
    #     print("can't open ")
    cmd_code,data_frame_length=generate_cmd(config,0x0400)
    hex_data_send=store_data(hex_data_send,cmd_code)
    hex_data_send=store_data(hex_data_send,0x0)
    check_code=0x3cab3b2b
    hex_data_send=store_data(hex_data_send,check_code)
    list_send=hex_data_2_bytes_list(hex_data_send,data_frame_length)


    ser.write(list_send)
    rs=ser.read(20)
    #print(rs)
    for d in rs:
        print(hex(d))
    if (hex(rs[-5]))!="0xaa":
        for d in list_send:
            print(hex(d))
        print("\n")
        for d in rs:
            print(hex(d))

        raise Exception("flash busy")

    if (hex(rs[-6]))!="0xaa":
        for d in list_send:
            print(hex(d))
        print("\n")
        for d in rs:
            print(hex(d))
        raise Exception("crc32mpeg2 FAILED")
def get_status():
    synccode=0xAD7BC565
    hex_data_send=synccode
    config=[0,0,0,0,1,"get_status"]

    cmd_code,data_frame_length=generate_cmd(config,0x0400)
    hex_data_send=store_data(hex_data_send,cmd_code)
    hex_data_send=store_data(hex_data_send,0x0)
    check_code=0x3cab3b2b
    hex_data_send=store_data(hex_data_send,check_code)
    list_send=hex_data_2_bytes_list(hex_data_send,data_frame_length)

    # for d in list_send:
    #     print(hex(d))
    # print("\n")
    ser.write(list_send)
    rs=ser.read(20)
    #print(rs)

    if rs!=b"":
        if (hex(rs[-5]))!="0xaa":
            for d in list_send:
                print(hex(d))
            print("\n")
            for d in rs:
                print(hex(d))
            return rs[-5]
            #raise Exception("flash busy")

        if (hex(rs[-6]))!="0xaa":
            for d in list_send:
                print(hex(d))
            print("\n")
            for d in rs:
                print(hex(d))
            raise Exception("crc32mpeg2 FAILED")
    else:

        time.sleep(1)
        rs=ser.read(20)
        print(rs)
        while rs==b"":
            time.sleep(0.1)
            ser.write(list_send)
            rs=ser.read(20)


    return rs[-5]
def writ_data_4IDB():
    tic = time.perf_counter()

    global synccode
    synccode=0xAD7BC565
    cmd=0x00180100
    des=0x00b00000
    data1=0x037a037c
    data2=0x037e0380
    check=0XA6D5D986
    calibritionNA=[256,256,132,2,1,"calibritionNA"]
    fastAlign=[256,256,24,4,1,"fastAlign"]
    fasZernike=[256,256,46,5,1,"fastZernike"]
    pupil=[256,256,8,6,1,"pupil"]
    testcase1=[4,4,3,9,1,"testcase1"]
    config_list=[calibritionNA,fastAlign,fasZernike,pupil]
    print(serial_ports())
    # global ser
    # ser=serial.Serial("COM4",57600,timeout=1)
    # if ser.is_open!=True:
    #     print("can't open ")
    global str_send
    global listsend
    str_send=""
    listsend=[]
    global config
    #config=testcase1
    for config in config_list:
        print("start to write",config[-1])
        for i in range(config[2]):
            print("start to write",config[-1],":","pic ",i+1,"\n")
            #print("start to wirite %d pic"&(i+1))
            f= open(config[5]+"/"+str(i+1)+".txt",encoding="utf-8")
            linelist = f.readlines()


            for column in range(config[0]):
                print("start to write","pic ",i+1," column ",column+1,"\n")
                hex_data_send=synccode

                #print(str_send)
                cmd_code,data_frame_length=generate_cmd(config)
                #print(data_frame_length)
                #print(hex(cmd_code),config)
                hex_data_send=store_data(hex_data_send,cmd_code)

                #print(str_send)
                des_code=generate_des(i,column)
                hex_data_send=store_data(hex_data_send,des_code)
                #hex_data_send=(hex_data_send<<32)+des_code
                #print(hex(hex_data_send))
                #print(des_code)
                # str_send_temp=send_data_hex_in4(des_code)
                # str_send+=str_send_temp
                #print(str_send)
                #for row in range(config[1]):
                send_list=generate_send_list(linelist,config[0],column)
                #print(send_list)
                for d in send_list:
                    hex_data_send=store_data(hex_data_send,d)

                #print(hex(hex_data_send))
                #check_code=crc32mpeg2(binascii.a2b_hex(hex(hex_data_send)[2:]))
                check_code=CRC.crc32_mpeg2(binascii.a2b_hex(hex(hex_data_send)[2:]))

                #print(hex(check_code))
                hex_data_send=store_data(hex_data_send,check_code)

                #print(hex(hex_data_send))
                #send_data_hex_in4(s3)
                temp=hex_data_send
                list_send=hex_data_2_bytes_list(hex_data_send,data_frame_length)
                # print(list_send)
                # for d1 in list_send:
                #     print(hex(d1))
                rs5=get_status()
                while hex(rs5)!="0xaa":
                    time.sleep(0.1)
                    rs5=get_status()
                ser.write(list_send)

                rs=ser.read(20)
                #print(rs)
                if (hex(rs[-5]))!="0xaa":
                    for d in rs:
                        print(hex(d))

                    raise Exception("flash busy")

                if (hex(rs[-6]))!="0xaa":
                    for d in rs:
                        print(hex(d))
                    raise Exception("crc32mpeg2 FAILED")
        pic_num+=config[2]
    toc = time.perf_counter()
    print(f"time is {toc - tic:0.4f} seconds")
def send_full_data():
    tic = time.perf_counter()
    global synccode
    synccode=0xAD7BC565
    cmd=0x00180100
    des=0x00b00000
    data1=0x037a037c
    data2=0x037e0380
    check=0XA6D5D986
    calibritionNA=[256,256,132,2,1,"calibritionNA"]
    fastAlign=[256,256,24,4,1,"fastAlign"]
    fasZernike=[256,256,46,5,1,"fastZernike"]
    pupil=[256,256,8,6,1,"pupil"]
    testcase1=[4,4,3,9,1,"testcase1"]
    config_list=[calibritionNA,fastAlign,fasZernike,pupil]
    print(serial_ports())
    # global ser
    # ser=serial.Serial("COM4",57600,timeout=1)
    # if ser.is_open!=True:
    #     print("can't open ")
    global str_send
    global listsend
    str_send=""
    listsend=[]
    global config
    #config=testcase1
    counter=0
    for list_send in list_send_total:
        rs5=get_status()
        while hex(rs5)!="0xaa":
            time.sleep(0.1)
            rs5=get_status()
        ser.write(list_send)
        rs=ser.read(20)
        counter+=1
        if counter%256==0:
            print(counter)
        #
        # print(rs)
        if (hex(rs[-5]))!="0xaa":
            for d in rs:
                print(hex(d))

            raise Exception("flash busy")

        if (hex(rs[-6]))!="0xaa":
            for d in rs:
                print(hex(d))
            raise Exception("crc32mpeg2 FAILED")

    toc = time.perf_counter()
    print(f"time is {toc - tic:0.4f} seconds")
def generate_full_data():
    global pic_num
    pic_num=0
    flag_log_hex_data=1
    tic = time.perf_counter()
    global synccode
    synccode=0xAD7BC565
    cmd=0x00180100
    des=0x00b00000
    data1=0x037a037c
    data2=0x037e0380
    check=0XA6D5D986
    calibritionNA=[256,256,132,2,1,"calibritionNA"]
    fastAlign=[256,256,24,4,1,"fastAlign"]
    fasZernike=[256,256,46,5,1,"fastZernike"]
    pupil=[256,256,8,6,1,"pupil"]
    testcase1=[4,4,3,9,1,"testcase1"]
    config_list=[calibritionNA,fastAlign,fasZernike,pupil]
    #print(serial_ports())
    # global ser
    # ser=serial.Serial("COM4",57600,timeout=1)
    # if ser.is_open!=True:
    #     print("can't open ")
    global str_send
    global listsend
    str_send=""
    listsend=[]
    global list_send_total
    list_send_total=[]
    global config
    #config=testcase1
    for config in config_list:
        print("start to generate",config[-1])
        for i in range(config[2]):
            #print("start to generate",config[-1],":","pic ",i+1,"\n")
            #print("start to generate %d pic"&(i+1))
            f= open(config[5]+"/"+str(i+1)+".txt",encoding="utf-8")
            linelist = f.readlines()
            if flag_log_hex_data:
                fhex=open(config[5]+"/"+str(i+1)+"_hex"+".txt","w",encoding="utf-8")
            #fbytes=open(config[5]+"/"+str(i+1)+"_bytes"+".txt","w",encoding="utf-8")

            for column in range(config[0]):
                #print("start to generate","pic ",i+1," column ",column+1,"\n")
                hex_data_send=synccode

                #print(str_send)
                cmd_code,data_frame_length=generate_cmd(config)
                #print(data_frame_length)
                #print(hex(cmd_code),config)
                hex_data_send=store_data(hex_data_send,cmd_code)

                #print(str_send)
                des_code=generate_des(i,column)
                hex_data_send=store_data(hex_data_send,des_code)
                #hex_data_send=(hex_data_send<<32)+des_code
                #print(hex(hex_data_send))
                #print(des_code)
                # str_send_temp=send_data_hex_in4(des_code)
                # str_send+=str_send_temp
                #print(str_send)
                #for row in range(config[1]):
                send_list=generate_send_list(linelist,config[0],column)
                #print(send_list)
                for d in send_list:
                    hex_data_send=store_data(hex_data_send,d)

                #print(hex(hex_data_send))
                #check_code=crc32mpeg2(binascii.a2b_hex(hex(hex_data_send)[2:]))
                check_code=CRC.crc32_mpeg2(binascii.a2b_hex(hex(hex_data_send)[2:]))

                #print(hex(check_code))
                hex_data_send=store_data(hex_data_send,check_code)
                #print(hex_data_send)
                if flag_log_hex_data:
                    fhex.write(hex(hex_data_send))
                    fhex.write("\n")
                #print(hex(hex_data_send))
                #send_data_hex_in4(s3)
                temp=hex_data_send
                list_send=hex_data_2_bytes_list(hex_data_send,data_frame_length)
                list_send_total.append(list_send)


                # print(list_send)

                # for d1 in list_send:
                #     fbytes.write(str(d1))
                #     if d1!=list_send[-1]:
                #         fbytes.write(" ")
                # fbytes.write("\n")


                    #print(hex(d1))
                # rs5=get_status()
                # while hex(rs5)!="0xaa":
                #     time.sleep(0.1)
                #     rs5=get_status()
                # ser.write(list_send)

                # rs=ser.read(20)
                # #print(rs)
                # if (hex(rs[-5]))!="0xaa":
                #     for d in rs:
                #         print(hex(d))

                #     raise Exception("flash busy")

                # if (hex(rs[-6]))!="0xaa":
                #     for d in rs:
                #         print(hex(d))
                #     raise Exception("crc32mpeg2 FAILED")
        pic_num+=config[2]
    toc = time.perf_counter()
    print(f"time is {toc - tic:0.4f} seconds")
def open_port(port_num="COM4",Baud_rate=57600):
    print(serial_ports())
    global ser
    ser=serial.Serial(port_num,Baud_rate,timeout=0.03)
    if ser.is_open!=True:
        print("can't open ")
if __name__ == '__main__':
    open_port(port_num="COM4",Baud_rate=1000000)
    #test1()

    #test_case1()

    chip_erase()
    #writ_data_4IDB()
    generate_full_data()
    send_full_data()
