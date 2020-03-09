import pytest

''' System under test (SUT) '''
class Arithmetic:
    def sum(self, a, b):
        return a + b

    def raise_exeception(self):
        raise NotImplementedError



'''  Unit Test '''
def test_raise_NotImplementedError():
    with pytest.raises(NotImplementedError): # this line "technically" is assert
        # arrange
        arithmetic = Arithmetic()
    
        # act
        target = arithmetic.raise_exeception()


# '''  Unit Test '''
# def test_raise_NotImplementedError():
#     with pytest.raises(ValueError):
#         # arrange
#         arithmetic = Arithmetic()
    
#         # act
#         target = arithmetic.raise_exeception()

#         #assert
#         # Should not make it to here
