"""Convert string of input into pig latin.

best practice by: dykchui, alpharam, pomps, enfrightened, Wild_Pointer
  def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha()
    else word for word in lst])
"""


def pig_it(text):
    """Convert string to pig latin."""
    print(text)
    original = text.split(' ')
    pyg = 'ay'
    final = []
    for word in original:
        if len(word) > 0 and word.isalpha():
            first = word[0]
            new_word = word + first + pyg
            new_word = new_word[1: len(new_word)]
            final.append(new_word)
        else:
            final.append(word)
    return ' '.join(final)
