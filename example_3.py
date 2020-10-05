
input_value = input('Введите положительное целое число:')
inx = 1
inx_max = 3
fin_str = ''
result_value = 0

while inx <= inx_max:
    tmp = input_value * inx
    if(inx < inx_max):
        fin_str += f'{tmp} + '
    else:
        fin_str += tmp
    result_value += int(tmp)
    inx+=1;

print(f'{fin_str} = {result_value}')

