
"""Sort shuffled list of cards, sorted by rank.

Output is a list of cards sorted.
>>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7',
'J', '6', 'K'])
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

"""


def sort_cards(cards):
    """Sort cards - any means."""
    import re
    rx = re.compile('\d')
    rt = re.compile('[T]')
    ra = re.compile('[A]')
    rk = re.compile('[K]')
    rq = re.compile('[Q]')
    rj = re.compile('[J]')
    new_string = ''.join(sorted(cards))
    nums = rx.findall(new_string)
    aces = ra.findall(new_string)
    jacks = rj.findall(new_string)
    tens = rt.findall(new_string)
    queens = rq.findall(new_string)
    kings = rk.findall(new_string)

    return aces + nums + tens + jacks + queens + kings
