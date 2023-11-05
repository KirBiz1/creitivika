"""
import pyautogui
import time

Fail = input("Какой файл из трех открыть? ")
if Fail == "1":
    pyautogui.moveTo(1250,11)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(45,38)
    time.sleep(2)
    pyautogui.doubleClick()
if Fail == "2":
    pyautogui.moveTo(1250,11)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(90,38)
    time.sleep(2)
    pyautogui.doubleClick()
if Fail == "3":
    pyautogui.moveTo(1250,11)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(180,38)
    time.sleep(2)
    pyautogui.doubleClick()
"""
"""
poisk = input("1 или 2? ")
import pyautogui
import time
import keyboard
if poisk == "1":
    pyautogui.moveTo(1250,11)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(644,754)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(446,441)
    pyautogui.click()
    keyboard.write("разумен ли я?")
if poisk == "2":
    pyautogui.moveTo(1250,11)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(644,754)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(446,441)
    pyautogui.click()
    keyboard.write("cлава России!")
"""



import pyautogui
import time
import keyboard
vrach = input("Во сколько прием у стомотолога? ")
vrach1 = input("Завтра или послезавтра? ")
time.sleep(2)
pyautogui.hotkey("winleft","r")
time.sleep(2)
keyboard.write("notepad")
time.sleep(2)
pyautogui.press("enter")
pyautogui.moveTo(644,754)
keyboard.write("Зубной врач","vrach1","vrach")




  
  
    
    

    
    
    
    


























