#Requires AutoHotkey v2.0
; 【修改1】：potplayer程序的路径
potplayer_path := "D:\DevelopmentTools\Softare\WindowsTools\PotPlayer64\PotPlayerMini64.exe"
; 【修改2】生成markdown连接，标题的默认名称
markdown_tittle := "name-->time"

log_toggle := false
open_window_parameter := InitOpenWindowParameter(potplayer_path)

; 【修改3】定义热键 Alt+G
; 热键 - 定义 & 使用 | AutoHotkey v2
; https://wyagd001.github.io/v2/docs/Hotkeys.htm
!g::{
    Potplayer2Obsidian(markdown_tittle)
}

; 【主逻辑】Potplayer的回调函数（回链）
CallbackPotplayer(){
    url := ReceivParameter()
    ParseUrl(url)
}

ReceivParameter(){
    ; 保存脚本为ShowParameters.ahk

    ; 获取命令行参数的数量
    paramCount := A_Args.Length

    ; 如果没有参数，显示提示信息
    if (paramCount = 0) {
        MsgBox "请提供至少一个参数。"
        ExitApp
    }

    ; 循环遍历参数并显示在控制台
    for n, param in A_Args{
        return param
    }
}
ParseUrl(url){
    ;url := "ahk-potplayer://open?type=1&aaa=123&bbb=456"
    url := StrReplace(url, "ahk-potplayer://open?type=1&")

    ; 解析键值对
    url_parameters := StrSplit(url, "&")
    parameters_map := Map()

    ; 遍历键值对，存储到字典中
    for index, pair in url_parameters {
        parts := StrSplit(pair, "=")
        parameters_map[parts[1]] := parts[2]
    }
    ; D:\PotPlayer64\PotPlayerMini64.exe "D:123.mp4" /seek=00:01:53.824 /new
    path := parameters_map["path"]
    time := parameters_map["time"]
    run_command := potplayer_path . " `"" . UrlDecode(path) . "`" /seek=" . time . " " . open_window_parameter
    MyLog run_command
    Run run_command
}

; 【主逻辑】将Potplayer的播放链接粘贴到Obsidian中
Potplayer2Obsidian(markdown_tittle){
    potplayer_name := GetProgramName(potplayer_path)
    media_time := ""
    InitMediaInfo(potplayer_path)
    media_path := GetMediaPath()
    media_time := GetMediaTime()
    Paste2Obsidian(media_path, media_time, markdown_tittle)
}
InitOpenWindowParameter(potplayer_path){
    if (IsPotplayerRunning(potplayer_path)) {
        return "/current"
    } else {
        return "/new"
    }
}
IsPotplayerRunning(potplayer_path){
    if SearchProgram(potplayer_path)
        return true
    else
        return false
}
SearchProgram(target_app_path) {
    ; 程序正在运行
    if (WinExist("ahk_exe " . GetProgramName(target_app_path))) {
        return true
    } else {
        return false
    }
}

InitMediaInfo(potplayer_path){
    if IsPotplayerRunning(potplayer_path){
        ; 激活窗口
        WinActivate "ahk_exe " . GetProgramName(potplayer_path)
    } else {
        MsgBox "PotPlayer is not running"
        Exit
    }
        
}
GetMediaPath(){
    hotkey := "!,"

    return PressDownHotkey(hotkey)
}
GetMediaTime(){
    hotkey := "!."

    return PressDownHotkey(hotkey)
}
PressDownHotkey(hotkey){
    old := A_Clipboard
    A_Clipboard := ""  ; 先让剪贴板为空, 这样可以使用 ClipWait 检测文本什么时候被复制到剪贴板中.
    Send hotkey
    ClipWait 0.60,0
    result := A_Clipboard
    ; MsgBox "剪切板的值是：" . result
    A_Clipboard := old

    return result
}

Paste2Obsidian(media_path, media_time, markdown_tittle){
    obsidian_active := "ahk_exe Obsidian.exe"
    if (WinExist(obsidian_active)) {
        WinActivate obsidian_active
        ; // [123](ahk-potplayer://open?type=1&aaa=123&bbb=456)

        markdown_tittle := StrReplace(markdown_tittle, "name",GetProgramName(media_path))
        markdown_tittle := StrReplace(markdown_tittle, "time",media_time)
        media_path := UrlEncode(media_path)
        ControlSendText "[" . markdown_tittle . "](ahk-potplayer://open?type=1" . "&path=" . media_path . "&time=" . media_time . ")"
        ControlSend "{Enter}"
    } else {
        MsgBox "Obsidian is not running"
        Exit
    }
}

; 【工具】
GetProgramName(program_path){
    ; 获取程序的路径
    SplitPath program_path, &name
    return name
}

MyLog(message){
    if log_toggle
        MsgBox message
}

UrlEncode(str, sExcepts := "-_.", enc := "UTF-8")
{
	hex := "00", func := "msvcrt\swprintf"
	buff := Buffer(StrPut(str, enc)), StrPut(str, buff, enc)   ;转码
	encoded := ""
	Loop {
		if (!b := NumGet(buff, A_Index - 1, "UChar"))
			break
		ch := Chr(b)
		; "is alnum" is not used because it is locale dependent.
		if (b >= 0x41 && b <= 0x5A ; A-Z
			|| b >= 0x61 && b <= 0x7A ; a-z
			|| b >= 0x30 && b <= 0x39 ; 0-9
			|| InStr(sExcepts, Chr(b), true))
			encoded .= Chr(b)
		else {
			DllCall(func, "Str", hex, "Str", "%%%02X", "UChar", b, "Cdecl")
			encoded .= hex
		}
	}
	return encoded
}

UrlDecode(Url, Enc := "UTF-8")
{
	Pos := 1
	Loop {
		Pos := RegExMatch(Url, "i)(?:%[\da-f]{2})+", &code, Pos++)
		If (Pos = 0)
			Break
		code := code[0]
		var := Buffer(StrLen(code) // 3, 0)
		code := SubStr(code, 2)
		loop Parse code, "`%"
			NumPut("UChar", Integer("0x" . A_LoopField), var, A_Index - 1)
		Url := StrReplace(Url, "`%" code, StrGet(var, Enc))
	}
	Return Url
}
