[General]
SyntaxVersion=2
BeginHotkey=121
BeginHotkeyMod=0
PauseHotkey=122
PauseHotkeyMod=0
StopHotkey=123
StopHotkeyMod=0
RunOnce=0
EnableWindow=
MacroID=1d1e1378-f7c3-46ad-ae73-a78630780a60
Description=LOL全自动挂机脚本4.3.2
Enable=1
AutoRun=0
[Repeat]
Type=1
Number=1
[SetupUI]
Type=2
QUI=
[Relative]
SetupOCXFile=
[Comment]

[Script]
/**
@author Han Yue bai
@Date 2021/12/7 - 22:38
@since 4.3.2

【功能说明】 
此脚本只适用于英雄联盟入门人机全自动挂机 
具体教程请看群文件

【热键说明】 
F10（启用脚本） 
F11（暂停脚本） 
F12（关闭脚本）


【设置说明】 
1.系统缩放与布局设置为：100%（系统默认125%）
2.系统分辨率设置为：1920*1080
3.打开在桌面模式下自动隐藏任务栏
4.英雄联盟客户端窗口尺寸设置为1920*1080
5.英雄联盟游戏内部窗口设置为：无边框
6.设置P为快捷攻击型移动
7.玩家移动点击设置2为：L

【使用说明】 
具体请看群文件教学
1.使用时打开LOL入门人机开始匹配界面，即可按下F10开启脚本。
2.需要暂停进行其他操作时点击F11
3.结束脚本按F12（尽量游戏结束，避免逃跑）


【注意事项】 
1.运行脚本时尽量开启键盘大写
2.注意LOL客户端和电脑屏幕重合，不要进行拖拽。
3.电脑桌面尽量不显示桌面图标
4.注意脚本勾选（只勾选需要启动的脚本）
5.一定要注意分辨率设置好在启动，不然容易出现乱点的情况。

*/

//F2视角循环
For 14
//------------------------F2视角------------------------
//寻找对局
MoveTo 907, 1028
Delay 100
LeftClick 1
Delay 100

//接受对局
MoveTo 960, 851
Delay 100
LeftClick 1
Delay 100

//赞誉一名队友
MoveTo 959, 985
Delay 100
LeftClick 1
Delay 100

//升级
MoveTo 1035, 1018
Delay 100
LeftClick 1
Delay 100
LeftClick 1

//寻找英雄（第二排最后一个）
Delay 100
MoveTo 1355, 381
Delay 100
LeftClick 1
Delay 300
LeftClick 1
Delay 200
//点击联盟英雄窗口按下空格下翻英雄窗口
MoveTo 1403, 665
Delay 100
LeftClick 1
Delay 100
KeyPress "Space", 1
Delay 100
//寻找英雄（第三排最后一个）
MoveTo 1366, 563
Delay 100
LeftClick 1
Delay 300

//锁定英雄
MoveTo 852, 918
Delay 100
LeftClick 1
Delay 500
LeftClick 1

//移动鼠标至中心点
Delay 100
MoveTo 1045, 549
Delay 100
//———角色移动———
KeyDown "F2", 1
Delay 100
KeyPress "P", 1
Delay 1000
KeyPress "L", 1
Delay 500
KeyUp "F2", 1
//———角色移动———

//接受对局
MoveTo 960, 851
Delay 100
LeftClick 1
Delay 100

//DF+眼+学习技能+使用技能
KeyDown "Ctrl", 1
KeyPress "R", 1
KeyPress "Q", 1
KeyPress "W", 1
KeyPress "E", 1
KeyUp "Ctrl", 1
Delay 100
KeyPress "4", 1
Delay 100
KeyPress "D", 1
KeyPress "F", 1
Delay 100
KeyPress "R", 1
KeyPress "E", 1
KeyPress "Q", 1
KeyPress "W", 1

//移动鼠标至中心点
MoveTo 938, 581
Delay 100
MoveTo 1045, 549

//———角色移动———
KeyDown "F2", 1
Delay 100
KeyPress "P", 1
Delay 1000
KeyPress "L", 1
Delay 500
KeyUp "F2", 1
//———角色移动———

//移动鼠标至中心点
Delay 100
MoveTo 1045, 549
Delay 100

//———角色移动———
KeyDown "F2", 1
Delay 100
KeyPress "P", 1
Delay 500
KeyPress "L", 1
Delay 100
KeyUp "F2", 1
//———角色移动———
//------------------------F2视角------------------------
Next

