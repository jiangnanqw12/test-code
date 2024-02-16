^+p::ProcessClipboard()

ProcessClipboard() {
    if (!ClipWait(1)) {  ; Wait up to 1 second for the clipboard to contain data. If it fails, notify the user.
        MsgBox "Clipboard did not receive content in time."
        return
    }

    clipContent := ClipboardAll  ; Use Clipboard directly for text content

    if (clipContent == "") {  ; Check if clipboard is indeed empty after ClipWait
        MsgBox "Clipboard is empty."
        return
    }

    lines := StrSplit(clipContent, "`n", "`r")

    processedLines := []

    for each, line in lines {
        processedLine := StrReplace(StrLower(line), " ", "_")
        processedLines.Push(processedLine)
    }

    processedText := StrJoin(processedLines, "`n")

    ; Display the processed text before setting it back to the clipboard
    MsgBox(processedText)

    Clipboard := processedText
}

StrJoin(arr, delimiter := "") {
    result := ""
    for index, value in arr {
        if (index > 1) {
            result .= delimiter
        }
        result .= value
    }
    return result
}
