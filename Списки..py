"""
slova = ["снежок", "пирожок", "СМЕТАААНА"]
for slovo in slova:
    print(slovo, end=" ") 
"""
"""
slova = ["снежок", "пирожок", "СМЕТАААНА"]
for slovo in slova:
    print(slovo, end=" ") 

slovo = input("Введите новое слово: ")
slova.append(slovo)

for slovo in slova:
    print(slovo, end=" ") 
"""
"""
slova = ["снежок", "пирожок", "СМЕТАААНА"]
for slovo in slova:
    print(slovo, end=" ") 

slovo = input("Введите новое слово: ")
slova.append(slovo)

for slovo in slova:
    print(slovo, end=" ") 
"""
"""
slova = ["снежок","пирожок", "СМЕТАААНА"]
slova[1] = "рогалик"
print(slova) 
"""
"""
frukt = ["яблоко","груша","дыня","виноград","манго"]
print(frukt)
frukt[0] = input("Введите новое 1 слово ")
frukt[4] = input("Введите новое 6 слово ")
print(frukt)
"""
"""
play = ["Варфейс","Ворлд оф танкс","Вар робот"]
print(play)
slovo = input("Введите новое слово: ")
play.append(slovo)

slovo = input("Введите новое слово: ")
play.append(slovo)

for slovo in play:
    print(slovo, end=" ")
"""
"""
name = []

slovo = input("Введите новое имя: ")
name.append(slovo)

slovo = input("Введите новое имя: ")
name.append(slovo)

slovo = input("Введите новое имя: ")
name.append(slovo)

slovo = input("Введите новое имя: ")
name.append(slovo)

slovo = input("Введите новое имя: ")
name.append(slovo)

slovo = input("Введите новое имя: ")
name.append(slovo)
print(name)
"""
"""
animals = ["Кот","Лев","Тигр"]
c = float(input("Какое слово заменить? "))
if c == 1:
    animals[0] = input("Введите новое слово ")
    print(animals)
if c == 2:
    animals[1] = input("Введите новое слово ")
    print(animals)
if c == 3:
    animals[2] = input("Введите новое слово ")
    print(animals)
"""
"""
sp = ["#", "#", "*", "#"]
kom = str(input("Напишите куда пойти звезде: вправо, влево"))
ch = 2
while kom != "stop": 
    if kom == "вправо":
        ch = ch + 1
        if ch == 4:
            ch = 3
        sp[ch] = "*"
        sp[ch - 1] = "#"
    if kom == "влево":
        ch = ch - 1
        if ch == -1:
            ch = 0
        sp[ch] = "*"
        sp[ch + 1] = "#"
    for slovo in sp:
        print(slovo, end="")
    kom = input("Напишите куда пойти звезде: вправо, влево")
"""


    
