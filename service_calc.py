__author__ = 'chaplygin_a'
#Исходные данные
#working_hours = 10
#hour_price = 30
#currency = 56.23
#discount_perc = 25

#Импорт даты и объявление переменной:
from datetime import datetime
now = datetime.now()

#Ввод данных:
working_hours = input("Сколько часов работали?")
hour_price = input("Сколько долларов стоит час?")
currency = input("Какой курс доллара?")
discount_perc = input("Какой размер скидки?")

#Расчёты
service_price = float(working_hours) * float(hour_price) * float(currency)
discount = float(discount_perc) / 100.0
total = float(service_price) - float(service_price) * float(discount)

#Вывод информации:
print('Цена процедуры: ' + str(service_price)+ " руб.")
print("Размер скидки: " + str(discount_perc)+ "%")
print("Итого: " + str(total)+ " руб.")
print('Дата: %s/%s/%s     Подпись:_______' % (now.day, now.month, now.year))

