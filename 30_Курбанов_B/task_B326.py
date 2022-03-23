# Написать функцию parse_molecule, которая в строке, представляющей из себя молекулярную формулу,
# подсчитывает количество всех атомов и возвращает результат в виде словаря.
#
# Пример:
# water =
# parse_molecule('H2O') ==> {'H': 2, 'O': 1}
# parse_molecule('Mg(OH)2') ==> {'Mg': 1, 'O: 2, 'H': 2}


import traceback


def parse_molecule(formula):
    element = ""
    atom_count = 0
    element_hash = {}

    for x in formula:
        if x.isupper():
            if element != "":
                element_hash[element] = 1
                element = ""
            element = x

        elif x.islower():
            element += x            

        else: 
            element_count = int(x)
            element_hash[element] = element_count
            element_count = 0
            element = ""

    if element!="":
        element_hash[element] = 1

    return element_hash

w = "Mg(OH)2"    
print(parse_molecule(w))

# Тесты
try:
    assert parse_molecule("H2O") == {'H': 2, 'O': 1}
    assert parse_molecule("Mg(OH)2") == {'Mg': 1, 'O': 2, 'H': 2}
    assert parse_molecule("K4[ON(SO3)2]2") == {'K': 4, 'O': 14, 'N': 2, 'S': 4}
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
