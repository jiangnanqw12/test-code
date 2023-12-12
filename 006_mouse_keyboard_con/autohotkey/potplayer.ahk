#Requires AutoHotkey v2.0
; Set the path of PotPlayer
potplayer_path := "D:\DevelopmentTools\Softare\WindowsTools\PotPlayer64\PotPlayerMini64.exe"
; Set the default title format for Markdown links
markdown_tittle := "name-->time"

log_toggle := false
open_window_parameter := InitOpenWindowParameter(potplayer_path)

; Define a hotkey Alt+G
; Hotkeys - Definition & Usage | AutoHotkey v2
; https://wyagd001.github.io/v2/docs/Hotkeys.htm
!g::{
    Potplayer2Obsidian(markdown_tittle)
}

; Main logic - Callback function for PotPlayer (Backlink)
CallbackPotplayer(){
    url := ReceivParameter()
    ParseUrl(url)
}

; Function to receive parameters
ReceivParameter(){
    ; Save script as ShowParameters.ahk

    ; Get the number of command line arguments
    paramCount := A_Args.Length

    ; Show a message if no arguments provided
    if (paramCount = 0) {
        MsgBox "Please provide at least one argument."
        ExitApp
    }

    ; Loop through arguments and return them
    for n, param in A_Args{
        return param
    }
}

; Function to parse URL
ParseUrl(url){
    ; Example URL: "ahk-potplayer://open?type=1&aaa=123&bbb=456"
    url := StrReplace(url, "ahk-potplayer://open?type=1&")

    ; Parse key-value pairs
    url_parameters := StrSplit(url, "&")
    parameters_map := Map()

    ; Iterate through key-value pairs and store them in a dictionary
    for index, pair in url_parameters {
        parts := StrSplit(pair, "=")
        parameters_map[parts[1]] := parts[2]
    }
    ; Construct and run the command to open PotPlayer with specific media and time
    run_command := potplayer_path . " `"" . UrlDecode(path) . "`" /seek=" . time . " " . open_window_parameter
    MyLog run_command
    Run run_command
}

; Main logic - Paste PotPlayer playback link to Obsidian
Potplayer2Obsidian(markdown_tittle){
    potplayer_name := GetProgramName(potplayer_path)
    media_time := ""
    InitMediaInfo(potplayer_path)
    media_path := GetMediaPath()
    media_time := GetMediaTime()
    Paste2Obsidian(media_path, media_time, markdown_tittle)
}

; Initialize window opening parameters based on whether PotPlayer is running
InitOpenWindowParameter(potplayer_path){
    if (IsPotplayerRunning(potplayer_path)) {
        return "/current"
    } else {
        return "/new"
    }
}

; Check if PotPlayer is running
IsPotplayerRunning(potplayer_path){
    if SearchProgram(potplayer_path)
        return true
    else
        return false
}

; Search for the PotPlayer program
SearchProgram(target_app_path) {
    ; Check if the program is running
    if (WinExist("ahk_exe " . GetProgramName(target_app_path))) {
        return true
    } else {
        return false
    }
}

; Initialize media information from PotPlayer
InitMediaInfo(potplayer_path){
    if IsPotplayerRunning(potplayer_path){
        ; Activate window
        WinActivate "ahk_exe " . GetProgramName(potplayer_path)
    } else {
        MsgBox "PotPlayer is not running"
        Exit
    }

}

; Get the media path from PotPlayer
GetMediaPath(){
    hotkey := "!,"

    return PressDownHotkey(hotkey)
}

; Get the media playing time from PotPlayer
GetMediaTime(){
    hotkey := "!"

    return PressDownHotkey(hotkey)
}

; Function to press a hotkey and return the clipboard content
PressDownHotkey(hotkey){
    old := A_Clipboard
    A_Clipboard := ""  ; Clear the clipboard first, so we can use ClipWait to detect when text is copied to it.
    Send hotkey
    ClipWait 0.60,0
    result := A_Clipboard
    ; MsgBox "Clipboard value is: " . result
    A_Clipboard := old

    return result
}

; Function to paste media information into Obsidian
Paste2Obsidian(media_path, media_time, markdown_tittle){
    obsidian_active := "ahk_exe Obsidian.exe"
    if (WinExist(obsidian_active)) {
        WinActivate obsidian_active
        ; Format: [123](ahk-potplayer://open?type=1&aaa=123&bbb=456)

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

; Utility functions
GetProgramName(program_path){
    ; Get the program's path
    SplitPath program_path, &name
    return name
}

; Logging function
MyLog(message){
    if log_toggle
        MsgBox message
}

; URL encode function
UrlEncode(str, sExcepts := "-_.", enc := "UTF-8")
{
    hex := "00", func := "msvcrt\swprintf"
    buff := Buffer(StrPut(str, enc)), StrPut(str, buff, enc)   ; Convert encoding
    encoded := ""
    Loop {
        if (!b := NumGet(buff, A_Index - 1, "UChar"))
            break
        ch := Chr(b)
        ; 'isalnum' is not used because it's locale-dependent.
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

; URL decode function
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