//检测是否需要重新连接
FindColor 856,533,861,546,"388DB6",intX,intY
If intX > 0 And intY > 0 Then 
MoveTo 845, 539
Delay 100
LeftClick 1
Delay 100
End If

//使用表情
Delay 100
KeyPress "T", 1
Delay 100

//F3视角循环
For 14
//------------------------F3视角------------------------
//寻找对局
MoveTo 907, 1028
Delay 100
LeftClick 1
Delay 100

//接受对局
MoveTo 960, 851
Delay 100
LeftClick 1
Delay 100

//赞誉一名队友
MoveTo 959, 985
Delay 100
LeftClick 1
Delay 100

//升级
MoveTo 1035, 1018
Delay 100
LeftClick 1
Delay 100
LeftClick 1

//寻找英雄（第二排最后一个）
Delay 100
MoveTo 1355, 381
Delay 100
LeftClick 1
Delay 300
LeftClick 1
Delay 200
//点击联盟英雄窗口按下空格下翻英雄窗口
MoveTo 1403, 665
Delay 100
LeftClick 1
Delay 100
KeyPress "Space", 1
Delay 100
//寻找英雄（第三排最后一个）
MoveTo 1366, 563
Delay 100
LeftClick 1
Delay 300

//锁定英雄
MoveTo 852, 918
Delay 100
LeftClick 1
Delay 500
LeftClick 1

//移动鼠标至中心点
Delay 100
MoveTo 1045, 549
Delay 100
//———角色移动———
KeyDown "F3", 1
Delay 100
KeyPress "P", 1
Delay 1000
KeyPress "L", 1
Delay 500
KeyUp "F3", 1
//———角色移动———

//接受对局
MoveTo 960, 851
Delay 100
LeftClick 1
Delay 100

//DF+眼+学习技能+使用技能
KeyDown "Ctrl", 1
KeyPress "R", 1
KeyPress "Q", 1
KeyPress "W", 1
KeyPress "E", 1
KeyUp "Ctrl", 1
Delay 100
KeyPress "4", 1
Delay 100
KeyPress "D", 1
KeyPress "F", 1
Delay 100
KeyPress "R", 1
KeyPress "E", 1
KeyPress "Q", 1
KeyPress "W", 1

//移动鼠标至中心点
MoveTo 938, 581
Delay 100
MoveTo 1045, 549

//———角色移动———
KeyDown "F3", 1
Delay 100
KeyPress "P", 1
Delay 1000
KeyPress "L", 1
Delay 500
KeyUp "F3", 1
//———角色移动———

//移动鼠标至中心点
Delay 100
MoveTo 1045, 549
Delay 100

//———角色移动———
KeyDown "F3", 1
Delay 100
KeyPress "P", 1
Delay 500
KeyPress "L", 1
Delay 100
KeyUp "F3", 1
//———角色移动———
//------------------------F3视角------------------------
Next

//检测是否需要重新连接
FindColor 856,533,861,546,"388DB6",intX,intY
If intX > 0 And intY > 0 Then 
MoveTo 845, 539
Delay 100
LeftClick 1
Delay 100
End If

//使用表情
Delay 100
KeyPress "T", 1
Delay 100

//F4视角循环
For 14
//------------------------F4视角------------------------
//寻找对局
MoveTo 907, 1028
Delay 100
LeftClick 1
Delay 100

//接受对局
MoveTo 960, 851
Delay 100
LeftClick 1
Delay 100

//赞誉一名队友
MoveTo 959, 985
Delay 100
LeftClick 1
Delay 100

//升级
MoveTo 1035, 1018
Delay 100
LeftClick 1
Delay 100
LeftClick 1

//寻找英雄（第二排最后一个）
Delay 100
MoveTo 1355, 381
Delay 100
LeftClick 1
Delay 300
LeftClick 1
Delay 200
//点击联盟英雄窗口按下空格下翻英雄窗口
MoveTo 1403, 665
Delay 100
LeftClick 1
Delay 100
KeyPress "Space", 1
Delay 100
//寻找英雄（第三排最后一个）
MoveTo 1366, 563
Delay 100
LeftClick 1
Delay 300

//锁定英雄
MoveTo 852, 918
Delay 100
LeftClick 1
Delay 600
LeftClick 1

//移动鼠标至中心点
Delay 100
MoveTo 1045, 549
Delay 100
//———角色移动———
KeyDown "F4", 1
Delay 100
KeyPress "P", 1
Delay 1000
KeyPress "L", 1
Delay 500
KeyUp "F4", 1
//———角色移动———

