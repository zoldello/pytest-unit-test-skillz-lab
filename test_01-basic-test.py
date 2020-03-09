''' System under test (SUT) '''
class Arithmetic:
    def sum(self, a, b):
        return a + b


'''
    Unit Test
'''
def test_sum_two_numbers():
    # arrange
    arithmetic = Arithmetic()
    expected = 3
    
    # act
    target = arithmetic.sum(1, 2)

    #assert
    assert target == expected
 


'''
    Demo of specific test exception
'''
def test_sum_two_numbers_second_test():
    # arrange
    arithmetic = Arithmetic()
    expected = 3
    
    # act
    target = arithmetic.sum(1, 2)

    # alternate assert
    assert target == expected, 'summation fail'

    # DON'T WRITE!!!!!!!
    #assert(target == expected, 'summation fail')
