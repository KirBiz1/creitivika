"""
tsvet = input("Введите цвет: ")
if tsvet == "красный" or tsvet == "синий":
    print("Я тоже этот цвет люблю!")
    print("Дай пять!")
    
if tsvet != "красный" and tsvet != "синий":
    print("Не люблю этот цвет")
    print("Синий и красный люблю")
    
print("Ладно, бывай")
"""
"""
tsvet = input("Введите цвет: ")
if tsvet == "красный" or tsvet == "синий" or tsvet == "зелёный":
    print("Я тоже этот цвет люблю!")
    print("Дай пять!")
    
if tsvet != "красный" and tsvet != "синий" and tsvet != "зелёный":
    print("Не люблю этот цвет")
    print("Синий и красный и зелёный ещё люблю")
    
print("Ладно, бывай")
"""
"""
import pyautogui

login = input("Введите логин ")
parol = input("Введите пароль ")
if login == "crystal" and parol == "123":
    pyautogui.moveTo(1250,11)
    pyautogui.click()
    pyautogui.moveTo(709,147)
    pyautogui.doubleClick()
if login != "crystal":
    print("Логин неверен")
if parol != "123":
    print("Пароль неверен")
if login != "crystal" and parol != "123":
    print()
"""
"""
ima = input("Введите имя ")
familia = input("Введите фамилию ")
vozrast = input("Введите полный возраст ")
if vozrast > "17" and ima != "Микордий" or familia != "Пармезанов":
    print("Добро пожаловать")
if vozrast <= "17":
    print("По закону вход несовершеннолетним запрещен ")
if ima == "Микордий" and familia =="Пармезанов":
    print("Вы в черном списке, вам нельзя")
"""
import pyautogui
vlaz = input("Влажность ")
temp = input("Температура ")
if vlaz > "60" and temp < "10": 
    pyautogui.moveTo(1250,11)
    pyautogui.click()
    pyautogui.moveTo(636,418)
    pyautogui.click()
    pyautogui.moveTo(475,418)
    pyautogui.click()
    pyautogui.write("Что делать при нарушении условий в оранжерее ")
    pyautogui.press("enter")
if vlaz < "30" or temp > "30":
    pyautogui.moveTo(1250,11)
    pyautogui.click()
    pyautogui.moveTo(636,900)
    pyautogui.click()
    pyautogui.moveTo(475,418)
    pyautogui.click()
    pyautogui.write("Что делать при нарушении условий в оранжерее ")
    pyautogui.press("enter")

    
   
    
   
    
    
  


    

