""""Test pig latin function."""
import pytest

PIG_LATIN_TABLE = [('Pig latin is cool', 'igPay atinlay siay oolcay'),
                   ('This is my string', 'hisTay siay ymay tringsay'),
                   ('Robert Bronson', 'obertRay ronsonBay'),
                   ('Nice string bro', 'iceNay tringsay robay'),
                   ('Drink more ovaltine', 'rinkDay oremay valtineoay'),
                   ('Go go Power Rangers', 'oGay ogay owerPay angersRay')]


@pytest.mark.parametrize('string_in, result', PIG_LATIN_TABLE)
def test_pig_it(string_in, result):
    """Verify expected pig latin is produced."""
    from simple_pig_latin import pig_it
    assert pig_it(string_in) == result
