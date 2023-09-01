"""
Напишите функцию, которая получит список покупок в виде словаря и вернет сумму.


def get_sum(purchases):
   ...

my_purchases = {
  "cookies": 400,
  "milk": 200,
  "banana": 100,
  "chocolate": 100
}

print(get_sum(my_purchases)) # вернет 800
"""


def get_sum(purchases):
    summ = 0
    for num in purchases.values():
        summ += num
    return summ

my_purchases = {
    "cookies": 400,
    "milk": 200,
    "banana": 100,
    "chocolate": 100
}


print(get_sum(my_purchases)) # вернет 800
