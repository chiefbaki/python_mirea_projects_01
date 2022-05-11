# Написать функцию order, которая отсортирует заданную строку. Каждое слово в строке
# содержит одну цифру. Эта цифра - позиция, которую слово должно занимать в результате.
#
# Пример:
# order("is2 Thi1s T4est 3a")  ==>  "Thi1s is2 3a T4est"

import traceback


def order(sentence):
    result = {}
    if len(sentence) == 0:
        return ""
    else:
        words = sentence.split(' ')

        for i in range(len(words)):
            result[i + 1] = ""

        for word in words:
            for letter in word:
                if letter.isdigit():
                    result[int(letter)] = word

    return " ".join(list(result.values()))

# Тесты
try:
    assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    assert order(
        "beli7eve Eve1rything if4 jus6t i2s y5ou 3possible") == "Eve1rything i2s 3possible if4 y5ou jus6t beli7eve"
    assert order("") == ""
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