//接受对局
MoveTo 960, 851
Delay 100
LeftClick 1
Delay 100

//DF+眼+学习技能+使用技能
KeyDown "Ctrl", 1
KeyPress "R", 1
KeyPress "Q", 1
KeyPress "W", 1
KeyPress "E", 1
KeyUp "Ctrl", 1
Delay 100
KeyPress "4", 1
Delay 100
KeyPress "D", 1
KeyPress "F", 1
Delay 100
KeyPress "R", 1
KeyPress "E", 1
KeyPress "Q", 1
KeyPress "W", 1

//移动鼠标至中心点
MoveTo 938, 581
Delay 100
MoveTo 1045, 549

//———角色移动———
KeyDown "F4", 1
Delay 100
KeyPress "P", 1
Delay 1000
KeyPress "L", 1
Delay 500
KeyUp "F4", 1
//———角色移动———

//移动鼠标至中心点
Delay 100
MoveTo 1045, 549
Delay 100

//———角色移动———
KeyDown "F4", 1
Delay 100
KeyPress "P", 1
Delay 500
KeyPress "L", 1
Delay 100
KeyUp "F4", 1
//———角色移动———
//------------------------F4视角------------------------
Next

//检测是否需要重新连接
FindColor 856,533,861,546,"388DB6",intX,intY
If intX > 0 And intY > 0 Then 
MoveTo 845, 539
Delay 100
LeftClick 1
Delay 100
End If

//使用表情
Delay 100
KeyPress "T", 1
Delay 100

//F5视角循环
For 14
//------------------------F5视角------------------------
//寻找对局
MoveTo 907, 1028
Delay 100
LeftClick 1
Delay 100

//接受对局
MoveTo 960, 851
Delay 100
LeftClick 1
Delay 100

//赞誉一名队友
MoveTo 959, 985
Delay 100
LeftClick 1
Delay 100

//升级
MoveTo 1035, 1018
Delay 100
LeftClick 1
Delay 100
LeftClick 1

//寻找英雄（第二排最后一个）
Delay 100
MoveTo 1355, 381
Delay 100
LeftClick 1
Delay 300
LeftClick 1
Delay 200
//点击联盟英雄窗口按下空格下翻英雄窗口
MoveTo 1403, 665
Delay 100
LeftClick 1
Delay 100
KeyPress "Space", 1
Delay 100
//寻找英雄（第三排最后一个）
MoveTo 1366, 563
Delay 100
LeftClick 1
Delay 300

//锁定英雄
MoveTo 852, 918
Delay 100
LeftClick 1
Delay 500
LeftClick 1

//移动鼠标至中心点
Delay 100
MoveTo 1045, 549
Delay 100
//———角色移动———
KeyDown "F5", 1
Delay 100
KeyPress "P", 1
Delay 1000
KeyPress "L", 1
Delay 500
KeyUp "F5", 1
//———角色移动———

//接受对局
MoveTo 960, 851
Delay 100
LeftClick 1
Delay 100

//DF+眼+学习技能+使用技能
KeyDown "Ctrl", 1
KeyPress "R", 1
KeyPress "Q", 1
KeyPress "W", 1
KeyPress "E", 1
KeyUp "Ctrl", 1
Delay 100
KeyPress "4", 1
Delay 100
KeyPress "D", 1
KeyPress "F", 1
Delay 100
KeyPress "R", 1
KeyPress "E", 1
KeyPress "Q", 1
KeyPress "W", 1

//移动鼠标至中心点
MoveTo 938, 581
Delay 100
MoveTo 1045, 549

//———角色移动———
KeyDown "F5", 1
Delay 100
KeyPress "P", 1
Delay 1000
KeyPress "L", 1
Delay 500
KeyUp "F5", 1
//———角色移动———


//锁定英雄错误取消
Delay 100
MoveTo 992, 582
Delay 100
LeftClick 1
Delay 100

//———角色移动———
KeyDown "F5", 1
Delay 100
KeyPress "P", 1
Delay 500
KeyPress "L", 1
Delay 100
KeyUp "F5", 1
//———角色移动———
//------------------------F5视角------------------------
Next

//检测是否需要重新连接
FindColor 856,533,861,546,"388DB6",intX,intY
If intX > 0 And intY > 0 Then 
MoveTo 845, 539
Delay 100
LeftClick 1
Delay 100
End If

//使用表情
Delay 100
KeyPress "T", 1
Delay 100


