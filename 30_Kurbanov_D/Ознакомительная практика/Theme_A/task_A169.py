# Напишите функцию opposite_house(address, n), которая определяет номер дома напротив дома со значением address, 
# при этом лица является совершенно прямой, по обе стороны которой находится ровно n одинаковых домов. 
# Нечетные номера домов слева и непрерывно увеличиваются, а четные справа и также увеличиваются.
# Улица выглядит так:
#  1 |       | 6
#  3 | улица | 4
#  5 |       | 2
#
# Примеры:
# opposite_house(2, 3) => 5 -> с каждой стороны улицы по три дома, напротив дома 2 находится дом 5

import traceback

def opposite_house(address, n):
    
    return 2*n + 1 - address
 
print(opposite_house(7,11))

# Тесты
try:
    assert opposite_house(1, 3) == 6
    assert opposite_house(3, 3) == 4
    assert opposite_house(2, 3) == 5
    assert opposite_house(3, 5) == 8
    assert opposite_house(7, 11) == 16
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")