import pytest


''' System under test (SUT) '''
class Arithmetic:
    def sum(self, a, b):
        return a + b



###############
# Fixture function ran before a consuming test (e.g. for getting data from file for a test)
###############

''' 
    Example #1
    fixture_from_conftest defined in conftest.py
'''
def test_sum(fixture_from_conftest):
    # arrange
    arithmetic = Arithmetic()
    expected = fixture_from_conftest
    
    # act
    target = arithmetic.sum(2, 2)

    #assert
    assert target == expected


'''  
    Example #2
    fixture_from_fixture_file defined in fixture.py
'''
def test_negative_number(fixture_from_fixture_file):
    # arrange
    arithmetic = Arithmetic()
    expected = fixture_from_fixture_file

    # act
    target = arithmetic.sum(-6, 9)

    # assert
    assert target == expected


'''
    Example #3
    fixture_in_this_test_file 
'''


# The fixture
@pytest.fixture
def fixture_in_this_test_file():
    return 0

def test_negative_number2(fixture_in_this_test_file):
    # arrange
    arithmetic = Arithmetic()
    expected = fixture_in_this_test_file

    # act
    target = arithmetic.sum(-5, 5)

    # assert
    assert target == expected
