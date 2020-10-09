str_lst = input("Введите список элементов через пробел:")
# преобразование введеной строки в список
lst = str_lst.strip(' ').split(' ')
# динна списка
lst_length = len(lst)
# четность длинны списка если 0-четн. если 1-нечет.
od_or_ev_lst = []
od_or_ev_lst.append(lst_length%2)
if lst_length%2 == 0:
    od_or_ev_lst.append("Четно")
else:
    od_or_ev_lst.append("НеЧетно")

print(f"Прямой порядок: {lst}")
print(f"Длинна списка: {lst_length}, {od_or_ev_lst[1]}")

# преобразование списка
inx = 0
if od_or_ev_lst == 0:
    while inx < lst_length:
        lst[inx],lst[inx+1] = lst[inx+1],lst[inx]
        inx += 2
else:
    while inx < lst_length-1:
        lst[inx], lst[inx + 1] = lst[inx + 1], lst[inx]
        inx += 2
print(f"Измененный порядок: {lst}")
