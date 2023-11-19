"""
one = input("Состояние первого колеса ")
two = input("Состояние второго колеса ")
three = input("Состояние третьего колеса ")
four = input("Состояние четвертого колеса")
if one > "6" or two > "6" or three > "6" or four > "6":
    print("Замени от греха подальше.")
else:
    print("Все хорошо, ехаем!")
"""

summ = float(input("Стоимость товара "))
mes = input("Сумма потраченная за месяц ")
skid = float(input("Какая скидка на товар "))
if skid == "0":
    if mes == "1000":
        print((summ * 5) / 100, "рублей скидка ")
        print("Сумма", summ - (summ* 5) / 100 , "рублей ")
    if mes == "2000":
        print((summ * 10) / 100, "рублей скидка ")
        print("Сумма", summ - (summ * 10) / 100 , "рублей ")
    if mes == "3000":
        print((summ * 15) / 100, "рублей скидка ")
        print("Сумма", summ - (summ * 15) / 100 , "рублей ")
if skid != "0":
    print("Цена", summ, "рублей")
    print("Сумма", summ - (summ * skid) / 100 , "рублей ")
    
    
    
    
    
        

                
                
                

    

    


    
    


    
    
