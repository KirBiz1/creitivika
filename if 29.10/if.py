"""
print("Это кто?")
name = input("Как тебя зовут? ")
if name == "Саня":
    print("О! САНЯ!")
    print("ПРОХОДИ, ДОРОГОЙ!")

if name != "Саня":
    print("Так, ИДИ ОТСЮДА!")
"""
"""
num = input("Введите число")
if num > "100":
    print("Много!")
    
if num <= "100":
    print("Мало!")
"""
"""
command = input("Что хотите сделать?")
if command == "умножить на 2":
    num = float(input("Введите число:"))
    print("Получилось", num*2)
    
if command == "разделить на 2":
    num = float(input("Введите число:"))
    print("Получилось", num/2)
"""
"""
slovo = input("Введите любое слово ")
print(slovo,"отличный выбор!")
if slovo == "крабик":
    print("Ого!")
    print("Интересный у вас вкус!")
    print(slovo,"- отличный выбор")
"""
"""
temp = float(input("Введите текущую температуру в градусах "))
import time
if temp > 25:
    time.sleep(1.5)
    print("Слишком жарко!")
    time.sleep(1.5)
    print("Оптимальная температура на 3 градуса холоднее!")
    time.sleep(1.5)
    print("Включаю кондиционер.")
    time.sleep(1.5)
    print("Сейчас станет прохладнее.")
if temp < 20:
    time.sleep(1.5)
    print("Слишком холодно!")
    time.sleep(1.5)
    print("Оптимальная температура на 2 градуса повысить!")
    time.sleep(1.5)
    print("Включаю обогреватель.")
    time.sleep(1.5)
    print("Сейчас станет теплее.")
time.sleep(1.5)    
print("Приятного отдыха!")
"""
"""
one = float(input("Введите первое число: "))
two = float(input("Ввeдите второе число: "))
if one > two:
    print("Разность равна:",one - two)
if one < two:
    print("Разность равна:",two - one)
if one == two:
    print("Разность равна:",one - two)
"""
"""
ves = float(input("Ведите вес ручной клади в килограммах "))
import time
if ves < 10:
    print("Принято")
time.sleep(1.5)
print("Самолет вылетает через час.")
"""

bilet = 2000
float(bilet)
vsego = float(input("Cколько всего людей "))
if vsego == 0:
    print("Поездка отменяется")
if vsego == 1:
    kilo = float(input("Сколько весит ваш багаж "))
    kg = (200*kilo)
    print("С вас",bilet + kg,"рублей")
if vsego == 2:
    kilo1 = float(input("Сколько весит багаж первого "))
    kilo2 = float(input("Сколько весит багаж вторго "))
    kg1 = (200*kilo1)
    kg2 = (200*kilo2)
    print("С первого",bilet + kg1,"рублей")
    print("Со второго",bilet + kg2,"рублей")
if vsego == 3:
     kilo3 = float(input("Сколько весит багаж первого "))
     kilo4 = float(input("Сколько весит багаж вторго "))
     kilo5 = float(input("Сколько весит багаж первого "))
     kg3 = (200*kilo3)
     kg4 = (200*kilo4)
     kg5 = (200*kilo5)
     print("C первого",bilet + kg3,"рублей")
     print("Cо второго",bilet + kg4,"рублей")
     print("C третьего",bilet + kg5,"рублей")
     print("Всего: ",(bilet + kg3)+(bilet + kg4)+(bilet + kg5))
     


     
     

     
     
     

     
     
     
    
    
    




