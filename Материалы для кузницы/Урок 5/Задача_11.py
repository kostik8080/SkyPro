"""
У вас есть `get_rur_kop(value)` сумма в копейках, верните количество полных рублей

Подсказка: деление нацело x//y , остаток от деления: x%y

Например: `get_rur_kop(230)` вернет 2

Например: `get_rur_kop(590)` вернет 5
"""

def get_rur_kop(value):
    return  value // 100

result = get_rur_kop(590)
print(result)