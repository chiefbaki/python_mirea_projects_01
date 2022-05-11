# Написать функцию row_sum_odd_numbers(k), которая вычисляет сумму чисел на k-ой строчке
# треугольника нечетных чисел:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ....
#
# Пример:
# row_sum_odd_numbers(3)  => 27  -> 7 + 9 + 11 = 27


import traceback


def row_sum_odd_numbers(k):
    return sum(range(k * (k - 1) + 1, k * (k - 1) + 1 + k * 2, 2))

print(row_sum_odd_numbers(13))

# Тесты
try:
    assert row_sum_odd_numbers(1) == 1
    assert row_sum_odd_numbers(2) == 8
    assert row_sum_odd_numbers(13) == 2197
    assert row_sum_odd_numbers(19) == 6859
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")