reg add HKEY_CURRENT_USER\Software\Classes\ahk-potplayer /ve /d "" /f
reg add HKEY_CURRENT_USER\Software\Classes\ahk-potplayer /v "URL Protocol" /d "" /f
reg add HKEY_CURRENT_USER\Software\Classes\ahk-potplayer\Shell /ve /f
reg add HKEY_CURRENT_USER\Software\Classes\ahk-potplayer\Shell\Open /ve /f

reg add HKEY_CURRENT_USER\Software\Classes\ahk-potplayer\Shell\Open\command /ve /d "\"%~dp0potplayer.exe\" \"%%1\"" /f