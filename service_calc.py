__author__ = 'chaplygin_a'

#Импорт даты и объявление переменной:
from datetime import datetime
now = datetime.now()


#Ввод и валидация часов работы
def is_valid(working_hours):
    return isinstance(working_hours,float) and working_hours > 0

working_hours = 0
while not is_valid(working_hours):
    working_hours = float(input("Сколько часов работали? "))
    if working_hours <= 0:
        print("Значение должно быть больше 0. ")


#Ввод и валидация цены
def is_valid(hour_price):
    return isinstance(hour_price,float) and hour_price > 0

hour_price = 0
while not is_valid(hour_price):
    hour_price = float(input("Сколько долларов стоит час? "))
    if hour_price <= 0:
        print("Значение должно быть больше 0. ")


#Ввод и валидация курса доллара
def is_valid(currency):
    return isinstance(currency,float) and currency > 0

currency = 0
while not is_valid(currency):
    currency = float(input("Какой курс доллара? "))
    if currency <= 0:
        print("Значение должно быть больше 0. ")


#Расчёты
service_price = float(working_hours) * float(hour_price) * float(currency)


#Проверка скидки
discount_check = input("Есть скидка? ")
if discount_check in ("Да","Д","да","д","Есть","Y","Yes","yes","y"):
    discount_perc = input("Какой размер скидки? (%) ")
    discount = float(discount_perc) / 100.0
    total = float(service_price) - float(service_price) * float(discount)
else:
    print("Скидка отсутствует.")
    discount_perc = 0
    total = float(service_price)


#Вывод информации
print("______________________________________________")
print(" ")
if 5 < float(working_hours):
    print("Выполнение заказа заняло " + str(working_hours) + " ч., Вам пологается карта VIP-клиента.")
print('Цена процедуры: ' + str(service_price)+ " руб.")
print("Размер скидки: " + str(discount_perc)+ "%")
print("Итого: " + str(total)+ " руб.")
print('Дата: %s/%s/%s     Подпись:_______' % (now.day, now.month, now.year))
print("______________________________________________")

