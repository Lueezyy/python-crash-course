from formatname import get_formatted_name

def test_first_last_name():
    '''Do names like 'Luis Doe' work?'''
    formatted_name = get_formatted_name('luis', 'doe')
    assert formatted_name == 'Luis Doe'