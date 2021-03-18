import os
import time
import keyboard
import pyautogui
import win32api, win32con
import sys

#meeting id past position==>X:  643 Y:  349 RGB: (255, 255, 255)

time.sleep(0.1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

os.system("TASKKILL /F /IM zoom.exe")

time.sleep(2)

os.system("start C:/Users/USER/AppData/Roaming/Zoom/bin/Zoom.exe")

def chec_1():
    
    time.sleep(4)
    
    try:
        x, y = pyautogui.locateCenterOnScreen('join_1.png')
        cry = True
    except:
        print("exception raised")
        chec_1()
        
    if cry:
        click(x, y)
        chec_2()
    else:
        time.sleep(1)
        print("false")
        chec_1()
        
    time.sleep(2)
    
def chec_2():
    
    time.sleep(1)
    
    try:
        cry = pyautogui.pixelMatchesColor(643, 516, ( 255, 255, 255))
    except:
        print("exception raised")
        chec_2()
    
    if cry:
        click(643,349)
        keyboard.write("7199225614")
        chec_3()
    else:
        time.sleep(1)
        print("false2")
        chec_2()
        
    time.sleep(1)
    
def chec_3():
    
    time.sleep(1)
    
    try:
        x, y = pyautogui.locateCenterOnScreen('join_2.png')
        cry = True
    except:
        print("exception raised")
        chec_3()
    
    if cry:
        click(x,y)
        sys.exit()
    

chec_1()
