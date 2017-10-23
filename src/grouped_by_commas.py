"""Format integer input as number-like string with commas.

BEST PRACTICE - by mbaxa, SwinKing, and others

    def group_by_commas(n):
        return '{:,}'.format(n)
"""


def group_by_commas(n):
    """Create number-string with commas."""
    n_string = str(n)
    if len(n_string) <= 3:
        return n_string

    n_list = list(n_string)
    n_list.reverse()
    print(n_list)
    len_counter = 0
    while len_counter < len(n_list) and len(n_list) - len_counter > 3:
        print('this ran')
        len_counter += 3
        if n_list[len_counter]:
            n_list.insert(len_counter, ',')
        len_counter += 1
    n_list.reverse()
    print(''.join(n_list))
    return ''.join(n_list)
