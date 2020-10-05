# Перевод секунд в форматированное время: hh:mm:ss
input_sec = int(input('Введите время в секундах:'))
hour = 0
min = 0
sec = 0

min = input_sec // 60
sec = input_sec % 60
hour = min // 60
min = min % 60

print('%02d : %02d : %02d' % (hour,min,sec))
