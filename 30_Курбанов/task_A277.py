# Написать функцию goldbach(n) для иллюстрации гипотезы Гольдбаха: каждое четное целое число больше 2 
# может быть записано как сумма двух простых чисел. 
# Если аргумент нечетный, верните пустой список.
# Для четных аргументов необходимо вернуть список с двумя простыми числами, сумма которых равна n. 
# Два простых числа должны быть самыми дальними (с наибольшей разницей). Первое простое число должно быть наименьшим.
#
# Пример:
# goldbach(15) ==> []
# goldbach(4) ==> [2, 2]
# goldbach(14) ==> [3, 11]


import traceback


def goldbach(n):
    def isPrime(n):
        if (n + 1) % 2:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n

    if n == 4:
        return [2, 2]
    elif n % 2 or n < 4:
        return []
    k = 3
    while True:
        if isPrime(k) and isPrime(n - k):
            return [k, n - k]
        k += 2


# Тесты
try:
    assert goldbach(15) == []
    assert goldbach(4) == [2, 2]
    assert goldbach(10) == [3, 7]
    assert goldbach(24) == [5, 19]
    assert goldbach(100) == [3, 97]
    assert goldbach(1234) == [3, 1231]

except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

