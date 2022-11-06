import pyautogui as pyautogui
import time


def test():
    pyautogui.keyDown("win")
    pyautogui.press("d")
    pyautogui.keyUp("win")
    pyautogui.moveTo(694, 365, duration=0.25)
    pyautogui.click()


if __name__ == '__main__':
    test()
