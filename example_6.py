# first_day_res - результат первого дня
# end_res - желаемый результат
# end_day - счетчик дней

first_day_res = int(input("Введите результат первого дня (только целое число в км):"))
end_res = int(input("Введите желаемый результат (только целое число в км):"))
end_day = 1
print("Результат:")
print(f"{end_day}-й день: {first_day_res}")

while first_day_res <= end_res:
    first_day_res = first_day_res + first_day_res * 10/100
    end_day+=1
    print("%d-й день: %.2f" % (end_day,first_day_res))
print(f"Ответ: на {end_day}-й день спортсмен достиг результата - не менее {end_res}")
