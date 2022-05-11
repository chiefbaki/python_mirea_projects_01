# Написать функцию recursive, которая задается рекурсивно:
# recursive(0) = 0
# recursive(1) = 1
# recursive(2n) = recursive(n)
# recursive(2n + 1) = recursive(n) + recursive(n + 1)


import traceback


def recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n % 2 == 0:
            return recursive(n // 2)
        else:
            return recursive(n // 2) + recursive(n // 2 + 1)


# Тесты
try:
    assert recursive(0) == 0
    assert recursive(1) == 1
    assert [recursive(i) for i in range(21)] == [0, 1, 1, 2,
                                                 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3]
    assert recursive(85) == 21
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
