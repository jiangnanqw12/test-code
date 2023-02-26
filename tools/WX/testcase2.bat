@echo off & pushd %~dp0

set wxid=小号

::发送文字消息
.\wx_sender.py %wxid% 测试消息


echo 按任意键测试发送文件&pause>nul

::发送文件，在后面加上参数f
.\wx_sender.py %wxid% "C:\Windows\write.exe" f


echo 按任意键测试发送剪贴板&pause>nul

::发送剪贴板内容
.\wx_sender.py %wxid%