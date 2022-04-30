import pyautogui as pyautogui
import time

while True:
    for str_f in ("f2", "f3", "f4", "f5"):

        pyautogui.moveTo(694, 365, duration=0.25)
        pyautogui.click()

        # //———角色移动———
        pyautogui.keyDown('str_f')
        time.sleep(0.1)
        pyautogui.press('p')
        time.sleep(1)
        pyautogui.press('l')
        time.sleep(0.5)
        pyautogui.keyUp('str_f')
