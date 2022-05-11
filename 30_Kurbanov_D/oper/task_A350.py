# Написать функцию strong_enough(earthquake, age), которая вычисляет достаточно ли безопасное здание,
# чтобы выдержать землетрясение.  Здание рухнет, если сила землетрясения будет больше, чем сила здания.
# Earthquake – список, состоящий из спсика ударных волн.
# Вычисление силы землетрясения для [[5,3,7], [3,3,1], [4,1,2]]
# -> ((5 + 3 + 7) * (3 + 3 + 1) * (4+ 1 + 2)) = 735.
# Прочность нового здания 1000, при этом это значение уменьшается на 1% каждый год


import traceback


def strong_enough(earthquake, age):
    building_strong = 1000
    while age > 0:
        building_strong -= building_strong * 0.01
        age -= 1

    # gets earthquake strong
    quake_strong = 1
    for i in earthquake:
        quake_strong *= sum(i)

    return building_strong >= quake_strong

print(strong_enough([[5,8,7],[3,3,1],[4,1,2]], 3))

# Тесты
try:
    assert strong_enough([[2,3,1],[3,1,1],[1,1,2]], 2) == True
    assert strong_enough([[5,8,7],[3,3,1],[4,1,2]], 2) == True
    assert strong_enough([[5,8,7],[3,3,1],[4,1,2]], 3) == False
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
