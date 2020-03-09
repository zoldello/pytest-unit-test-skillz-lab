import pytest

''' 
    System Under Test (SUT)
'''
class Arithmetic:
    def sum(self, a, b):
        return a + b


''' 
    Parametrize- Way to run a test with different parameters
'''
@pytest.mark.parametrize('num1, num2, expected', [(1, 2, 3), (3, -1, 2)])
def test_sum(num1, num2, expected):
    # arrange
    arithmetic = Arithmetic()
    
    # act
    target = arithmetic.sum(num1, num2)

    #assert
    assert target == expected
