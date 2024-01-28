"""
num = input("Введите 5: ")
while num != "5":
    num = input("Это не 5! Введите 5: ")
print("Вот теперь 5!")
"""
"""
name = input("Введите имя: ")
sur_name = input("Введите фамилию: ")

while name != "Неждан" or sur_name != "Мохноногов":
    print("Нет, я жду Неждана Мохноногова, тебя не пущу!")
    print("А ты кто?")
    name = input("Введите имя: ")
    sur_name = input("Введите фамилию: ")

print("Проходи, Нежданчик!")
"""
"""
otvet = input("Отгадай загадку: зимой и летом одним цветом: ")

while otvet != "человек-паук":
    if otvet == "ель":
        print("Неплохо, но не угадал")
    elif otvet == "небо":
        print("Да не, небо разного цвета даже за один день")
    else:
        print("Нет, не верно")
    otvet = input("Отгадай загадку: зимой и летом одним цветом: ")

print("Верно! Паутина из рук и костюм один и тот же!")
"""
"""
parol = float(input("Введите пароль "))
while parol != 2024:
    print("Пароль неверный. Введите снова")
    parol = float(input("Введите пароль "))
else:
    print("Пароль верный ")
"""
"""
login = input("Введите логин ")
while login != "ABC.ru":
    print("Логин неверный. Попробуйте снова.")
    login = input("Введите логин ")
if login == "ABC.ru":
    print("Логин верный ")
parol = float(input("Введите пароль "))
while parol != 123:
    print("Пароль неверный. Попробуйте снова.")
    parol = float(input("Введите пароль "))
if parol == 123:
    print("Пароль верный ")
print("Успешный вход")
"""


    
    
    




