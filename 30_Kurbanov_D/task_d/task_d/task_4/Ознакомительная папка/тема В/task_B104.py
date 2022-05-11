# Написать функцию break_camel_case, которая разбивает слова написанные CamelCase,
# используя в качестве разделителя пробел
#
# Примеры:
# break_camel_case("BreakCamelCase") ==> "Break Camel Case"

import traceback
import jsd


def break_camel_case(s):
    return " ".join(re.findall('^[a-z]+|[A-Z][^A-Z]*', s.replace(' ', '')))


# Тесты
try:
    assert break_camel_case("BreakCamelCase") == "Break Camel Case"
    assert break_camel_case("helloWorld") == "hello World"
    assert break_camel_case(
        "helloWorld BreakCamelCase") == "hello World Break Camel Case"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
