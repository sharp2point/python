print('Печать визитки для вашей собаки:')
dog_spec = input('Порода собаки ?:')
dog_name = input('Кличка собаки ?:')
dog_age = int(input('Возраст собаки ?:'))
dog_owner_phone = input('Телефон хозяина ?:')

print('\t Ваша визитка готова:\n')
print(f'Моя кличка: {dog_name} \n Я: {dog_spec} \n Мне уже: {dog_age} \n'
      f'И если я потерялся звоните хозяину:\n \t{dog_owner_phone}')
