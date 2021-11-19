# Отредактируйте код чтобы выполнялись ассерт инструкции. (потребуется знание строковых функций.)
print('TACK1:')

var1 = 'pyThoN'
venv = var1.lower()
var1 = var1.capitalize()
assert var1 == 'Python'

var1 = var1.upper()
assert var1 == 'PYTHON'

var1 = var1.lower()
assert var1 == 'python'

var1 = " python "
var1 = var1.strip()
assert var1 == 'python'

print('Text edited!')

####Задача Вот код: Сделайте чтобы он выводил 'Привіт Остап' еще тремя способами форматирования.
# И да они все вам понадобятся. f-строки, .format и форматирование через "%"
print('Tack2')

name = "Остап"
print("Привет "+name)

text = "Привет {}".format(name)
print(text)

text = f"Привет {name}"
print(text)

text = "Привет %s"%(name)
print(text)

###Задача Почините код
print('TACK3')

price = 12
weight = 3.4121
rez = 0
rez = price*weight
rez = round(rez,2)
rez="Итого: {}".format(rez)
print(rez)
assert rez == 'Итого: 40.95'

###Задача Используя форматирование и черную магию заставьте этот код выполниться без ошибок.
#Строки с обьявлением переменных и assert не трогаем!
#Подсказка: 54 в битовом представлении - 110110

print('TACK4')

number = 12
username = "ираклий"
access_mask = 54
hour_price=15.321
rez = 0

username = username.capitalize()
hour_price=round(hour_price,2)

number = "{}{}".format("0000", number)

b_access_mask = ''
while access_mask > 0:
    b_access_mask = str(access_mask % 2) + b_access_mask
    access_mask = access_mask // 2

rez = "{0} {1} {2} {3}".format(number,username,b_access_mask,hour_price)
print(rez)
assert rez == '000012 Ираклий 110110 15.32'

###Задача Используя слайсы, конкатенацию (обьединение) и смекалку заставьте код работать
print('TACK5')

base_str = 'Корова'
rez = 0
base_str = base_str.replace('в','н')
base_str = base_str.replace('К','в')
base_str = base_str.capitalize()
rez = base_str
print(rez)
assert rez == 'Ворона'

###Задача Поменяйте местами значения в переменных
print('TACK6')

a = 10
b = 55
a,b=b,a
print('a=',a,'b=',b)
assert a==55 and b==10, "Не поменялось. :("