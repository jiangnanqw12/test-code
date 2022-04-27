import pyautogui as pyautogui
import time
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
while True:
    for str_f in ("f2", "f3", "f4", "f5"):
        time.sleep(3)
        # 寻找对局
        pyautogui.click(601, 685)
        time.sleep(0.1)
        # 接受对局
        pyautogui.click(714, 556)
        time.sleep(0.1)
        # 赞誉队友
        pyautogui.click(714, 556)
        time.sleep(0.1)
        # 寻找英雄（第二排最后一个）
        pyautogui.click(910, 277)
        time.sleep(1)
        pyautogui.click(910, 277)
        time.sleep(0.2)
        # （第三排最后一个）
        pyautogui.click(913, 373)
        time.sleep(0.2)
        # 寻找英雄（第三排最后一个）
        pyautogui.click(1366, 563)
        time.sleep(0.2)
        # //发送邀请
        pyautogui.click(671, 638)
        time.sleep(0.2)
        # //锁定英雄
        pyautogui.click(700, 604)
        time.sleep(0.2)
        # //移动鼠标至中心点
        pyautogui.moveTo(694, 365)
        time.sleep(0.2)

        # //———角色移动———
        pyautogui.keyDown('str_f')
        time.sleep(0.1)
        pyautogui.press('p')
        time.sleep(1)
        pyautogui.press('l')
        time.sleep(0.5)
        pyautogui.keyUp('str_f')

        # //接受对局
        pyautogui.click(714, 556)
        time.sleep(0.1)

        # //DF+眼+学习技能+使用技能
        pyautogui.keyDown('ctrl')
        time.sleep(0.1)
        pyautogui.press('r')
        time.sleep(0.1)
        pyautogui.press('q')
        time.sleep(0.1)
        pyautogui.press('w')
        time.sleep(0.1)
        pyautogui.press('e')
        time.sleep(0.1)
        pyautogui.keyUp('ctrl')
        time.sleep(0.1)

        pyautogui.press('4')
        time.sleep(0.1)
        pyautogui.press('d')
        time.sleep(0.1)
        pyautogui.press('f')
        time.sleep(0.1)
        pyautogui.press('r')
        time.sleep(0.1)
        pyautogui.press('e')
        time.sleep(0.1)
        pyautogui.press('q')
        time.sleep(0.1)
        pyautogui.press('w')
        time.sleep(0.1)

        # //移动鼠标至中心点
        pyautogui.moveTo(938, 581)
        time.sleep(0.1)
        pyautogui.moveTo(1045, 549)

        # //———角色移动———
        pyautogui.keyDown('str_f')
        time.sleep(0.1)
        pyautogui.press('p')
        time.sleep(1)
        pyautogui.press('l')
        time.sleep(0.5)
        pyautogui.keyUp('str_f')
        time.sleep(0.1)
        # //使用表情
        pyautogui.press('t')
        time.sleep(1)
