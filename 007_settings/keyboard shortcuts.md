
## vscode example

// Place your key bindings in this file to override the defaults
[
    {
        "key": "shift+alt+e",
        "command": "revealInExplorer"
    },
    {
        "key": "ctrl+shift+1",
        "command": "md-shortcut.toggleTitleH1",
        "when": "editorLangId == markdown"
    },
    {
        "key": "ctrl+shift+2",
        "command": "md-shortcut.toggleTitleH2",
        "when": "editorLangId == markdown"
    },
    {
        "key": "ctrl+shift+3",
        "command": "md-shortcut.toggleTitleH3",
        "when": "editorLangId == markdown"
    },
    {
        "key": "ctrl+shift+4",
        "command": "md-shortcut.toggleTitleH4",
        "when": "editorLangId == markdown"
    },
    {
        "key": "ctrl+shift+5",
        "command": "md-shortcut.toggleTitleH5",
        "when": "editorLangId == markdown"
    },
    {
        "key": "ctrl+shift+6",
        "command": "md-shortcut.toggleTitleH6",
        "when": "editorLangId == markdown"
    },
    {
        "key": "ctrl+shift+7",
        "command": "md-shortcut.toggleBullets",
        "when": "editorTextFocus && markdownShortcuts:enabled"
    },
    {
        "key": "ctrl+m ctrl+b",
        "command": "-md-shortcut.toggleBullets",
        "when": "editorTextFocus && markdownShortcuts:enabled"
    },
    {
        "key": "ctrl+shift+8",
        "command": "md-shortcut.toggleNumbers",
        "when": "editorTextFocus && markdownShortcuts:enabled"
    },
    {
        "key": "ctrl+m ctrl+1",
        "command": "-md-shortcut.toggleNumbers",
        "when": "editorTextFocus && markdownShortcuts:enabled"
    }
]

## sumatra pdf example

Shortcuts [
	[
		Cmd = CmdShowInFolder
		Key = Alt + Shift + R
	]
]