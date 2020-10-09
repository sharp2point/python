# задание номер 6 структура данных Товары
product_index = 1
product_list = []
product_dict = {}
attr_list = ["название","цена","количество","ед"]

# цикл ввода атрибутов товара
while True:
    print(f"Задайте атрибуты товара N{product_index}:")
    tmp_dict = {}
    for i in attr_list:
        tmp = input(f"{i} товара:")
        tmp_dict[i] = tmp

    tmp_tuple = (product_index,tmp_dict)
    product_list.append(tmp_tuple)
    product_index+=1

    quit_or_onward = input("Введите 'quit' для выхода "
                           "или нажмите ENTER:")
    if quit_or_onward == 'quit':
        break
# Вывод кортежей товаров
print("\nВаши товары:\n")
for product in product_list:
    print(product)

# формирование словаря по атрибутам
for attr in attr_list:
    tmp_list = []
    for i in product_list:
        tmp = i[1][attr]
        tmp_list.append(tmp)
    product_dict[attr] = tmp_list
# вывод словаря
print("\nСловарь аттрибутов товаров:\n")
for k,v in product_dict.items():
    print(f"{k} : {v}")