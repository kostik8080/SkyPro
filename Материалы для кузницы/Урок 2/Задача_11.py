"""В переменных is_weekend и has_vacation хранится два булевых значения

```
is_weekend = True # сейчас выходные
has_vacation = True # сейчас каникулы
```

Если у нас каникулы - выведите "не идем на работу"Если у нас будний день и нет каникул - выведите 
"идем на работу"Если у нас выходной - выведите  "не идем на работу". Изменяйте значения ,
чтобы проверить работу программы (отредактировано)"""

is_weekend = True # сейчас выходные
has_vacation = True # сейчас каникулы
# weekend_bool = bool(input("Введите True/False"))
# vacation_bool = bool(input("Введите True/False"))

if is_weekend is True:
    print("не идем на работу")
elif has_vacation is True:
    print("не идем на работу")
elif is_weekend == False and has_vacation == False:
    print('идем на работу')