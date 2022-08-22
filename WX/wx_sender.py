from pyperclip import copy, paste
from time import sleep
import ctypes
import pyautogui
import sys
import win32clipboard
import win32con
import win32gui


class DROPFILES(ctypes.Structure):
    _fields_ = [
        ("pFiles", ctypes.c_uint),
        ("x", ctypes.c_long),
        ("y", ctypes.c_long),
        ("fNC", ctypes.c_int),
        ("fWide", ctypes.c_bool),
    ]


def restore_clipboard(func):  #自动还原剪贴板
    def wrapper(*args, **kwargs):
        clip_bak = paste()  # 备份
        result = func(*args, **kwargs)
        copy(clip_bak)  #还原
        return result

    return wrapper


class WxMsg:
    def __handle(self):
        return win32gui.FindWindow('WeChatMainWndForPC', '微信')

    def __pos_and_size(self):
        win_x, win_y, win_right_down_x, win_right_down_y = win32gui.GetWindowRect(
            self.__handle())
        win_width = win_right_down_x - win_x
        win_height = win_right_down_y - win_y
        return win_x, win_y, win_width, win_height

    #复制文件到剪贴板 代码来源：https://www.cnblogs.com/love-DanDan/p/15900159.html
    def __copy_file(self, files):
        pDropFiles = DROPFILES()
        pDropFiles.pFiles = ctypes.sizeof(DROPFILES)
        pDropFiles.fWide = True
        mdata = bytes(pDropFiles)
        files = ("\0".join(files)).replace("/", "\\")
        data = files.encode("U16")[2:] + b"\0\0"
        win32clipboard.OpenClipboard()
        try:
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_HDROP,
                                            mdata + data)
        finally:
            win32clipboard.CloseClipboard()

    #打开窗口  代码来源： 【yuupuu】 [url]https://www.52pojie.cn/thread-1673429-1-1.html[/url]
    def __activate_wx_window(self):
        if handle := self.__handle():
            win_x, win_y, win_width, win_height = self.__pos_and_size()
            win32gui.ShowWindow(handle, win32con.SW_SHOWMINIMIZED)
            win32gui.ShowWindow(handle, win32con.SW_SHOWNORMAL)
            win32gui.ShowWindow(handle, win32con.SW_SHOW)
            win32gui.SetWindowPos(handle, win32con.HWND_TOP, win_x, win_y,
                                  win_width, win_height,
                                  win32con.SWP_SHOWWINDOW)
            win32gui.SetForegroundWindow(handle)
        else:
            print('微信未登录')
            exit()

    #复制文字，并粘贴
    @restore_clipboard
    def __wx_input(self, txt):
        copy(txt)
        pyautogui.hotkey('ctrl', 'v')

    #延时点击坐标
    #默认使用相对坐标点击 (实际点击位置：窗口坐标+相对坐标)
    def __click(self, x, y, timeout=0.25, relative=True):  #默认使用相对坐标点击
        sleep(timeout)
        win_x, win_y = self.__pos_and_size()[:2]
        if relative:
            pyautogui.click(win_x + x, win_y + y)  #使用相对坐标点击
        else:
            pyautogui.click(x, y)

        #把消息发送出去
    def __send_msg_out(self):
        sleep(0.4)
        pyautogui.hotkey('alt', 's')

    #搜索联系人
    def search(self, wxid):
        self.__activate_wx_window()
        self.__click(21, 145)  # 通讯录
        self.__click(143, 39)  # 搜索框
        self.__wx_input(wxid)  # 搜索微信id
        self.__click(155, 120, 0.6)  # 点第一个搜索结果 要多停留一会儿

        #点输入框，从微信窗口右下角:x-50,y-63，使用绝对坐标点击
        win_right_down_x, win_right_down_y = win32gui.GetWindowRect(
            self.__handle())[-2:]  #微信窗口右下角的坐标
        self.__click(win_right_down_x - 50, win_right_down_y - 63, 0.2, False)

    #发送文字消息
    @restore_clipboard
    def send_txt(self, txt, send_out=True):
        copy(txt)  # 粘贴文本内容
        pyautogui.hotkey('ctrl', 'v')  # 粘贴复制的内容
        if send_out:
            self.__send_msg_out()

    #发送文件，传入参数为文件路径
    @restore_clipboard
    def send_file(self, file_list, send_out=True):
        if isinstance(file_list, str):
            file_list = [file_list]
        self.__copy_file(file_list)
        pyautogui.hotkey('ctrl', 'v')  # 粘贴复制的内容
        if send_out:
            self.__send_msg_out()

    #直接发送剪贴板内容
    def send_clipboard(self, send_out=True):
        if paste():
            pyautogui.hotkey('ctrl', 'v')  # 粘贴复制的内容
            if send_out:
                self.__send_msg_out()
        else:
            print('剪贴板为空')
            exit()


if __name__ == '__main__':
    arg_count = len(sys.argv)  #传入的参数个数

    if arg_count not in {1, 2, 3, 4}:
        print('参数个数不是2或3，看看是不是传入了含空格的文件路径')
    else:
        wx = WxMsg()  #实例化对象

        # 3个参数发文件
        if arg_count == 4:  # 传入3个参数（微信id,消息内容，文件路径）
            _, wxid, msg_content, msg_type = sys.argv
            if msg_type.lower() == 'f':
                wx.search(wxid)  #搜索微信号
                wx.send_file(msg_content)  # 发送1个文件
            else:
                print(f'第3参数【{msg_type}】错误，必须是“f”\n可以检查下是不是传入了含空格的文件路径')

        # 2个参数发文字
        elif len(sys.argv) == 3:  # 传入2个参数（微信id,文字消息内容）
            _, wxid, msg_content = sys.argv
            wx.search(wxid)  #搜索微信号
            wx.send_txt(msg_content)

        # 1个参数发剪贴板内容
        elif len(sys.argv) == 2:  # 传入1个参数（微信id）
            _, wxid = sys.argv
            wx.search(wxid)  #搜索微信号
            wx.send_clipboard()

        ################################ 不传入参数，直接在python里运行，可以发送多行文本或者多个文件
        elif arg_count == 1:
            wxid = '小号'  #要发送的微信号
            wx.search(wxid)  #搜索微信号

            # 发送1条消息
            wx.send_txt('测试1条消息')

            # # 发送1个文件
            # wx.send_file(r'C:\Windows\write.exe')

            # # 发送多个文件，传入[文件路径列表]
            # sleep(1)
            # wx.send_file([r'C:\Windows\write.exe', r'C:\Windows\hh.exe'])

            # # 发送多条文字消息
            # sleep(1)
            # for i in range(5):
            #     wx.send_txt(f'发送第{i+1}条文字消息')
            #     sleep(1)

            # #粘贴消息，不发送出去
            # wx.send_txt('此消息不会发送出去，因为添加了第二参数 False', False)