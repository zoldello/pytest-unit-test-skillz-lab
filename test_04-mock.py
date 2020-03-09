import requests
from unittest import mock

''' System Under Test (SUT)  '''
class Calculator:
    def sum(self, a, b):
        return a + b

    '''  
        RELEVANT METHOD! 
        Returns word count of json in URL
    '''
    def json_item_count(self, url):
        if not url:
            return None
        
        # breakpoint()
        response = requests.get(url)
        json_list = response.json()
        a = requests.status_codes
        #breakpoint()
        return len(json_list)


''' 
    Return Value of mocked (not always neccessary, not using is a pet peeve of mines)
'''
def _mocked_request_get():
    class MockedRequestGet:
        def json(self):
            fake_request_get_data = [
                {'song1': 'The Way you make me Feel'},
                {'song2': 'Another Part of me'},
                {'song3': 'Bad'}
            ]
            return fake_request_get_data

    return MockedRequestGet()


'''
    Unit Test
'''
@mock.patch('requests.get', return_value = _mocked_request_get())
def test_jsoncharacter_count_return_correct_character_count(mock_get):
    # arrange
    calc = Calculator()
    url = 'https://jsonplaceholder.typicode.com/posts'
    expected = 3

    # act
    target = calc.json_item_count(url)
    # breakpoint()
    
    # assert
    assert target == expected
    assert mock_get.called
    assert mock_get.call_count == 1

    # mock or a stub
    mock_get.assert_called_once() 
