"""
login = input("Введите логин ")
parol = input("Введите пароль ")
if login == "gta@mail.ru" and parol == "1234":
    print("Добро пожаловать,",login)
else:
    print("Логин или пароль неверный")
print("Спасибо что пользуетесь технологиями Umbrella Corporation")
"""
"""
f = open('data.txt', 'r')
str1 = f.readline()
print(str1)
f.close()
"""
"""
f = open('data.txt', 'r')
str1 = f.readline()
print(str1)
print("Вот ещё текст")
f.close()
"""
"""
f = open('data.txt', 'r')
str1 = f.readline()
print(str1.strip())
print("Вот ещё текст")
f.close()
"""
"""
f = open('data.txt', 'r')
str1 = f.readline()
str1 = str1.strip()
print(str1)
print("Вот ещё текст")
f.close()
"""
"""
f = open('data.txt', 'r')
str1 = f.readline().strip()
str2 = f.readline().strip()
print(str1)
print(str2)
print("Вот ещё текст")
f.close()
"""
"""
f = open('data2.txt', 'r', encoding="utf-8")
str1 = f.readline().strip()
print("Сейчас текст в файле такой:", str1)
f.close()

f = open('data2.txt', 'w', encoding="utf-8")
str2 = input("Введите новый текст файла: ")
f.write(str2)
f.close()
"""
"""
login = input("Введите логин ")
parol = input("Введите пароль ")
if login != "mail":
    print("Логин неверный ")
if parol != "132":
    print("Пароль неверный ")
else:
    f = open("Секретные данные.png", "r")
    str1 = f.readline()
    print(str1)
    f.close()
"""
"""
fail = input("Что сделать с файлом? Показать или Изменить? ")
if fail == "Показать":
    f = open("data3.txt","r")
    str1 = f.readline()
    print(str1)
    f.close()
else:
    f = open('data3.txt', 'w')
    str1 = input("Введите новый текст файла: ")
    f.write(str1)
    f.close()
"""
"""
money = input("Что сделать с деньгами: отнять или прибавить ")
if money == "отнять" or "прибавить":
    if money == "отнять":
        A = int(input("сколько отнять? "))
        f = open("Кошелек.txt","r", encoding="utf-8")
        str1 = f.readline()
        str1 = int(str1)
        print(str1 - A)
        f.close()
"""
НЕ ДОДЕЛАНО!!!
        
        
        
        







