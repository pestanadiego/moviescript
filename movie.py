import time
import pyautogui

def SendScript():
           
        time.sleep(3)

        with open('movie.txt') as file:
            script = file.readlines()

        for line in script:
            pyautogui.typewrite(line.strip())
            pyautogui.press('enter')

SendScript()

