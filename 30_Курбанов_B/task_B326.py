# Написать функцию parse_molecule, которая в строке, представляющей из себя молекулярную формулу,
# подсчитывает количество всех атомов и возвращает результат в виде словаря.
#
# Пример:
# water =
# parse_molecule('H2O') ==> {'H': 2, 'O': 1}
# parse_molecule('Mg(OH)2') ==> {'Mg': 1, 'O: 2, 'H': 2}


import traceback


def parse_molecule(formula):
    # ==========================================================================
    def get_tokens(formula):
        res = []
        i = 0
        while i < len(formula):
            token_cur = ''
            if formula[i].isalpha():
                token_cur += formula[i]
                i += 1
                while i < len(formula) and formula[i].isalpha() and formula[i].islower():
                    token_cur += formula[i]
                    i += 1
            elif formula[i].isdigit():
                while i < len(formula) and formula[i].isdigit():
                    token_cur += formula[i]
                    i += 1
            elif formula[i] in '()':
                token_cur += formula[i]
                i += 1
            elif formula[i] == '[':
                token_cur += '('
                i += 1
            elif formula[i] == ']':
                token_cur += ')'
                i += 1
            res.append(token_cur)
        return res

    # ==========================================================================
    def parse_tokens(tokens):
        # ======================================================================
        def get_right_br_ind(tokens, i_beg):
            st = []
            for i in range(i_beg, len(tokens)):
                if tokens[i] == '(':
                    st.append('(')
                elif tokens[i] == ')':
                    st.pop()
                    if not st:
                        return i

        # ======================================================================
        d_res = {}
        i = 0
        while i < len(tokens):
            if tokens[i][0].isalpha():
                if i == len(tokens) - 1 or not tokens[i + 1][0].isdigit():
                    d_res[tokens[i]] = d_res.get(tokens[i], 0) + 1
                    i += 1
                elif tokens[i + 1][0].isdigit():
                    d_res[tokens[i]] = d_res.get(tokens[i], 0) + int(tokens[i + 1])
                    i += 2
            elif tokens[i] == '(':
                ind = get_right_br_ind(tokens, i)
                d_sub = parse_tokens(tokens[i + 1: ind])
                k = 1
                i = ind + 1
                if ind < len(tokens) - 1 and tokens[ind + 1][0].isdigit():
                    k = int(tokens[ind + 1])
                    i = ind + 2
                for key in d_sub:
                    d_res[key] = d_res.get(key, 0) + d_sub[key] * k
        return d_res

    tokens = get_tokens(formula)
    return parse_tokens(tokens)

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