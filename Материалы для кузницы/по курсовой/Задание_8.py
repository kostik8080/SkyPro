"""
Напишите функцию, которая получит список покупок в виде словаря и вернет словарь, который будет содержать ключи:

`min` – минимальная покупка

`max` – максимальная покупка

`sum` – cумма покупок


"""

def purchase_stats(purchases):
    summ = 0
    min_summ = min(purchases.values())
    max_summ = max(purchases.values())
    for num in purchases.values():
        summ += num

    return {"min": min_summ, "max": max_summ, "sum": summ}


# для тестирования

my_purchases = {
  "cookies": 400,
  "milk": 200,
  "banana": 100,
  "chocolate": 50
}

print(purchase_stats(my_purchases))

# вернет {"min": 50, "max": 400, "sum": 750}
