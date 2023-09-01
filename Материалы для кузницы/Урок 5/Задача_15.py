"""
Напишите функцию `get_price_with_discount(price, level)`, которая получает сумму и уровень скидок и возвращает
 цену с плавающей точкой(`price` - это цена. `level` - уровень скидки, целое число. )

**Уровень 1** - 10%

**Уровень 2** - 25%

**Уровень 3** - 50%

Например:

`get_price_with_discount(1000, 1)` возвращает 900.0

`get_price_with_discount(500, 3)` возвращает 250.0
"""

def get_price_with_discount(price, level):
    discount = {
        1: 0.1,
        2: 0.25,
        3: 0.5
    }
    return price * (1 - discount[level])

result = get_price_with_discount(1000, 3)
print(result)