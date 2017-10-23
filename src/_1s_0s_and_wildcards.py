"""Create list of possible srtrings using wildcards.

Best: by asmgf

from itertools import product

def possibilities(pattern):
    pattern_format = pattern.replace("?","{}")
    return [pattern_format.format(*values) for values in product('10',
    repeat=pattern.count('?'))]
"""


def possibilities(param):
    """Generate list of possibilities using wildcards."""
    print(param)
    exit_list = []
    qmark_indices = []
    word_as_list = list(param)
    for index, letter in enumerate(word_as_list):
        if letter is "?":
            qmark_indices.append(index)
    for num in qmark_indices:
        word_as_list[num] = "1"
        exit_list.append(''.join(word_as_list))
        word_as_list[num] = "0"
        exit_list.append(''.join(word_as_list))
    for num in qmark_indices:
        word_as_list[num] = "0"
        exit_list.append(''.join(word_as_list))
        word_as_list[num] = "1"
        exit_list.append(''.join(word_as_list))
    new_list = list(set(word for word in exit_list if word.count("?") == 0))
    new_list.sort()
    return new_list
