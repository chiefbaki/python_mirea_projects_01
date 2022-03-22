# На вход поступает список словарей. Написать функцию sentence, которая возвращает строку,
# состоящую из слов (значений словарей), разделенных пробелом в порядке возрастания
# целочисленных значений их ключей.
#
# Пример:
# [{"12": "back"}, {"0": "Never"}, {"7": "back"}] ==> "Never look back"


import traceback


def sentence(s):
    sorted_list = sorted(s, key=lambda x: list(map(int, x)))

    for d in sorted_list:
        print(*d.values(), end=' ')


#Тесты
try:
    assert sentence([{"0": "is"}, {"14": "never"}, {"-100": "Lost"}, {"75": "again"}, {"15": "found"},
                     {"-9": "time "}]) == "Lost time is never found again"
    assert sentence([{"100": "overeducated"}, {"0": "never"}, {"": "or"}, {"11": "overdressed"}, {"-500": "You"},
                     {"-2": "can"}, {"7": "be"}]) == "You can never be overdressed or overeducated"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")