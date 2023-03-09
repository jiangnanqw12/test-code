import ctypes
class ZAUXNrapper
    def init (self):
        self. handle_ctypes. c_void_p()
        self. sys_ip = ""
        self. sys_info=""
        self. is_connected = False
def search( self, console=[]):
    iplist =ctypes.create_string_buffer (b"",1024)#create string buffer 创建的是一个ANSI标准的C类型字符串
    zauxdll.ZAux_SearchEth(ctypes.byref(iplist) ,1024,200)
    s= iplist.value.decode()
    str_iplist=s.split()
    num len( str iplist)print( num, Controller( s) Found: "
    print( * str iplist, seps'\n')
    console. append(Searching...)
    console. append( str( num) t Controller( s) Found:
    return str iplist, num
def connect( self, ip, console=)
    if self. handle. value is not None:
    self. disconnect(
    ip bytes ip. encode('utf-8)
    p_ ip ctypes. _ char_ p( ip bytes)
    print( Connecting to" , ip,"...")
    ret zauxdl1. ZAux Openeth (p ip, ctypes. pointer( self. handle))
    msg = connected"
    if ret 20:
    msg = ip t connected
    self. sys ip = ip