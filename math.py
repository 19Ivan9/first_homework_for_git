###задание 1.0 В курсе 44 занятия с домашними работами. Для получения диплома надо сдать 80%.
# Сколько заданий нужно будет сдеать? Ответ выведите с помощью функции print()

print('TACK1:')
maxPer = 100
minPer = 80

total = 44
rez = int((total*minPer)/maxPer)
print("Для успешного окончания курса надо сдать {} домашек".format(rez))
assert rez ==35

###Есть координаты (переменные) x1, y1 и x2, y2 рассчитайте и выведите расстояние между точками.
print('TACK2:')
import random
import math
x1 =int(random.randint(1,10))
y1 =int(random.randint(1,10))
x2 =int(random.randint(1,10))
y2 =int(random.randint(1,10))
print("x1=",x1,';' ,'y1 =',y1,';','x2=',x2,';','y2=',y2)
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print('Distance between two points= ', distance)

###задание Создайте переменные Высоты ширины и глубины для прямоугольника и выведите с помощью команды print
# площадь диагонального сечения. (представьте себе что нужно рассчитать площадь щифера для крыши.)
# Стоимость "листа" шифера - 600грн. Размеры 3х4м. Сколько листов вам понадобиться купить?
# Выведете на экран количество, сумму, остаток шифера.
print('TACK3:')

aa1=22
ad=22
ab=10

LenDiag = math.sqrt(ad**2+ab**2)
DiagArea = aa1*LenDiag
print('Diagonal area= ',DiagArea)

price = 600
slate_size = 3*4

remainder =round(DiagArea%slate_size)
amount_slate = round(DiagArea/slate_size)
total_price = amount_slate*price

print('amount: ',amount_slate,'; Total price of slate: ',total_price,'UAN;','remainder: ',remainder)

