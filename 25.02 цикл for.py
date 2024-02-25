"""
for num in 5, 4, 3, 2, 1:
    print(num)
print("БУМ!")
"""
"""
for num in 5, 4, 3, 2, 1, "БУМ!":
    print(num)
"""
"""
for data in 5, "СалАТИЩЕ", True, None , 2>6, 2*2, "БУМ!":
    print(data)
"""
"""
step = 0
for num in "банан","арбуз","дыня","груша":
    step += 1
print(step)
"""
"""
marks = 0
for i in 1, 2, 3, 4, 5, 6:
    marks += int(input())
print(marks/6)
"""
"""
zagadano = 6

for popytki in range(3, 0, -1):
    
    print("Осталось" + str(popytki) + ' попыток')
    print("Отгадай число от 0 до 9")
    num = int(input('Введи число: '))
    
    if num > zagadano:
        print("Не угадал!")
        print(str(num) + " больше загаданного числа")
    elif num < zagadano:
        print(str(num) + " меньше загаданного числа")
    else:
        break
    
if num != zagadano:
    print("Попытки кончились!")
else:
    print("Угадал!")
#break - выход из цикла.
#str - превращает в строку.
"""
"""
step = 0
for num in "GD","Warface","WOT","Rust","GD":
    if num == "GD":
        step += 1
        print(step)
"""
"""
for num in "Джек Воробей","Халк","Буратино","Тор","Шерлок Холмс","Шрек","Гринч":
    if num == "Джек Воробей":
        print("Минуточку КАПИТАН Джек Воробей")
    print (num)
"""
"""
#num - попытка
chislo = 8
step = False
for num in 3,2,1:
    per = int(input("Введите число "))
    if per > 8:
        print("Число",per,",больше заданного числа," "осталось",num,"попытки")
    if per < 8:
        print("Число",per,"меньше заданного числа," "осталось",num,"попытки")
    else:
        print("угадали")
        step = True
        break
if not step:
    print("Продули")
"""        
        
    





    
