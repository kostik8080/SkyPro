"""
Напишите функцию `get_price_with_discount(price, percentage)` которая получает сумму и уровень скидок и
возвращает цену с плавающей точкой(`price` - это цена. `percentage` - процент скидки, целое число. )

1000 - 1000 * (15 / 100)
Например:

`get_price_with_discount(1000, 10)` возвращает 900.0

`get_price_with_discount(500, 50)` возвращает 250.0
"""

def get_price_with_discount(price, percentage):
    return price - price * (percentage / 100)


result = get_price_with_discount(500, 50)
print(result)