# max_number - максимальное число из заданных
# inx - длинна введенной строки
# input_number - введеная строка чисел

max_number = 0
input_number = input('Введите многозначное целое число:')
inx = len(input_number)-1
while input_number  :
    if int(input_number[inx]) > max_number:
       max_number = int(input_number[inx])
    inx-=1
    if inx < 0: break;
print(f'Максимальное введеное число: {max_number}')
