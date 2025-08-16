from formatcity import format_city

def test_city():
    formatted_city = format_city('paris', 'france', 2048000)
    assert formatted_city == 'Paris, France - population 2048000'

def test_new_city():
    formatted_city = format_city('colchester', 'united kingdom')
    assert formatted_city == 'Colchester, United Kingdom'