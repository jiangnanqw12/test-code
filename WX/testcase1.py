from wx_sender import WxMsg
from time import sleep

wx = WxMsg()  #实例化对象

wxid = '小号'  #要发送的微信号
wx.search(wxid)  #搜索微信号

# 发送剪贴板内容
wx.send_clipboard()

# 发送1条消息
wx.send_txt('测试单条消息')

# 发送1个文件
wx.send_file(r'C:\Windows\write.exe')

# 发送多个文件，传入[文件路径列表]
sleep(1)
wx.send_file([r'C:\Windows\write.exe', r'C:\Windows\hh.exe'])

# 发送多条文字消息
sleep(1)
for i in range(5):
    wx.send_txt(f'发送第{i+1}条文字消息')
    sleep(1)

#粘贴消息，不发送出去
wx.send_txt('此消息不会发送出去，因为添加了第二参数 False', False)