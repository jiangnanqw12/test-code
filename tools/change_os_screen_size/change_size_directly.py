import win32api
import win32con
import pywintypes
devmode = pywintypes.DEVMODEType()

# screenSize = [1280,800]
screenSize = [1920,1080]

devmode.PelsWidth = screenSize[0]
devmode.PelsHeight = screenSize[1]
devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
win32api.ChangeDisplaySettings(devmode,0)