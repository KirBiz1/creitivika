import time
print("Вас приветствует электронный помощник: kolkway ")
time.sleep(4)
print("С моей помощью математические потребности в вашей жизни сокращаться в двое! ")
time.sleep(4)
print("Меню моих возможностей: ")
time.sleep(4)
print("Калькулятор, нахождение среднего арифмитического из массы чисел, возведение в квадрат ")
time.sleep(4)
work = input("Что вам понадобиться для дальнейшей работы? ")
if work == "калькулятор":
    one = float(input("Введите первое число "))
    two = float(input("Введите второе число "))
    three = input("Что вы хотите сделать? ")
    if three == "сложить":
        print(one + two)
    if three == "вычесть":
        print(one - two)
    if three == "разделить":
        print(one / two)
        if two == "0":
            print("Ошибка, на ноль делить нельзя")
    if three == "умножить":
        print(one * two)
    else:
        print("Вы допустили ошибку при использовании колькулятора! ")
        print("Повторите снова! ")
if work == "нахождение среднего арифмитического из массы чисел":
    time.sleep(3)
    print("Если у вас масса чисел меньше чем придложено, то вместо придложенных чисел ставьте ноль ")
    pervoe = float(input("Введите первое число "))
    vtoroe = float(input("Введите второе число "))
    tretie = float(input("Введите третье число "))
    chetvertoe = float(input("Введите четвертое число "))
    patoe = float(input("Введите пятое число "))
    shestoe = float(input("Введите шестое число "))
    sedimoe = float(input("Введите седьмое число "))
    vosimoe = float(input("Введите восьмое число "))
    devatoe = float(input("Введите девятое число "))
    desatoe = float(input("Введите десятое число "))
    print("Среднее арифмитеческое равняется" , (pervoe + vtoroe + tretie + chetvertoe + patoe + shestoe + sedimoe + vosimoe + devatoe + desatoe) / 2)
if work == "возведение в квадрат":
    A = float(input("Введите число "))
    print("Квадрат числа равен" , A*A)
B = input("Интресно ли вам информация о нашем помощнике? ")
if B == "да":
    f = открыть('kolk.way.txt', 'r')




    
        
    
    

        


