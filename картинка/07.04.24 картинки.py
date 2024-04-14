"""
from PIL import Image
 
image = Image.open('img.jpg')
image.show()
"""
"""
from PIL import Image
 
image = Image.open('img.jpg')
print("Ширина:", image.width)
print("Высота:", image.height)
print("Название:", image.filename)
image.close()
"""
"""
from PIL import Image
 
image = Image.open('img.jpg')
new_image = image.resize((100, 100), Image.LANCZOS)
new_image.save("resized_img.jpg")
image.close()
new_image.close()
"""
"""
задание - 2
from PIL import Image
 
image = Image.open('img.jpg')
image2 = Image.open('img.jpg')
new_image = image.crop((0, 0, image.width / 2, image.height))
new_image2 = image2.crop((1000,0,image.width  , image.height))
#можно так
#cord = (10, 50, 100, 200)
#new_image = image.crop(cord)
new_image.save("cropped2_img.jpg")
new_image2.save("cropped3_img.jpg")
image.close()
new_image.close()
image2.close()
new_image2.close()
"""
"""
from PIL import Image
 
image = Image.open('img.jpg')
new_image = image.rotate(180)
new_image.save("rotated_img.jpg")
image.close()
new_image.close()
"""
"""
from PIL import Image
 
image = Image.open('img.jpg')
new_image = image.rotate(180)
new_image.save("rotated_img.jpg")
image.close()
new_image.close()
"""
"""
from PIL import Image
 
image = Image.open('img.jpg')
print(image.format)
image.save('img.png', 'png')
image.close()
"""
"""
Задание - 1
from PIL import Image

image = Image.open("pupu.jpg")
image2 = Image.open("apple.jpg")
new_image = image.resize((150, 150), Image.LANCZOS)
new_image2 = image2.resize((150, 150), Image.LANCZOS)
new_image.save("icon_pupu.jpg")
new_image2.save("icon_apple.jpg")
image.close()
new_image.close()
image2.close()
new_image2.close()
"""
"""
from PIL import Image
 
image = Image.open('img.jpg')

image.close()
"""
"""
задание - 2
from PIL import Image
 
image = Image.open('img.jpg')
image2 = Image.open('img.jpg')
new_image = image.crop((0, 0, image.width / 2, image.height))
new_image2 = image2.crop((1000,0,image.width  , image.height))
#можно так
#cord = (10, 50, 100, 200)
#new_image = image.crop(cord)
new_image.save("cropped2_img.jpg")
new_image2.save("cropped3_img.jpg")
image.close()
new_image.close()
image2.close()
new_image2.close()
"""
"""
Задание - 3
from PIL import Image
 
image = Image.open('pupu.jpg')
image2 = Image.open('apple.jpg')
image3 = Image.open("logo.jpg")
#print("Ширина:", image.width)
#print("Высота:", image.height)
#print("Ширина2:", image2.width)
#print("Высота2:", image2.height)
#print("Ширина3:", image3.width)
#print("Высота3:", image3.height)
new_image = image.resize((525, image.height), Image.LANCZOS)
new_image2 = image2.resize((369, image2.height), Image.LANCZOS)
new_image3 = image3.resize((600, image3.height), Image.LANCZOS)
new_image.save("pupu1.img.jpg")
new_image2.save("apple1.img.jpg")
new_image3.save("logo1.img.jpg")
image.close()
new_image.close()
image2.close()
new_image2.close()
image3.close()
new_image3.close()
"""
"""
Задание 4
from PIL import Image
point = input("Как повернуть картинку? Направо на 90 градусов, налево, вверх ногами или оставить, как есть.")
if point.lower() == "направо на 90 градусов":
    image = Image.open('tiger.jpg')
    new_image = image.rotate(240)
    new_image.save("tiger right.jpg")
    image.close()
    new_image.close()
if point.lower == "налево на 90 градусов":
    image = Image.open('tiger.jpg')
    new_image = image.rotate(90)
    new_image.save("tiger left.jpg")
    image.close()
    new_image.close()
if point.lower == "вверх ногами":
    image = Image.open('tiger.jpg')
    new_image = image.rotate(180)
    new_image.save("tiger3.jpg")
    image.close()
    new_image.close()
if point.lower == "оставить как есть":
    print()
else:
    print("Команда не ясна")
"""
"""
задание 5
from PIL import Image
art = input("Что сделать с картинкой: обрезать, повернуть, показать формат, изменить формат.Если вам больше не надо редактировать напишите стоп.")
if art == "обрезать":
    rez = int(input("Насколько хотите обрезать?"))
    rez1 = int(input("Насколько хотите обрезать?"))
if art == "повернуть":
    pov = input("Насколько хотите повернуть?")
if art == "показать формат":
    print()
if art == "поменять формат":
    fr = input("На какой формат хотели бы вы поменять? ")
while art != "стоп":
    if art == "поменять формат":
        img = Image.open("lion.jpg")
        new_img = img.resize((rez, rez1))
        new_img.save("lion2.jpg")
        img.close()
        new_img.close()
"""

from PIL import image
for a in range(1,4):
    img = image = Image.open('1.jpg')
    


        
    
    
    
        
        
        
    
    
    
    
    






