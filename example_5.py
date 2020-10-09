#задание № 5 сортировка списка
sorted_list=[]
while True:
    code = input("Введите целое число:").strip(' ')
    if not code.isnumeric(): # выход из цикла
        break;
    input_numb = int(code)
    sorted_list.append(input_numb)
    sorted_list.sort()
    sorted_list.reverse()
    print(f"Результат: {str(sorted_list).strip('][')}")
          
