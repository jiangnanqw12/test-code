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
MacroID=92a999f5-4eda-470a-98bf-e305a4dc4e3c
Description=LOL全自动1280X720分辨率1.6
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

//LOL全自动1280X720分辨率1.5
Dim data_hero_str
data_hero_str = Array("f2","f3","f4", "f5")
Dim x, y, coordinate, delay1, delay2, click_num,fx
click_num = 1
delay1 = 100
delay2 = 100

Dim search_match,accept_match,legend_2_last
search_match = Array(601, 685)
accept_match = Array(714, 556)
legend_2_last = Array(910,277)
legend_3_last = Array(913, 373)
invite_others = Array(671, 638)
lock_legend = Array(700, 604)
centre_screen = Array(636, 387)
rematch= Array(518,359)
Function move_and_click(coordinate, click_num, delay1, delay2)
	Delay delay1
	MoveTo coordinate(0), coordinate(1)
	Delay delay1
	LeftClick click_num
	Delay delay2
End Function
Function legend_move(fx)
	KeyDown fx, 1
	Delay 100
	KeyPress "P", 1
	Delay 1000
	KeyPress "L", 1
	Delay 500
	KeyUp fx, 1
End Function
Function learn_get_spell()
	KeyDown "Ctrl", 1
	KeyPress "R", 1
	KeyPress "Q", 1
	KeyPress "W", 1
	KeyPress "E", 1
	KeyUp "Ctrl", 1
	Delay 100
	KeyPress "4", 1
	KeyPress "1", 1
	Delay 100

	KeyPress "D", 1
	KeyPress "F", 1
	Delay 100
	KeyPress "R", 1
	KeyPress "E", 1
	KeyPress "Q", 1
	KeyPress "W", 1
End Function
For Each d In data_hero_str
	For 10

	//寻找对局
	call move_and_click(search_match,1,100,100)
	//接受对局
	Call move_and_click(accept_match, 1, 100, 100)
	//赞誉一名队友
	Call move_and_click(accept_match, 1, 100, 100)
	//升级
	Call move_and_click(accept_match, 1, 100, 100)
	//寻找英雄（第二排最后一个）
	Call move_and_click(legend_2_last, 1, 100, 500)
	Call move_and_click(legend_2_last, 1, 100, 500)
	//（第三排最后一个）
	Call move_and_click(legend_3_last, 1, 100, 100)
	//寻找英雄（第三排最后一个）
	MoveTo 1366, 563
	Delay 100
	LeftClick 1
	Delay 300
	//发送邀请
	Call move_and_click(invite_others, 1, 100, 100)
	//锁定英雄
	Call move_and_click(lock_legend, 1, 100, 500)
	Call move_and_click(lock_legend, 1, 100, 100)

	//移动鼠标至中心点
	Call move_and_click(centre_screen, 1, 100, 100)

	//———角色移动———
	Call legend_move(d)

	//———角色移动———

	//接受对局
	Call move_and_click(accept_match, 1, 100, 100)


	//DF+眼+学习技能+使用技能
	Call learn_get_spell()


	//移动鼠标至中心点
	MoveTo 938, 581
	Delay 100
	MoveTo 1045, 549

	//———角色移动———
	Call legend_move(d)

	//———角色移动———

	//移动鼠标至中心点
	Delay 100
	MoveTo 1045, 549
	Delay 100

	//———角色移动———
	Call legend_move(d)
	//———角色移动———

	Next



//使用表情
Delay 100
KeyPress "T", 1
Delay 100
//重新连接
call move_and_click(rematch,1,100,100)
Delay 30000
Next



