'''
Why we do bin/test -m "not bdd"

- bin/test has (1)shebang [no neeed for python bin/test.py] (2)pytest.main()
- -m means "look for marker"
- No unit or integration test in ENCODE has pytest.mark.bdd
'''

import pytest

@pytest.mark.bdd
def test_true_is_tru():
    assert 1 == 1
