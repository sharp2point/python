# Перебор списка с выводом типа элементов

lst = [1,1.78,True,"Hello world !"
        ,[1,2],(1,2),{1,2}
        ,{1:"Name",2:"Family"}]
for i in enumerate(lst):
    parse_el_type = str(type(i[1])).strip(">").split()
    print(f"{i[0]}. Элемент: {i[1]} : имеет тип: {parse_el_type[1]}")