import time
import os
import threading
import pyautogui
l=["sdfgfd","werert","sdrhj","sdfttghjmfc","bunny"]

def rat():
    while True:
        os.system('su bunny')
r=threading.Thread(target=rat)
r.start()
while True:
    for i in l:
        time.sleep(5)
        pyautogui.typewrite(i)
        pyautogui.press('enter')


